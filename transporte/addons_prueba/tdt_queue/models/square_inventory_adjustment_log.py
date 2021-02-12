# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SquareInvLogs(models.Model):
    _name = "square_inventory_logs"
    
    square_inventory_adjustment_id = fields.Char(string="inventory adjustment id form square")
