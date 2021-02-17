from square.client import Client
import pika
import json
from parser import Parser

client = Client(
    access_token='EAAAEDal4hW8gV_04ryfB8ehTT0NEEZYhqKalsiTfu-GpAZPEGcxRjldU-bhGY_M',
    environment='sandbox',
)

location_api = client.locations
inventory_api = client.inventory
catalog_api = client.catalog

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

items = catalog_api.list_catalog('', 'ITEM_VARIATION')
inventory_adjustments = []
for i in range(len(items.body['objects'])):
    item_changes = inventory_api.retrieve_inventory_changes(items.body['objects'][i]['id'])
    if 'changes' in item_changes.body:
        inventory_adjustments.append(item_changes.body['changes'])

parser_dic = Parser._parse_inventory_to_general(inventory_adjustments)
message = json.dumps(parser_dic)
channel.basic_publish(exchange='master_exchange', routing_key='', body=message)

channel.close()
connection.close()