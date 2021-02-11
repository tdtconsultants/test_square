from square.client import Client
import pika
import json
from parser import Parser

client = Client(
    access_token='EAAAEDal4hW8gV_04ryfB8ehTT0NEEZYhqKalsiTfu-GpAZPEGcxRjldU-bhGY_M',
    environment='sandbox',
)

# catalog_api = client.catalog
# inventory_api = client.inventory
#
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
#
# items = catalog_api.list_catalog('','ITEM')
# catalog_objet_ids = []
# for i in range(len(items.body['objects'])):
#     for j in range(len(items.body['objects'][i]['item_data']['variations'])):
#         catalog_objet_ids.append(items.body['objects'][i]['item_data']['variations'][j]['id'])
#
# body = {
#     'catalog_object_ids': catalog_objet_ids
# }
# inventory = inventory_api.batch_retrieve_inventory_changes(body)
#
# for i in range(len(inventory.body['counts'])):
#     parser_dic = Parser._parse_inventory_to_general(inventory.body['counts'][i])
#     message = json.dumps(parser_dic)
#     channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
#
# channel.close()
# connection.close()

location_api = client.locations
inventory_api = client.inventory

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

locations = location_api.list_locations()
locations_ids = []
for i in range(len(locations.body['locations'])):
    locations_ids.append(locations.body['locations'][i]['id'])

body = {
    'location_ids': locations_ids
}
inventory = inventory_api.batch_retrieve_inventory_changes(body)

for i in range(len(inventory.body['changes'])):
    parser_dic = Parser._parse_inventory_to_general(inventory.body['changes'][i]['adjustment'])
    message = json.dumps(parser_dic)
    channel.basic_publish(exchange='master_exchange', routing_key='', body=message)

channel.close()
connection.close()