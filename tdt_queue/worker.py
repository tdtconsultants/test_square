import pika, sys, os, time

def main():

    connections = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connections.channel()
    channel.queue_declare(queue='task_queue', durable=True)

    def callback(ch, method, properties, body):
        print(" [x] Receive %r" % body.decode())
        time.sleep(body.count(b'.'))
        print("[x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)
    print("[*] Waiting for message. To exit press CTRL+C")

    channel.start_consuming()
