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

    def _parse_odoo_to_general(self, partner):

        name = str.split(partner.name)
        general_first_name = name[0]
        general_last_name = name[1]

        if partner.company_name:
            general_company_name = partner.company_name
        else:
            general_company_name = None

        if partner.display_name:
            general_nickname = partner.display_name
        else:
            partner.display_name = None

        if partner.state_id:
            state_id = partner.state_id.code
        else:
            state_id = None

        if partner.country_id:
            country_code = partner.country_id.code
        else:
            country_code = None

        if partner.square_id:
            square_id = partner.square_id
        else:
            square_id = None

        if partner.email:
            general_email_address = partner.email
        else:
            general_email_address = None

        if partner.mobile:
            general_phone_number = partner.mobile
        else:
            general_phone_number = None

        if partner.additional_info:
            general_note = partner.additional_info
        else:
            general_note = None

        if partner.street:
            general_address_line_1 = partner.street
        else:
            general_address_line_1 = None

        if partner.street2:
            general_address_line_2 = partner.street2
        else:
            general_address_line_2 = None

        if partner.city:
            general_locality = partner.city
        else:
            general_locality = None

        if partner.zip:
            general_postal_code = partner.zip
        else:
            general_postal_code = None

        general_dic = {
            'general_first_name': general_first_name,
            'general_last_name': general_last_name,
            'general_company_name': general_company_name,
            'general_nickname': partner.display_name,
            'general_email_address': general_email_address,
            'general_phone_number': general_phone_number,
            'general_note': general_note,
            'square_id': square_id,
            'odoo_id': partner.id,
            'general_address_line_1': general_address_line_1,
            'general_address_line_2': general_address_line_2,
            'general_locality': general_locality,
            'general_administrative_district_level_1': state_id,
            'general_postal_code': general_postal_code,
            'general_country': country_code,
            'key': 'odoo',
        }
        return general_dic

    def _parse_general_to_odoo(self, general_dic):

        if 'general_country' in general_dic and general_dic['general_country'] is not None:
            country_code = general_dic['general_country']
            country_res = self.env['res.country'].search([('code', '=', country_code)])
            if country_res:
                country = country_res.id
            else:
                country = None
        else:
            country = None

        if 'general_administrative_district_level_1' in general_dic and general_dic['general_administrative_district_level_1'] is not None:
            state_id_code = general_dic['general_administrative_district_level_1']
            country_res_state = self.env['res.country.state'].search([('code', '=', state_id_code)])
            if country_res_state:
                state_id = country_res_state.id
            else:
                state_id = None
        else:
            state_id = None

        if 'general_first_name' in general_dic and 'general_first_name' is not None:
            fname = general_dic['general_first_name']
        else:
            fname = ''

        if 'general_last_name' in general_dic and general_dic['general_last_name'] is not None:
            lname = general_dic['general_last_name']
        else:
            lname = ''

        if 'general_address_line_1' in general_dic:
            street = general_dic['general_address_line_1']
        else:
            street = None

        if 'general_address_line_2' in general_dic:
            street2 = general_dic['general_address_line_2']
        else:
            street2 = None

        if 'general_company_name' in general_dic:
            company_name = general_dic['general_company_name']
        else:
            company_name = None

        if 'general_nickname' in general_dic:
            display_name = general_dic['general_nickname']
        else:
            display_name = None

        if 'general_email_address' in general_dic:
            email = general_dic['general_email_address']
        else:
            email = None

        if 'general_phone_number' in general_dic:
            mobile = general_dic['general_phone_number']
        else:
            mobile = None

        if 'general_postal_code' in general_dic:
            zip = general_dic['general_postal_code']
        else:
            zip = None

        if 'general_locality' in general_dic:
            city = general_dic['general_locality']
        else:
            city = None

        if 'square_id' in general_dic:
            square_id = general_dic['square_id']
        else:
            square_id = None

        if 'general_note' in general_dic:
            additional_info = general_dic['general_note']
        else:
            additional_info = None

        odoo_dic = {
            'name': fname + ' ' + lname,
            'street': street,
            'street2': street2,
            'company_name': company_name,
            'display_name': display_name,
            'email': email,
            'mobile': mobile,
            'zip': zip,
            'country_id': country,
            'city': city,
            'state_id': state_id,
            'square_id': general_dic['square_id'],
            #'additional_info': general_dic['general_note']
        }
        return odoo_dic

    def _active_cron_task(self):

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        result = channel.basic_get('odoo_queue', auto_ack=True)

        if None in result:
            channel.close()
            connection.close()
        else:
            while result[0].message_count >= 0:
                parsed_message = json.loads(result[2])
                if 'key' in parsed_message and parsed_message['key'] != 'odoo':
                    dict = self._parse_general_to_odoo(parsed_message) #self._parse_general_dic_to_odoo(parsed_message)
                    partner_square_id = self.env['res.partner'].search([('square_id', '=', dict['square_id'])])
                    partner_odoo_id = self.env['res.partner'].search([('id', '=', parsed_message['odoo_id'])])
                    if partner_square_id:
                        #Si lo encuentra por square_id significa que odoo ya recibio informacion de este customer de square, por lo tanto este cliente en square ya tiene en el campo reference_id la id de odoo
                        partner_square_id.update(dict)
                    elif partner_odoo_id:
                        #Si no lo encuentra por square_id pero lo encuentra por reference_id, significa que odoo creo este cliente y lo envio a square, square lo creo en su sistema y en reference_id puso la id de odoo.
                        #Lo que hay que hacer es agregar la referencia en square_id
                        #Pueden haber mas cambios ademas del square id
                        partner_odoo_id.update(dict)
                    else:
                        # Si no encuentra por square_id ni por id de odoo significa que esta es la primera vez que odoo sabe de este cliente
                        # Entonces lo crea, en el campo square_id pone el id del customer de square y manda un mensaje a square para que èste actualize el campo reference_id con la id de odoo
                        new_customer = self.env['res.partner'].create(dict)
                        parsed_message['odoo_id'] = new_customer.id
                        parsed_message['key'] = 'odoo'
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
        modified_customers = self.env['res.partner'].search([('create_date', '>=', last_execution_date)])
        for cust in modified_customers:
            dict = self._parse_odoo_to_general(cust)#self._parse_resPartner_to_general_dic(cust)
            message = json.dumps(dict)
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
        channel.close()
        connection.close()
