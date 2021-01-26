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

if result.is_success():
    message = json.dumps(result.body['customers'])
    if message != '{}':
        for i in range(len(result.body['customers'])):
            parser_dic = Parser._parse_square_to_general(result.body['customers'][i])
            message = json.dumps(parser_dic)
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)

elif result.is_error():
    print(result.errors)

channel.close()
connection.close()