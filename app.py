from square.client import Client
import pika
import json

from parser import Parser


def _parse_square_to_general_dic(square_dic):
    if 'given_name' in square_dic:
        first_name = square_dic['given_name']
    else:
        first_name = None

    if 'family_name' in square_dic:
        last_name = square_dic['family_name']
    else:
        last_name = None

    if 'id' in square_dic:
        square_id = square_dic['id']
    else:
        square_id = None

    if 'reference_id' in square_dic:
        odoo_id = square_dic['reference_id']
    else:
        odoo_id = None

    if 'nickname' in square_dic:
        nickname = square_dic['nickname']
    else:
        nickname = None

    if 'email_address' in square_dic:
        email_address = square_dic['email_address']
    else:
        email_address = None

    if 'phone_number' in square_dic:
        phone_number = square_dic['phone_number']
    else:
        phone_number = None

    if 'note' in square_dic:
        note = square_dic['note']
    else:
        note = None

    if 'company_name' in square_dic:
        company_name = square_dic['company_name']
    else:
        company_name = None

    if 'address' in square_dic:

        if 'address_line_1' in square_dic['address']:
            address_line_1 = square_dic['address']['address_line_1']
        else:
            address_line_1 = None

        if 'address_line_2' in square_dic['address']:
            address_line_2 = square_dic['address']['address_line_2']
        else:
            address_line_2 = None

        if 'locality' in square_dic['address']:
            locality = square_dic['address']['locality']
        else:
            locality = None

        if 'administrative_district_level_1' in square_dic['address']:
            administrative_district_level_1 = square_dic['address']['administrative_district_level_1']
        else:
            administrative_district_level_1 = None

        if 'postal_code' in square_dic['address']:
            postal_code = square_dic['address']['postal_code']
        else:
            postal_code = None

        if 'country' in square_dic['address']:
            country = square_dic['address']['country']
        else:
            country = None

    general_dic = {
        'first_name': first_name,
        'last_name': last_name,
        'square_id': square_id,
        'odoo_id': odoo_id,
        'nickname': nickname,
        'email_address': email_address,
        'phone_number': phone_number,
        'note': note,
        'company_name': company_name,
        'key': 'square',
    }
    if 'address' in square_dic:
        general_dic['address']: {'address_line_1': address_line_1, 'address_line_2': address_line_2, 'locality': locality, 'administrative_district_level_1': administrative_district_level_1,
                    'postal_code': postal_code, 'country': country}
    else:
        general_dic['address']: {}
    return general_dic


def _parse_general_dic_to_square(general_dic):
    new_customer = general_dic

    if 'note' in new_customer:
        note = new_customer['note']
    else:
        note = None

    if 'odoo_id' in new_customer and new_customer['odoo_id'] is not None:
        reference_id = new_customer['odoo_id']
    else:
        reference_id = '999999'

    if 'square_id' in new_customer:
        square_id = new_customer['square_id']
    else:
        square_id = 'none'

    if 'company_name' in new_customer:
        company_name = new_customer['company_name']
    else:
        company_name = None

    if 'nickname' in new_customer:
        nickname = new_customer['nickname']
    else:
        nickname = None

    if 'email_address' in new_customer:
        email_address = new_customer['email_address']
    else:
        email_address = None

    if 'phone_number' in new_customer:
        phone_number = new_customer['phone_number']
    else:
        phone_number = None

    if 'address' in new_customer:

        if 'postal_code' in new_customer['address']:
            postal_code = new_customer['address']['postal_code']
        else:
            postal_code = None

        if 'country' in new_customer['address']:
            country = new_customer['address']['country']
        else:
            country = None

        if 'administrative_district_level_1' in new_customer['address']:
            administrative_district_level_1 = new_customer['address']['administrative_district_level_1']
        else:
            administrative_district_level_1 = None

        if 'locality' in new_customer['address']:
            locality = new_customer['address']['locality']
        else:
            locality = None

        if 'address_line_1' in new_customer['address']:
            address_line_1 = new_customer['address']['address_line_1']
        else:
            address_line_1 = None

        if 'address_line_2' in new_customer['address']:
            address_line_2 = new_customer['address']['address_line_2']
        else:
            address_line_2 = None

    parsed_dict = {
        'given_name': new_customer['first_name'],
        'family_name': new_customer['last_name'],
        'company_name': company_name,
        'display_name': nickname,
        'email_address': email_address,
        'phone_number': phone_number,
        'reference_id': str(reference_id),
        'note': note,
    }
    if 'address' in new_customer:
        parsed_dict['address']: {'address_line_1': address_line_1, 'address_line_2': address_line_2, 'administrative_district_level_1': administrative_district_level_1, 'country': country,
                    'locality': locality, 'postal_code': postal_code}
    return parsed_dict


