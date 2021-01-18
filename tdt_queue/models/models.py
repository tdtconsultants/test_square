# -*- coding: utf-8 -*-
from odoo import models, fields, api
from queue import Queue
import pika
import sys
import threading


class TdtQueue(models.Model):
    _name = "tdt_queue"

    name = fields.Char(string="Customer")
    type_jobs = fields.Char(string="Tipo de jobs")

    def _active_cron_task(self):

        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel_cron = connection.channel()

        severities = sys.argv[1:]

        for severity in severities:
            channel_cron.queue_bind(queue='task_queue', exchange='my_exchange', routing_key=severity)

        result = channel_cron.basic_get('task_queue', auto_ack=True)

        if None in result:
            channel_cron.close()
            connection.close()
        else:
            while result[0].message_count >= 0:
                self.create({
                    'name': "lolo",
                    'type_jobs': result[2]
                })
                if result[0].message_count == 0:
                    break
                result = channel_cron.basic_get('task_queue', auto_ack=True)
            channel_cron.close()
            connection.close()



