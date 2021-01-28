from square.client import Client
import pika
import json

from parser import Parser




client = Client(
    access_token='EAAAEDal4hW8gV_04ryfB8ehTT0NEEZYhqKalsiTfu-GpAZPEGcxRjldU-bhGY_M',
    environment='sandbox',
)

locations_api = client.locations
result = locations_api.list_locations()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


def _find_location_by_description(descriprion):
    locations = locations_api.list_locations()
    found = False
    i = 0
    location = 'Not found'
    while not found and i < range(len(locations.body['location'])):
        if 'description' in locations.body['locations'][i] and locations.body['locations'][i] == descriprion:
            found = True
            location = locations.body['locations'][i]
        else:
            i = i + 1
    return location


result = channel.basic_get('square_queue', auto_ack=True)
if None in result:
    channel.close()
    connection.close()
else:
    while result[0].message_count >= 0:
        general_dic = json.loads(result[2])
        if 'key' in general_dic and general_dic['key'] != 'square':
            if 'type' in general_dic and general_dic['type'] == 'location':
                square_dic = general_dic['data']

                if general_dic['square_location_id'] is None:
                    square_location_id = 'this is not an id'
                else:
                    square_location_id = general_dic['square_location_id']

                location_square_id = locations_api.retrieve_location(square_location_id)
                location_odoo_id = _find_location_by_description(str(square_dic['description']))

                if location_odoo_id is not 'Not found':
                    #Si lo encuentra por odoo_id significa que square ya recibio informaicon de este cliente, por lo tanto lo actualiza
                    update_result = locations_api.update_customer(location_odoo_id.body['customers'][0]['id'], square_dic)
                    if update_result.is_success():
                        print(update_result.body)
                    else:
                        print(update_result.errors)
                elif location_square_id.is_success():
                    #Si no lo encuetra por odoo_id pero si por square_id significa que square creo este cliente y lo envio a odoo, odoo lo creeo en su sistema y
                    #mando un mensaje para que square actualize el valor odoo_id
                    update_result = locations_api.update_customer(location_square_id.body['customer']['id'], square_dic)
                    if update_result.is_success():
                        print(update_result.body)
                    else:
                        print(update_result.errors)
                else:
                    #Si no lo encuentra por square_id ni por odoo_id significa que es un cliente nuevo de odoo
                    #Luego envia a odoo un mensaje para que este acutalize su campo square id
                    create_result = locations_api.create_customer(square_dic)
                    if create_result.is_success():
                        print(create_result.body)
                        response = Parser._parse_square_to_general(create_result.body['customer'])
                        message = json.dumps(response)
                        channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
                    elif create_result.is_error():
                        print(create_result.errors)
        if result[0].message_count == 0:
            break
        result = channel.basic_get('square_queue', auto_ack=True)
    channel.close()
    connection.close()
