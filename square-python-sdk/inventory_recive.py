from square.client import Client
import pika
import json
import uuid
import datetime
from parser import Parser

client = Client(
    access_token='EAAAEDal4hW8gV_04ryfB8ehTT0NEEZYhqKalsiTfu-GpAZPEGcxRjldU-bhGY_M',
    environment='sandbox',
)


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
inventory_api = client.inventory

result = channel.basic_get('square_queue', auto_ack=True)
if None in result:
    channel.close()
    connection.close()
else:
    while result[0].message_count >= 0:
        general_dic = json.loads(result[2])
        if 'key' in general_dic and general_dic['key'] != 'square':
            if 'type' in general_dic and general_dic['type'] == 'inventory':
                inventory_lines = general_dic['data']
                body = {}
                body['changes'] = []

                i = 0
                for line in inventory_lines:
                    date = datetime.datetime.utcnow()
                    occurred_at = str(date.isoformat("T")) + 'Z'
                    body['changes'].append({})
                    body['changes'][i]['type'] = 'PHYSICAL_COUNT'
                    body['changes'][i]['physical_count'] = {}
                    body['changes'][i]['physical_count']['catalog_object_id'] = {}
                    body['changes'][i]['physical_count']['catalog_object_id'] = line['catalog_object_id']
                    body['changes'][i]['physical_count']['state'] = 'IN_STOCK'
                    body['changes'][i]['physical_count']['location_id'] = line['location_id']
                    body['changes'][i]['physical_count']['quantity'] = str(line['quantity'])
                    body['changes'][i]['physical_count']['occurred_at'] = occurred_at
                    i = i + 1
                body['idempotency_key'] = str(uuid.uuid1())
                body['ignore_unchanged_counts'] = True

                adjustment = inventory_api.batch_change_inventory(body)

                if adjustment.is_success():
                    print(adjustment.body)
                elif adjustment.is_error():
                    print(adjustment.errors)
        if result[0].message_count == 0:
            break
        result = channel.basic_get('square_queue', auto_ack=True)

    channel.close()
    connection.close()
