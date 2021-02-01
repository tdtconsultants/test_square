# -*- coding: utf-8 -*-
from odoo import models, fields


class AppliedTAxes(models.Model):

    _name = "pos.order.line.applied.taxes"

    tax_uid = fields.Char(string="id of tax within this order")
    uid = fields.Char()
