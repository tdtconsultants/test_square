# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Category(models.Model):
    _inherit = 'product.category'

    square_category_id = fields.Char(string="id from square")
