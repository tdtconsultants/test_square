from square.client import Client
import pika
import json
from parser import Parser

client = Client(
    access_token='EAAAEDal4hW8gV_04ryfB8ehTT0NEEZYhqKalsiTfu-GpAZPEGcxRjldU-bhGY_M',
    environment='sandbox',
)

catalog_api = client.catalog
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

result = catalog_api.list_catalog('','CATEGORY')
i = 0
while i < len(result.body['objects']):
    parser_dic = Parser._parse_square_category_to_general((result.body['objects'][i]))
    message = json.dumps(parser_dic)
    channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
    i = i + 1

result = catalog_api.list_catalog('','ITEM')
i = 0
while i < len(result.body['objects']):
    parser_dic = Parser._parse_square_item_to_general((result.body['objects'][i]))
    message = json.dumps(parser_dic)
    channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
    i = i + 1

channel.close()
connection.close()
