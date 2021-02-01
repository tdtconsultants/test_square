# -*- coding: utf-8 -*-
from odoo import models, fields


class AppliedDiscount(models.Model):

    _name = "pos.order.line.applied.discount"

    discount_uid = fields.Char(string="uid of a discount within this order")
    uid = fields.Char()
