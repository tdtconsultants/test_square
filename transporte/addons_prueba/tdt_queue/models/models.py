# -*- coding: utf-8 -*-
from odoo import models, fields, api
from queue import Queue
import pika
import sys
import json
from pytz import timezone
import datetime

class TdtQueue(models.Model):
    _name = "tdt_queue"

    name = fields.Char(string="Customer")
    type_jobs = fields.Char(string="Tipo de jobs")

    def _parse_odoo_customer_to_general(self, partner):

        general_dic = {}

        if partner.family_name:
            general_dic['family_name'] = partner.family_name
        if partner.given_name:
            general_dic['given_name'] = partner.given_name
        if partner.birthday:
            general_dic['birthday'] = partner.birthday
        if partner.company_name:
            general_dic['company_name'] = partner.company_name
        if partner.email:
            general_dic['email_address'] = partner.email
        if partner.display_name:
            general_dic['nickname'] = partner.display_name
        if partner.note:
            general_dic['note'] = partner.note
        if partner.mobile:
            general_dic['phone_number'] = partner.mobile
        general_dic['reference_id'] = str(partner.id)

        general_dic['address'] = {}

        if partner.street:
            general_dic['address']['address_line_1'] = partner.street
        if partner.street2:
            general_dic['address']['address_line_2'] = partner.street2
        if partner.street3:
            general_dic['address']['address_line_3'] = partner.street3
        if partner.administrative_district_level_1:
            general_dic['address']['administrative_district_level_1'] = partner.administrative_district_level_1
        if partner.administrative_district_level_2:
            general_dic['address']['administrative_district_level_2'] = partner.administrative_district_level_2
        if partner.administrative_district_level_3:
            general_dic['address']['administrative_district_level_3'] = partner.administrative_district_level_3
        if partner.country_id:
            general_dic['address']['country'] =  partner.country_id.code
        if partner.city:
            general_dic['address']['locality'] = partner.city
        if partner.zip:
            general_dic['address']['postal_code'] = partner.zip
        if partner.sublocality:
            general_dic['address']['sublocality'] = partner.sublocality
        if partner.sublocality2:
            general_dic['address']['sublocality_2'] = partner.sublocality2
        if partner.sublocality3:
            general_dic['address']['sublocality_3'] = partner.sublocality3

        if partner.square_id:
            square_id = partner.square_id
        else:
            square_id = None

        square_dic = {
            'key': 'odoo',
            'type': 'customer',
            'data': general_dic,
            'square_id': square_id
        }
        return square_dic

    def _parse_general_customer_to_odoo(self, general_dic):

        odoo_dic = {}
        if 'address_line_1' in general_dic['address']:
            odoo_dic['street'] = general_dic['address']['address_line_1']
        if 'address_line_2' in general_dic['address']:
            odoo_dic['street2'] = general_dic['address']['address_line_2']
        if 'address_line_3' in general_dic['address']:
            odoo_dic['street3'] = general_dic['address']['address_line_3']
        if 'administrative_district_level_1' in general_dic['address']:
            odoo_dic['administrative_district_level_1'] = general_dic['address']['administrative_district_level_1']
        if 'administrative_district_level_2' in general_dic['address']:
            odoo_dic['administrative_district_level_2'] = general_dic['address']['administrative_district_level_2']
        if 'administrative_district_level_3' in general_dic['address']:
            odoo_dic['administrative_district_level_3'] = general_dic['address']['administrative_district_level_3']
        if 'country' in general_dic['address']:
            country_code = general_dic['address']['country']
            country_res = self.env['res.country'].search([('code', '=', country_code)])
            if country_res:
                odoo_dic['country_id'] = country_res.id
        if 'locality' in general_dic['address']:
            odoo_dic['city'] = general_dic['address']['locality']
        if 'organization' in general_dic['address']:
            odoo_dic['organization'] = general_dic['address']['organization']
        if 'postal_code' in general_dic['address']:
            odoo_dic['zip'] = general_dic['address']['postal_code']
        if 'sublocality' in general_dic['address']:
            odoo_dic['sublocality'] = general_dic['address']['sublocality']
        if 'sublocality_2' in general_dic['address']:
            odoo_dic['sublocality2'] = general_dic['address']['sublocality_2']
        if 'sublocality_3' in general_dic['address']:
            odoo_dic['sublocality3'] = general_dic['address']['sublocality_3']
        if 'birthday' in general_dic:
            odoo_dic['birthday'] = general_dic['birthday']
        if 'company_name' in general_dic:
            odoo_dic['company_name'] = general_dic['company_name']
        if 'email_address' in general_dic:
            odoo_dic['email'] = general_dic['email_address']
        if 'family_name' in general_dic:
            odoo_dic['family_name'] = general_dic['family_name']
        if 'given_name' in general_dic:
            odoo_dic['given_name'] = general_dic['given_name']
        odoo_dic['name'] = general_dic['given_name'] + ' ' + general_dic['family_name']
        if 'nickname' in general_dic:
            odoo_dic['display_name'] = general_dic['nickname']
        if 'note' in general_dic:
            odoo_dic['note'] = general_dic['note']
        if 'phone_number' in general_dic:
            odoo_dic['mobile'] = general_dic['phone_number']
        odoo_dic['square_id'] = general_dic['id']

        return odoo_dic

    def _parse_general_payment_to_odoo(self, general_payment):
        odoo_payment = {}

        odoo_payment['payment_square_id'] = general_payment['id']
        if 'amount_money' in general_payment:
            odoo_payment['amount'] = general_payment['amount_money']['amount']
            currency = self.env['res.currency'].search([('name', '=', general_payment['amount_money']['currency'])])
            odoo_payment['currency_id'] = currency.id
        if 'tip_money' in general_payment:
            odoo_payment['tip_amount'] = general_payment['tip_money']['amount']
            currency_tip = self.env['res.currency'].search([('name', '=', general_payment['tip_money']['currency'])])
            odoo_payment['tip_currency_id'] = currency_tip.id
        if 'app_fee_money' in general_payment:
            odoo_payment['app_fee_amount'] = general_payment['app_fee_money']['amount']
            currency_fee = self.env['res.currency'].search([('name', '=', general_payment['app_fee_money']['currency'])])
            odoo_payment['app_fee_currency_id'] = currency_fee.id
        if 'status' in general_payment:
            odoo_payment['payment_status'] = general_payment['status']
        if 'source_type' in general_payment:
            odoo_payment['payment_status'] = general_payment['source_type']
        if 'location_id' in general_payment:
            odoo_payment['square_location_id'] = general_payment['location_id']
        if 'order_id' in general_payment:
            odoo_payment['square_order_id'] = general_payment['order_id']
        if 'buyer_email_address' in general_payment:
            odoo_payment['buyer_email_address'] = general_payment['buyer_email_address']
        if 'note' in general_payment:
            odoo_payment['note'] = general_payment['note']
        if 'customer_id' in general_payment:
            odoo_payment['square_customer_id'] = general_payment['customer_id']
        if 'receipt_number' in general_payment:
            odoo_payment['square_receipt_number'] = general_payment['receipt_number']
        if 'receipt_url' in general_payment:
            odoo_payment['square_receipt_url'] = general_payment['receipt_url']

        return odoo_payment

    def _parse_odoo_payment_to_general(self):
        return {}

    def _parse_general_location_to_odoo(self,general_location):
        odoo_location = {}
        search_list = []
        if 'address' in general_location:
            if 'address_line_1' in general_location['address']:
                search_list.append(('address_line_1', '=', general_location['address']['address_line_1']))
            if 'address_line_2' in general_location['address']:
                search_list.append(('address_line_2', '=', general_location['address']['address_line_2']))
            if 'address_line_3' in general_location['address']:
                search_list.append(('address_line_3', '=', general_location['address']['address_line_3']))

        search_result = self.env['square.address'].search(search_list)
        if  search_result and search_list:
            #Significa que la direccion ya esta ingresada en odoo
            odoo_location['square_address_id'] = search_result[0].id
        else:
            new_address = self.env['square.address'].create(general_location['address'])
            odoo_location['square_address_id'] = new_address.id
        self.env.cr.commit()
        odoo_location['square_location_id'] = general_location['id']
        if 'name' in general_location:
            odoo_location['name'] = general_location['name']
            odoo_location['code'] = general_location['name']
        else:
            odoo_location['name'] = ''
            odoo_location['code'] = ''
        if 'timezone' in general_location:
            odoo_location['timezone'] = general_location['timezone']
        if 'status' in general_location:
            odoo_location['status'] = general_location['status']
        if 'language_code' in general_location:
            odoo_location['language_code'] = general_location['language_code']
        if 'currency' in general_location:
            odoo_location['currency'] = general_location['currency']
        if 'phone_number' in general_location:
            odoo_location['phone_number'] = general_location['phone_number']
        if 'business_name' in general_location:
            odoo_location['business_name'] = general_location['business_name']
        if 'twitter_username' in general_location:
            odoo_location['twitter_username'] = general_location['twitter_username']
        if 'instagram_username' in general_location:
            odoo_location['instagram_username'] = general_location['instagram_username']
        if 'facebook_url' in general_location:
            odoo_location['facebook_url'] = general_location['facebook_url']
        if 'mcc' in general_location:
            odoo_location['mcc'] = general_location['mcc']
        if 'description' in general_location:
            odoo_location['description'] = general_location['description']

        odoo_location['code'] = general_location['name']

        odoo_location['square_warehouse'] = True
        return odoo_location

    def _parse_odoo_location_to_general(self, odoo_location):
        general_dic = {}
        general_dic['location'] = {}
        if odoo_location.business_email:
            general_dic['location']['business_email'] = odoo_location.business_email
        if odoo_location.business_name:
            general_dic['location']['business_name'] = odoo_location.business_name
        if odoo_location.description:
            general_dic['location']['description'] = odoo_location.description
        if odoo_location.facebook_url:
            general_dic['location']['facebook_url'] = odoo_location.facebook_url
        if odoo_location.instagram_username:
            general_dic['location']['instagram_username'] = odoo_location.instagram_username
        if odoo_location.language_code:
            general_dic['location']['language_code'] = odoo_location.language_code
        if odoo_location.mcc:
            general_dic['location']['mcc'] = odoo_location.mcc
        if odoo_location.name:
            general_dic['location']['name'] = odoo_location.name
        if odoo_location.phone_number:
            general_dic['location']['phone_number'] = odoo_location.phone_number
        if odoo_location.status:
            general_dic['location']['status'] = odoo_location.status
        if odoo_location.timezone:
            general_dic['location']['timezone'] = odoo_location.timezone
        if odoo_location.twitter_username:
            general_dic['location']['twitter_username'] = odoo_location.twitter_username
        if odoo_location.type:
            general_dic['location']['type'] = odoo_location.type
        if odoo_location.website_url:
            general_dic['location']['website_url'] = odoo_location.website_url
        if odoo_location.square_address_id:
            address = self.env['square.address'].browse(odoo_location.square_address_id.id)
            general_dic['location']['address'] = {}
            if address.address_line_1:
                general_dic['location']['address']['address_line_1'] = address.address_line_1
            if address.address_line_2:
                general_dic['location']['address']['address_line_2'] = address.address_line_2
            if address.address_line_3:
                general_dic['location']['address']['address_line_3'] = address.address_line_3
            if address.administrative_district_level_1:
                general_dic['location']['address']['administrative_district_level_1'] = address.administrative_district_level_1
            if address.administrative_district_level_2:
                general_dic['location']['address']['administrative_district_level_2'] = address.administrative_district_level_2
            if address.administrative_district_level_3:
                general_dic['location']['address']['administrative_district_level_3'] = address.administrative_district_level_3
            if address.country:
                general_dic['location']['address']['country'] = address.country
            if address.first_name:
                general_dic['location']['address']['first_name'] = address.first_name
            if address.last_name:
                general_dic['location']['address']['last_name'] = address.last_name
            if address.locality:
                general_dic['location']['address']['locality'] = address.locality
            if address.organization:
                general_dic['location']['address']['organization'] = address.organization
            if address.postal_code:
                general_dic['location']['address']['postal_code'] = address.postal_code
            if address.sublocality:
                general_dic['location']['address']['sublocality'] = address.sublocality
            if address.sublocality2:
                general_dic['location']['address']['sublocality_2'] = address.sublocality2
            if address.sublocality3:
                general_dic['location']['address']['sublocality_3'] = address.sublocality3

        if odoo_location.square_location_id:
            square_location_id = odoo_location.square_location_id
        else:
            square_location_id = None

        dic = {
            'key': 'odoo',
            'type': 'location',
            'data': general_dic,
            'square_location_id': square_location_id
        }
        return dic

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
                if 'kay' in parsed_message and parsed_message['key'] != 'odoo':
                    if 'type' in parsed_message and parsed_message['type'] == 'customer':
                        dict = self._parse_general_customer_to_odoo(parsed_message['data']) #self._parse_general_dic_to_odoo(parsed_message)
                        partner_square_id = self.env['res.partner'].search([('square_id', '=', dict['square_id'])])
                        if 'reference_id' in parsed_message['data']:
                            partner_odoo_id = self.env['res.partner'].search([('id', '=', parsed_message['data']['reference_id'])])
                        else:
                            partner_odoo_id = None

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
                            response = self._parse_odoo_customer_to_general(new_customer)
                            message = json.dumps(response)
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
        modified_customers = self.env['res.partner'].search([('write_date', '>=', last_execution_date)])
        for cust in modified_customers:
            dict = self._parse_odoo_customer_to_general(cust)
            message = json.dumps(dict)
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
        channel.close()
        connection.close()

    def _get_from_queue_payments(self):

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
                    if 'type' in parsed_message and parsed_message['type'] == 'payment':
                        dict = self._parse_general_payment_to_odoo(parsed_message['data'])  # self._parse_general_dic_to_odoo(parsed_message)
                        payment_square_id = self.env['pos.payment'].search([('payment_square_id', '=', dict['payment_square_id'])])
                        if 'reference_id' in parsed_message['data']:
                            payment_odoo_id = self.env['pos.payment'].search([('id', '=', parsed_message['data']['reference_id'])])
                        else:
                            payment_odoo_id = None

                        if payment_square_id:
                            # Si lo encuentra por square_id significa que odoo ya recibio informacion de este customer de square, por lo tanto este cliente en square ya tiene en el campo reference_id la id de odoo
                            payment_square_id.update(dict)
                        elif payment_odoo_id:
                            # Si no lo encuentra por square_id pero lo encuentra por reference_id, significa que odoo creo este cliente y lo envio a square, square lo creo en su sistema y en reference_id puso la id de odoo.
                            payment_odoo_id.update(dict)
                        else:
                            # Si no encuentra por square_id ni por id de odoo significa que esta es la primera vez que odoo sabe de este cliente
                            new_payment = self.env['pos.payment'].create(dict)
                            parsed_message['data']['reference_id'] = new_customer.id
                            parsed_message['key'] = 'odoo'
                            message = json.dumps(parsed_message)
                            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
                if result[0].message_count == 0:
                    break
                result = channel.basic_get('odoo_queue', auto_ack=True)
            channel.close()
            connection.close()

    def _get_from_queue_locations(self):

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
                    if 'type' in parsed_message and parsed_message['type'] == 'location':
                        dict = self._parse_general_location_to_odoo(parsed_message['data'])
                        location_square_id = self.env['stock.warehouse'].search([('square_location_id', '=', dict['square_location_id'])])
                        if location_square_id.warehouse_count == 0:
                            location_odoo_id = self.env['stock.warehouse'].search([('name', '=', parsed_message['data']['name']),
                                                                                   ('phone_number', '=', parsed_message['data']['phone_number'])])
                        else:
                            location_odoo_id = None

                        if location_square_id.warehouse_count > 0:
                            # Si lo encuentra por square_id significa que odoo ya recibio informacion de este customer de square, por lo tanto este cliente en square ya tiene en el campo reference_id la id de odoo
                            location_square_id.update(dict)
                        elif location_odoo_id:
                            # Si no lo encuentra por square_id pero lo encuentra por reference_id, significa que odoo creo este cliente y lo envio a square, square lo creo en su sistema y en reference_id puso la id de odoo.
                            location_odoo_id.update(dict)
                        else:
                            # Si no encuentra por square_id ni por id de odoo significa que esta es la primera vez que odoo sabe de este cliente
                            new_location = self.env['stock.warehouse'].create(dict)
                            self.env.cr.commit()
                            response = self._parse_odoo_location_to_general(new_location)
                            message = json.dumps(response)
                            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
                if result[0].message_count == 0:
                    break
                result = channel.basic_get('odoo_queue', auto_ack=True)
            channel.close()
            connection.close()

    def _send_locations(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()
        tzu = timezone(self.env.user.tz)
        tz = timezone('UTC')
        last_execution_date = tz.localize(self.env['ir.cron'].browse(21).lastcall).astimezone(tzu)
        modified_locations = self.env['stock.warehouse'].search([('write_date', '>=', last_execution_date)])
        for loc in modified_locations:
            dict = self._parse_odoo_location_to_general(loc)
            message = json.dumps(dict)
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
        channel.close()
        connection.close()

    def _testing(self):
        print('sfsfs')
        self.env['stock.warehouse'].create({'name': 'Test 03',
                                            'code':'Test3' ,
                                            'square_address_id': 5,
                                            'business_email': 'test03@test.com',
                                            'phone_number': '1234567890',})
