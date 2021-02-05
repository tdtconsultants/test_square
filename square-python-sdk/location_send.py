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


def _get_locations_created_later_than(date):
    locations = locations_api.list_locations()
    result = []
    i = 0
    while i < len(locations.body['locations']):
        if locations.body['locations'][i]['created_at'] > date:
            result.append(locations.body['locations'][i])
        i = i + 1
    return result


locations = _get_locations_created_later_than('2021-02-02T13:00:00Z')
if locations:
    message = json.dumps(locations)
    if message != '{}':
        i = 0
        while i < len(locations):
            parser_dic = Parser._parse_square_location_to_general(locations[i])
            message = json.dumps(parser_dic)
            channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
            i = i + 1

channel.close()
connection.close()