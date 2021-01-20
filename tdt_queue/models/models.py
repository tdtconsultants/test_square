# -*- coding: utf-8 -*-
from odoo import models, fields, api
from queue import Queue
import pika
import sys
import threading
import json
from pytz import timezone
import datetime


class TdtQueue(models.Model):
    _name = "tdt_queue"

    name = fields.Char(string="Customer")
    type_jobs = fields.Char(string="Tipo de jobs")

    def _parse_dic_from_square_to_odoo(self, square_dic):
        parsed_message = square_dic
        if 'key' in parsed_message and parsed_message['key'] != 'odoo':

            new_customer = parsed_message
            if 'address_line_1' in new_customer['address']:
                address_line_1 = new_customer['address']['address_line_1']
            else:
                address_line_1 = 'Test address_line1'

            if 'address_line_2' in new_customer['address']:
                address_line_2 = new_customer['address']['address_line_2']
            else:
                address_line_2 = 'Test address_line2'

            if 'company_name' in new_customer:
                company_name = new_customer['company_name']
            else:
                company_name = 'Test company_name'

            if 'nickname' in new_customer:
                nickname = new_customer['nickname']
            else:
                nickname = 'Test nickname'

            if 'email_address' in new_customer:
                email_address = new_customer['email_address']
            else:
                email_address = 'Test email_address'

            if 'phone_number' in new_customer:
                phone_number = new_customer['phone_number']
            else:
                phone_number = 'Test phone_number'

            if 'postal_code' in new_customer['address']:
                postal_code = new_customer['address']['postal_code']
            else:
                postal_code = 'Test postal_code'

            if 'country' in new_customer['address']:
                country_code = new_customer['address']['country']
                country_res = self.env['res.country'].search([['code', '=', country_code]])
                if country_res:
                    country = country_res.id
                else:
                    country = None
            else:
                country = None

            if 'note' in new_customer:
                note = new_customer['note']
            else:
                note = 'Test note'

            if 'administrative_district_level_1' in new_customer['address']:
                administrative_district_level_1_code = new_customer['address']['administrative_district_level_1']
                country_res_state = self.env['res.country.state'].search([['code', '=', 'NY']])
                if country_res_state:
                    administrative_district_level_1_id = country_res_state.id
                else:
                    administrative_district_level_1_id = 'Test state_id'

            else:
                administrative_district_level_1_id = None

            if 'locality' in new_customer['address']:
                locality = new_customer['address']['locality']
            else:
                locality = 'Test locality'

            if 'id' in new_customer:
                id = new_customer['id']
            else:
                id = 'Test id'

            parsed_dict = {
                'name': new_customer['given_name'] + ' ' + new_customer['family_name'],
                'street': address_line_1,
                'street2': address_line_2,
                'company_name': company_name,
                'display_name': nickname,
                'email': email_address,
                'mobile': phone_number,
                'zip': postal_code,
                'country_id': country,
                'city': locality,
                'state_id': administrative_district_level_1_id,
                'square_id': id,
                'additional_info': note
            }
            return parsed_dict

    def _parse_resPartner_to_square_dic(self, partner):
        name = str.split(partner.name)
        given_name = name[0]
        family_name = name[1]
        if partner.state_id:
            #country_res_state = self.env['res.country.state'].search([['id', '=', 'partner.state_id']])
            administrative_district_level_1_code = partner.state_id.code
        else:
            administrative_district_level_1_code = ''

        if partner.country_id:
            #country_res = self.env['res.country'].search([['id', '=', 'partner.country_id']])
            country = partner.country_id.code
        else:
            country = ''

        if partner.additional_info:
            note = partner.additional_info
        else:
            note = ''

        if partner.email:
            email_address = partner.email
        else:
            email_address = ''

        square_dic = {
            'id': '123',
            'given_name': given_name,
            'family_name': family_name,
            'nickname': partner.display_name,
            'email_address': email_address,
            'address': {'address_line_1': partner.street, 'address_line_2': partner.street2,'locality': partner.city,'administrative_district_level_1': administrative_district_level_1_code,'postal_code': partner.zip,'country': country},
            'phone_number': partner.mobile,
            'note': note,
            'company_name': partner.company_name,
            'key': 'odoo',
        }
        return square_dic

    def _active_cron_task(self):

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        #Create queue if it doesn't exist
        #channel_cron.queue_declare(queue='odoo_queue', exclusive=True)
        #Create exchange if it doesn't exist
        #channel_cron.exchange_declare(exchange='master_exchange', exchange_type='fanout')
        #Bind queue and exchange if they aren't already
        #channel_cron.queue_bind(queue='odoo_queue', exchange='master_exchange', routing_key='')

        result = channel.basic_get('odoo_queue', auto_ack=True)

        if None in result:
            channel.close()
            connection.close()
        else:
            while result[0].message_count >= 0:
                parsed_message = json.loads(result[2])
                dict = self._parse_dic_from_square_to_odoo(parsed_message)
                partner_square_id = self.env['res.partner'].search([['square_id', '=', parsed_message['id']]])
                partner_odoo_id = self.env['res.partner'].search([['id', '=', parsed_message['reference_id']]])
                if partner_square_id:
                    #Si lo encuentra por square_id significa que odoo ya recibio informacion de este customer de square, por lo tanto este cliente en square ya tiene en el campo reference_id la id de odoo
                    partner_square_id.update(dict)
                elif partner_odoo_id:
                    #Si no lo encuentra por square_id pero lo encuentra por reference_id, significa que odoo creo este cliente y lo envio a square, square lo creo en su sistema y en reference_id puso la id de odoo.
                    #Lo que hay que hacer es agregar la referencia en square_id
                    partner_odoo_id.update({'square_id': parsed_message['id']})
                else:
                    # Si no encuentra por square_id ni por id de odoo significa que esta es la primera vez que odoo sabe de este cliente
                    # Entonces lo crea, en el campo square_id pone el id del customer de square y manda un mensaje a square para que èste actualize el campo reference_id con la id de odoo
                    new_customer = self.env['res.partner'].create(dict)
                    parsed_message['reference_id'] = new_customer.id
                    message = json.dumps(parsed_message)
                    channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
                if result[0].message_count == 0:
                    break
                result = channel.basic_get('odoo_queue', auto_ack=True)
            channel.close()
            connection.close()

    def _active_cron_sender_task(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        tzu = timezone(self.env.user.tz)
        tz = timezone('UTC')
        last_execution_date = tz.localize(self.env['ir.cron'].browse(21).lastcall).astimezone(tzu)
        modified_customers = self.env['res.partner'].search([['write_date', '>=', last_execution_date]])
        for cust in modified_customers:
            dict = self._parse_resPartner_to_square_dic(cust)
            message = json.dumps(dict)
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
        channel.close()
        connection.close()
