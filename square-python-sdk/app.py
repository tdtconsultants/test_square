from square.client import Client
import pika
import json

from parser import Parser

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
#             parser_dic = Parser._parse_square_to_general(result.body['customers'][i])
#             message = json.dumps(parser_dic)
#             channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
#
# elif result.is_error():
#     print(result.errors)
#
# channel.close()
# connection.close()


#read form queue and do something if it is not my message
# result = channel.basic_get('square_queue', auto_ack=True)
# if None in result:
#     channel.close()
#     connection.close()
# else:
#     while result[0].message_count >= 0:
#         general_dic = json.loads(result[2])
#         if 'key' in general_dic and general_dic['key'] != 'square':
#             square_dic = Parser._parse_general_to_square(general_dic)
#
#             if general_dic['square_id'] is None:
#                 square_id = 'this is not an id'
#             else:
#                 square_id = general_dic['square_id']
#
#             partner_square_id = customer_api.retrieve_customer(square_id)
#
#             body = {}
#             body['query'] = {}
#             body['query']['filter'] = {}
#             body['query']['filter']['reference_id'] = {}
#             body['query']['filter']['reference_id']['exact'] = square_dic['reference_id']
#
#             partner_odoo_id = customer_api.search_customers(body)
#
#             if partner_odoo_id.is_success() and partner_odoo_id.body != {}:
#                 #Si lo encuentra por odoo_id significa que square ya recibio informaicon de este cliente, por lo tanto lo actualiza
#                 update_result = customer_api.update_customer(partner_odoo_id.body['customers'][0]['id'], square_dic)
#                 if update_result.is_success():
#                     print(update_result.body)
#                 else:
#                     print(update_result.errors)
#             elif partner_square_id.is_success():
#                 #Si no lo encuetra por odoo_id pero si por square_id significa que square creo este cliente y lo envio a odoo, odoo lo creeo en su sistema y
#                 #mando un mensaje para que square actualize el valor odoo_id
#                 update_result = customer_api.update_customer(partner_square_id.body['customer']['id'], square_dic)
#                 if update_result.is_success():
#                     print(update_result.body)
#                 else:
#                     print(update_result.errors)
#             else:
#                 #Si no lo encuentra por square_id ni por odoo_id significa que es un cliente nuevo de odoo
#                 #Luego envia a odoo un mensaje para que este acutalize su campo square id
#                 create_result = customer_api.create_customer(square_dic)
#                 if create_result.is_success():
#                     print(create_result.body)
#                     general_dic['square_id'] = create_result.body['customer']['id']
#                     general_dic['key'] = 'square'
#                     message = json.dumps(general_dic)
#                     channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
#                 elif create_result.is_error():
#                     print(create_result.errors)
#         if result[0].message_count == 0:
#             break
#         result = channel.basic_get('square_queue', auto_ack=True)
#     channel.close()
#     connection.close()



#Delete all customers
result = customer_api.list_customers()
if result.is_success():
    for i in range(len(result.body['customers'])):
        delete = customer_api.delete_customer(result.body['customers'][i]['id'])
        if delete.is_success():
            print('Delete')
        else:
            print(delete.errors)
elif result.is_error():
    print(result.errors)


