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

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

locations = location_api.list_locations()
locations_ids = []
for i in range(len(locations.body['locations'])):
    locations_ids.append(locations.body['locations'][i]['id'])

body = {
    'location_ids': locations_ids
}

inventory = inventory_api.batch_retrieve_inventory_counts(body)
parser_dic = Parser._parse_inventory_count_to_general(inventory.body['counts'])
message = json.dumps(parser_dic)
channel.basic_publish(exchange='master_exchange', routing_key='', body=message)

channel.close()
connection.close()