client = Client(
    access_token='EAAAEDal4hW8gV_04ryfB8ehTT0NEEZYhqKalsiTfu-GpAZPEGcxRjldU-bhGY_M',
    environment='sandbox',
)

body = {}
body['limit'] = 2
body['query'] = {}
body['query']['filter'] = {}
body['query']['filter']['created_at'] = {}
body['query']['filter']['created_at']['start_at'] = '2021-01-21T00:00:00-00:00'

customer_api = client.customers
result = customer_api.list_customers()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
#
# if result.is_success():
#     message = json.dumps(result.body['customers'])
#     if message != '{}':
#         for i in range(len(result.body['customers'])):
#             parser_dic = Parser._parse_square_to_general(result.body['customers'][i]) #_parse_square_to_general_dic(result.body['customers'][i])
#             message = json.dumps(parser_dic)
#             channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
#
# elif result.is_error():
#     print(result.errors)
#
# channel.close()
# connection.close()


#read form queue and do something if it is not my message
result = channel.basic_get('square_queue', auto_ack=True)
if None in result:
    channel.close()
    connection.close()
else:
    while result[0].message_count >= 0:
        general_dic = json.loads(result[2])
        if 'key' in general_dic and general_dic['key'] != 'square':
            square_dic = Parser._parse_general_to_square(general_dic)

            if general_dic['square_id'] is None:
                square_id = 'this is not an id'
            else:
                square_id = general_dic['square_id']

            partner_square_id = customer_api.retrieve_customer(square_id)

            body = {}
            body['query'] = {}
            body['query']['filter'] = {}
            body['query']['filter']['reference_id'] = {}
            body['query']['filter']['reference_id']['exact'] = square_dic['reference_id']

            partner_odoo_id = customer_api.search_customers(body)

            if partner_odoo_id.is_success() and partner_odoo_id.body != {}:
                #Si lo encuentra por odoo_id significa que square ya recibio informaicon de este cliente, por lo tanto lo actualiza
                update_result = customer_api.update_customer(partner_odoo_id.body['customers'][0]['id'], square_dic)
                if update_result.is_success():
                    print(update_result.body)
                else:
                    print(update_result.errors)
            elif partner_square_id.is_success():
                #Si no lo encuetra por odoo_id pero si por square_id significa que square creo este cliente y lo envio a odoo, odoo lo creeo en su sistema y
                #mando un mensaje para que square actualize el valor odoo_id
                update_result = customer_api.update_customer(partner_square_id.body['customer']['id'], square_dic)
                if update_result.is_success():
                    print(update_result.body)
                else:
                    print(update_result.errors)
            else:
                #Si no lo encuentra por square_id ni por odoo_id significa que es un cliente nuevo de odoo
                #Luego envia a odoo un mensaje para que este acutalize su campo square id
                create_result = customer_api.create_customer(square_dic)
                if create_result.is_success():
                    print(create_result.body)
                    general_dic['square_id'] = create_result.body['customer']['id']
                    general_dic['key'] = 'square'
                    message = json.dumps(general_dic)
                    channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
                elif create_result.is_error():
                    print(create_result.errors)
        if result[0].message_count == 0:
            break
        result = channel.basic_get('square_queue', auto_ack=True)
    channel.close()
    connection.close()


# result = customer_api.list_customers()
# if result.is_success():
#     for i in range(len(result.body['customers'])):
#         delete = customer_api.delete_customer(result.body['customers'][i]['id'])
#         if delete.is_success():
#             print('Delete')
#         else:
#             print(delete.errors)
# elif result.is_error():
#     print(result.errors)


