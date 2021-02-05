# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.product'

    square_item_id = fields.Char(string="id from square")
