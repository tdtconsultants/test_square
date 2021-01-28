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

locations_api = client.locations
result = locations_api.list_locations()
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

if result.is_success():
    message = json.dumps(result.body['locations'])
    if message != '{}':
        for i in range(len(result.body['locations'])):
            parser_dic = Parser._parse_square_location_to_general(result.body['locations'][i])
            message = json.dumps(parser_dic)
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)

elif result.is_error():
    print(result.errors)

channel.close()
connection.close()