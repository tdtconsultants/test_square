# -*- coding: utf-8 -*-
from odoo import models, fields


class FulfillmentsRecipient(models.Model):

    _name = "fulfillments.recipient"

    recipient_address = fields.Many2one(comodel_name="square.address")
    square_customer_id = fields.Char()
    odoo_customer_id = fields.Integer()
    display_name = fields.Char()
    email_address = fields.Char()
    phone_number = fields.Char()

