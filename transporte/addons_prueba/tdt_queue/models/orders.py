# -*- coding: utf-8 -*-
from odoo import models, fields


class Orders(models.Model):
    _inherit = 'pos.order'

    square_location_id = fields.Char(string="Square location id")
    square_order_id = fields.Char()
