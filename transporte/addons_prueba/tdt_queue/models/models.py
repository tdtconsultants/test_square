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

        general_dic = {
            'company_name': partner.company_name if partner.company_name else None,
            'email_address': partner.email if partner.email else None,
            'nickname': partner.display_name if partner.display_name else None,
            'note': partner.comment if partner.comment else None,
            'phone_number': partner.phone if partner.phone else None,
            'reference_id': str(partner.id),
            'address': {
                'address_line_1': partner.street if partner.street else None,
                'address_line_2': partner.street2 if partner.street2 else None,
                'administrative_district_level_1': partner.state_id.code if partner.state_id else None,
                'country': partner.country_id.code if partner.country_id.code else None,
                'locality': partner.city if partner.city else None,
                'postal_code': partner.zip if partner.zip else None,
            }
        }
        names = partner.name.split()
        i = 0
        general_dic['family_name'] = ''
        while i < len(names):
            if i == 0:
                general_dic['given_name'] = names[i]
            else:
                general_dic['family_name'] = str(general_dic['family_name']) + ' ' + names[i]
            i = i + 1

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

        odoo_dic = {
            'street': general_dic['address']['address_line_1'] if 'address_line_1' in general_dic['address'] else None,
            'street2': general_dic['address']['address_line_2'] if 'address_line_2' in general_dic['address'] else None,
            'city': general_dic['address']['locality'] if 'locality' in general_dic['address'] else None,
            'zip': general_dic['address']['postal_code'] if 'postal_code' in general_dic['address'] else None,
            'company_name': general_dic['company_name'] if 'company_name' in general_dic else None,
            'email': general_dic['email_address'] if 'email_address' in general_dic else None,
            'name': general_dic['given_name'] + ' ' + general_dic['family_name'],
            'display_name': general_dic['nickname'] if 'nickname' in general_dic else None,
            'comment': general_dic['note'] if 'note' in general_dic else None,
            'phone': general_dic['phone_number'] if 'phone_number' in general_dic else None,
            'square_id': general_dic['id']
        }
        if 'country' in general_dic['address']:
            country_code = general_dic['address']['country']
            country_res = self.env['res.country'].search([('code', '=', country_code)])
            if country_res:
                odoo_dic['country_id'] = country_res.id
        if 'administrative_district_level_1' in general_dic['address']:
            country_code = general_dic['address']['country']
            state_code = general_dic['address']['administrative_district_level_1']
            state_res = self.env['res.country.state'].search([('code', '=', state_code), ('country_id', '=', country_code)])
            if state_res:
                odoo_dic['state_id'] = state_res.id

        return odoo_dic

    def _parse_general_payment_to_odoo(self, general_payment):
        odoo_payment = {
            'payment_square_id': general_payment['id'],
            'amount': general_payment['amount_money']['amount'] if 'amount_money' in general_payment else None,
            'currency_id': self.env['res.currency'].search([('name', '=', general_payment['amount_money']['currency'])]).id if 'amount' in general_payment else None,
            'tip_amount': general_payment['tip_money']['amount'] if 'tip_money' in general_payment else None,
            'tip_currency_id' : 'asdf'
        }

        # if 'amount_money' in general_payment:
        #     odoo_payment['amount'] = general_payment['amount_money']['amount']
        #     currency = self.env['res.currency'].search([('name', '=', general_payment['amount_money']['currency'])])
        #     odoo_payment['currency_id'] = currency.id
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
        pass

    def _parse_general_location_to_odoo(self,general_location):
        odoo_location = {
            'name': general_location['name'] if 'name' in general_location else '',
            'code': general_location['name'] if 'name' in general_location else '',
            'timezone': general_location['timezone'] if 'timezone' in general_location else None,
            'square_location_id': general_location['id'],
            'status': general_location['status'] if 'status' in general_location else None,
            'language_code': general_location['language_code'] if 'language_code' in general_location else None,
            'currency_id': self.env['res.currency'].search([('name', '=', general_location['currency'])], limit = 1).id if 'currency' in general_location else None,
            'phone_number': general_location['phone_number']  if 'phone_number' in general_location else None,
            'business_name': general_location['business_name'] if 'business_name' in general_location else None,
            'twitter_username': general_location['twitter_username'] if 'twitter_username' in general_location else None,
            'instagram_username': general_location['instagram_username'] if 'instagram_username' in general_location else None,
            'facebook_url': general_location['facebook_url'] if 'facebook_url' in general_location else None,
            'mcc': general_location['mcc'] if 'mcc' in general_location else None,
            'description': general_location['description'] if 'description' in general_location else None,
            'square_warehouse': True,
        }
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

        return odoo_location

    def _parse_odoo_location_to_general(self, odoo_location):

        if odoo_location.square_address_id:
            address = self.env['square.address'].browse(odoo_location.square_address_id.id)
        else:
            address = False

        general_dic = {
            'location': {
                'business_email': odoo_location.business_email if odoo_location.business_email else None,
                'business_name': odoo_location.business_name if odoo_location.business_name else None,
                'description': odoo_location.description if odoo_location.description else None,
                'facebook_url': odoo_location.facebook_url if odoo_location.facebook_url else None,
                'instagram_username': odoo_location.instagram_username if odoo_location.instagram_username else None,
                'language_code': odoo_location.language_code if odoo_location.language_code else None,
                'mcc': odoo_location.mcc if odoo_location.mcc else None,
                'name': odoo_location.name if odoo_location.name else None,
                'phone_number': odoo_location.phone_number if odoo_location.phone_number else None,
                'status': odoo_location.status if odoo_location.status else None,
                'timezone': odoo_location.timezone if odoo_location.timezone else None,
                'twitter_username': odoo_location.twitter_username if odoo_location.twitter_username else None,
                'type': odoo_location.type if odoo_location.type else None,
                'website_url': odoo_location.website_url if odoo_location.website_url else None,
                'address': {
                    'address_line_1': address.address_line_1 if address.address_line_1 else None,
                    'address_line_2': address.address_line_2 if address.address_line_2 else None,
                    'address_line_3': address.address_line_3 if address.address_line_3 else None,
                    'administrative_district_level_1': address.administrative_district_level_1 if address.administrative_district_level_1 else None,
                    'administrative_district_level_2': address.administrative_district_level_2 if address.administrative_district_level_2 else None,
                    'administrative_district_level_3': address.administrative_district_level_3 if address.administrative_district_level_3 else None,
                    'country': address.country if address.country else None,
                    'first_name': address.first_name if address.first_name else None,
                    'last_name': address.last_name if address.last_name else None,
                    'locality': address.locality if address.locality else None,
                    'organization': address.organization if address.organization else None,
                    'postal_code': address.postal_code if address.postal_code else None,
                    'sublocality': address.sublocality if address.sublocality else None,
                    'sublocality_2': address.sublocality2 if address.sublocality2 else None,
                    'sublocality_3': address.sublocality3 if address.sublocality3 else None,
                } if address else None,
            }
        }

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

    def _parse_general_order_to_odoo(self, general_order):

        state = None
        if 'state' in general_order:
            if general_order['state'] == 'OPEN':
                state = 'draft'
            if general_order['state'] == 'COMPLETED':
                state = 'done'
            if general_order['state'] == 'CANCELED':
                state = 'cancel'


        odoo_order_dict = {
            'state': state,
            'square_location_id': general_order['location_id'],
            'square_order_id': general_order['id'],
            'lines': [],
            'session_id': self.env['pos.session'].search([('state', '=', 'opened')], limit = 1).id,
            'amount_tax': general_order['total_tax_money']['amount'] / 100,
            'amount_total': general_order['total_money']['amount'] / 100,
            'amount_paid': 0,
            'amount_return': 0,
        }
        if 'line_items' in general_order:
            for line in general_order['line_items']:
                discount_percentage = 0
                if line['gross_sales_money']['amount'] != 0:
                    discount_percentage = (line['total_discount_money']['amount'] * 100) / line['gross_sales_money']['amount']
                new_order_line = {
                    'square_catalog_object_id': line['catalog_object_id'] if 'catalog_object_id' in line else None,
                    'product_id' : 119, #self.env['product.product'].search([('square_item_id', '=', line['catalog_object_id'])]).id if 'catalog_object_id' in line else 1,
                    'name': line['name'] if 'name' in line else None,
                    'qty': line['quantity'],
                    'discount': discount_percentage,
                    'price_subtotal': line['gross_sales_money']['amount'] / 100,
                    'price_subtotal_incl': line['gross_sales_money']['amount'] / 100,

                }
                odoo_order_dict['lines'].append((0,0,new_order_line))

        return odoo_order_dict

    def _parse_general_item_to_odoo(self, general_item):

        odoo_item_dict = {
            'name': general_item['item_data']['name'],
            'square_item_id': general_item['id'],
            'list_price': 0,
            'description': general_item['description'] if 'description' in general_item else None,
        }
        if 'category_id' in general_item['item_data']:
            odoo_item_dict['categ_id'] = self.env['product.category'].search([('square_category_id', '=', general_item['item_data']['category_id'])], limit = 1).id
        else:
            empty_categ = self.env['product.category'].search([('name', '=', 'NO CATEGORY')])
            if not empty_categ.id:
                empty_categ = self.env['product.category'].create({'name': 'NO CATEGORY'})
            odoo_item_dict['categ_id'] = empty_categ.id

        return odoo_item_dict

    def _parse_general_category_to_odoo(self, general_category):
        odoo_category = {
            'square_category_id': general_category['id'],
            'name': general_category['category_data']['name']
        }
        return odoo_category

    def _parse_general_item_variation_to_odoo(self, item_variation):
        odoo_item_variation = {
            'square_item_id': item_variation['id'],
            'is_product_variant': True,
            'name': item_variation['item_variation_data']['name'],
            'list_price': item_variation['item_variation_data']['price_money']['amount'],
            'currency_id': self.env['res.currency'].search([('name', '=', item_variation['item_variation_data']['price_money']['currency'])], limit = 1).id,
            'product_variant_id': self.env['product.product'].search([('square_item_id', '=', item_variation['item_variation_data']['item_id'])]).id
        }
        return odoo_item_variation

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
        modified_customers = self.env['res.partner'].search([('create_date', '>=', '2021-02-02 13:36:45.990092')])
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

    def _get_from_queue_orders(self):

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
                    if 'type' in parsed_message and parsed_message['type'] == 'order':
                        order_square_id = self.env['pos.order'].search([('square_order_id', '=', parsed_message['data']['id'])])
                        dict = self._parse_general_order_to_odoo(parsed_message['data'])
                        if order_square_id:
                            order_square_id.update(dict)
                        else:
                            new_location = self.env['pos.order'].create(dict)
                            self.env.cr.commit()
                if result[0].message_count == 0:
                    break
                result = channel.basic_get('odoo_queue', auto_ack=True)
            channel.close()
            connection.close()

    def _get_from_queue_items(self):

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

                    if 'type' in parsed_message and parsed_message['type'] == 'item':
                        dict = self._parse_general_item_to_odoo(parsed_message['data'])
                        item_square_id = self.env['product.product'].search([('square_item_id', '=', dict['square_item_id'])])
                        parent_name = parsed_message['data']['item_data']['name']
                        if item_square_id:
                            item_square_id.update(dict)
                        else:
                            item_square_id = self.env['product.product'].create(dict)

                        for variation in parsed_message['data']['item_data']['variations']:
                            variation_in_odoo = self.env['product.product'].search([('square_item_id', '=', variation['id'])])
                            variation_dict = self._parse_general_item_variation_to_odoo(variation)
                            if variation_in_odoo:
                                variation_in_odoo.update(variation_dict)
                            else:
                                if variation_dict['name'] != 'Regular111':
                                    variation_in_odoo = self.env['product.product'].create(variation_dict)
                                    variation_in_odoo.write({'combination_indices': parent_name + '_' + variation_in_odoo.name})
                                    item_square_id.write({
                                            'product_variant_ids': [(4, variation_in_odoo.id, 0)],
                                        })
                                else:
                                    item_square_id.write({'list_price': variation_dict['list_price'], 'currency_id': variation_dict['currency_id'], 'square_item_id': variation_dict['square_item_id']})

                    if 'type' in parsed_message and parsed_message['type'] == 'category':
                        dict = self._parse_general_category_to_odoo(parsed_message['data'])
                        category_square_id = self.env['product.category'].search([('square_category_id', '=', dict['square_category_id'])])
                        if category_square_id:
                            category_square_id.update(dict)
                        else:
                            new_category = self.env['product.category'].create(dict)

                if result[0].message_count == 0:
                    break
                result = channel.basic_get('odoo_queue', auto_ack=True)
            channel.close()
            connection.close()

    def _testing(self):
        self.env['res.partner'].create({
            'street': 'Av siempre viva',
            'street2': 'elm st',
            'city': 'Montevideo',
            'zip': '11200',
            'company_name': 'AN orgAnization',
            'email': 'myemail@testing.com',
            'name': 'F Mangold',
            'display_name': 'Fernando',
            'comment': 'This is my coment, hope it works!',
            'phone': '1234567890',
            'country_id': 233,
            'state_id': 13,
        })
        self.env['stock.warehouse'].create({'name': 'Test9',
                                            'code':'Test9' ,
                                            'square_address_id': 2,
                                            'business_email': 'test5@test.com',
                                            'phone_number': '9999999999',
                                            'twitter_username': 'username',
                                            'square_warehouse': True,})

        # self.env['account.account'].create({
        #     'name': 'account1',
        #     'code': 'acc1',
        #     'user_type_id': 3
        #
        # })
        # self.env['pos.payment.method'].create({
        #     'name': 'Efectivo1',
        #     'receivable_account_id': 5
        # })

