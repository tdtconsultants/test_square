# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    square_id = fields.Char(string="id from square")

    #def create_patner_square(self):
