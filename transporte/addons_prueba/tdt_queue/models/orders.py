# -*- coding: utf-8 -*-
from odoo import models, fields


class Orders(models.Model):

    _inherit = 'pos.order'

    square_location_id = fields.Char(string="Square location id")
    order_line_item_discount = fields.One2many(comodel_name="line.item.discount", string="item discount lines")
    fulfillments = fields.One2many(comodel_name="fulfillments", string="fulfillments")
    metadata = fields.One2many(comodel_name="metadata", string="metadata")
    auto_apply_discounts = fields.Boolean()
    auto_apply_taxes = fields.Boolean()
    square_order_id = fields.Char()
    service_charges = fields.One2many(comodel_name="order.service.charge")
    source_name = fields.Char(string="source")
    taxes = fields.One2many(comodel_name="account.tax")
    version = fields.Integer(string="version")
