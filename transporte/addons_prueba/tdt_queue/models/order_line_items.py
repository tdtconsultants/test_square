# -*- coding: utf-8 -*-
from odoo import models, fields


class OrderLineItems(models.Model):

    _inherit = 'pos.order.line'

    square_catalog_object_id = fields.Char(string="id item square")

