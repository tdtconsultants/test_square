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

if result.is_success():
    message = json.dumps(result.body['locations'])
    if message != '{}':
        for i in range(len(result.body['locations'])):
            message = json.dumps(result.body['locations'][i])
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)

elif result.is_error():
    print(result.errors)

channel.close()
connection.close()
