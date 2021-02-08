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
                    dict = self._parse_general_customer_to_odoo(parsed_message['data'])  # self._parse_general_dic_to_odoo(parsed_message)
                    partner_square_id = self.env['res.partner'].search([('square_id', '=', dict['square_id'])])
                    if 'reference_id' in parsed_message['data']:
                        partner_odoo_id = self.env['res.partner'].search([('id', '=', parsed_message['data']['reference_id'])])
                    else:
                        partner_odoo_id = None

                    if partner_square_id:
                        # Si lo encuentra por square_id significa que odoo ya recibio informacion de este customer de square, por lo tanto este cliente en square ya tiene en el campo reference_id la id de odoo
                        partner_square_id.update(dict)
                    elif partner_odoo_id:
                        # Si no lo encuentra por square_id pero lo encuentra por reference_id, significa que odoo creo este cliente y lo envio a square, square lo creo en su sistema y en reference_id puso la id de odoo.
                        # Lo que hay que hacer es agregar la referencia en square_id
                        # Pueden haber mas cambios ademas del square id
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
                                item_square_id.write({'list_price': variation_dict['list_price'], 'currency_id': variation_dict['currency_id'],
                                                      'square_item_id': variation_dict['square_item_id']})

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
