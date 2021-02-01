# -*- coding: utf-8 -*-
from odoo import models, fields


class Fulfillments(models.Model):

    _name = "fulfillments"

    metadata = fields.One2many(comodel_name="metadata", string="metadata")
    recipient = fields.Many2one(comodel_name="fulfillment.pickup")
    shipment_details = fields.Many2one(comodel_name="fulfillment.shipment")
    state = fields.Selection([('proposed', 'PROPOSED'), ('reserved', 'RESERVED'), ('prepared', 'PREPARED'), ('completed', 'COMPLETED'), ('canceled', 'CANCELED')
                                ,('failed', 'FAILED')])
    type = fields.Selection([('pickup', 'PICKUP'), ('shipment', 'SHIPMENT')])
    udi = fields.Char(string="id of the fulfillment within the order")
