from square.client import Client
import pika
import json
from parser import Parser

client = Client(
    access_token='EAAAEDal4hW8gV_04ryfB8ehTT0NEEZYhqKalsiTfu-GpAZPEGcxRjldU-bhGY_M',
    environment='sandbox',
)

orders_api = client.orders
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

body = {}
body['location_ids'] = ['L13D0EZRRJPQD', 'L4SN6DDDDRS2G']
orders = orders_api.search_orders(body)
parser_dic = Parser._parse_square_order_to_general(orders.body['orders'])
message = json.dumps(parser_dic)
#channel.basic_publish(exchange='master_exchange', routing_key='', body=message)

if orders:

    i = 0
    while i < len(orders.body['orders']):
        parser_dic = Parser._parse_square_order_to_general(orders.body['orders'][i])
        message = json.dumps(parser_dic)
        channel.basic_publish(exchange='master_exchange', routing_key='', body=message)
        i = i + 1

channel.close()
connection.close()
