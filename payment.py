from square.client import Client
import pika
import json
from parser import Parser

client = Client(
    access_token='EAAAEDal4hW8gV_04ryfB8ehTT0NEEZYhqKalsiTfu-GpAZPEGcxRjldU-bhGY_M',
    environment='sandbox',
)

payments_api = client.payments
result = payments_api.list_payments()

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

if result.is_success():
    message = json.dumps(result.body['payments'])
    if message != '{}':
        for i in range(len(result.body['payments'])):
            parser_dic = Parser._parse_square_to_general_payment(result.body['payments'][i])
            message = json.dumps(parser_dic)
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)

elif result.is_error():
    print(result.errors)

channel.close()
connection.close()