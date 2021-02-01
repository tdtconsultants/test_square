# -*- coding: utf-8 -*-
from odoo import models, fields


class FulfillmentsShipment(models.Model):

    _name = "fulfillments.shipment"

    cancel_reason = fields.Char()
    canceled_at = fields.Char()
    carrier = fields.Char()
    expected_shipped_at = fields.Char()
    failure_reason = fields.Char()
    recipient = fields.Many2one(comodel_name="filfillment.recipient")
    shipping_note = fields.Char()
    shipping_type = fields.Char()
    tracking_number = fields.Char()
    tracking_url = fields.Char()
