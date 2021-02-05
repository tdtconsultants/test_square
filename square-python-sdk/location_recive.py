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
                if location_square_id.is_success():
                    #Square creo esta location y odoo responde
                    update_result = locations_api.update_location(location_square_id.body['location']['id'], square_dic)
                    if update_result.is_success():
                        print(update_result.body)
                    else:
                        print(update_result.errors)
                else:
                    #Crea una nueva location
                    create_result = locations_api.create_location(square_dic)
                    if create_result.is_success():
                        print(create_result.body)
                        response = Parser._parse_square_location_to_general(create_result.body['location'])
                        message = json.dumps(response)
                        channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
                    elif create_result.is_error():
                        print(create_result.errors)
        if result[0].message_count == 0:
            break
        result = channel.basic_get('square_queue', auto_ack=True)
    channel.close()
    connection.close()
