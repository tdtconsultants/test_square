import pika, sys

message = ' '.join(sys.argv[1:]) or "Hello Word!"

connections = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connections.channel()


channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(delivery_mode=2)
    )

print("[x] sent %r" % message)

connections.close()
