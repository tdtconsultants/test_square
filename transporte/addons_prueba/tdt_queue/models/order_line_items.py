# -*- coding: utf-8 -*-
from odoo import models, fields


class OrderLineItems(models.Model):

    _inherit = 'pos.order.line'

    applied_discounts = fields.One2many(comodel_name="pos.order.line.applied.discount")
    applied_taxes = fields.One2many(comodel_name="pos.order.line.applied.taxes")
    base_price_money_amount = fields.Integer()
    base_price_money_currency_id = fields.One2many(comodel_name="res.currency")

