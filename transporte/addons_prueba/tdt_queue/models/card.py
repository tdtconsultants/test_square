# -*- coding: utf-8 -*-
from odoo import models, fields


class CardDetails(models.Model):
    _name = "CardDetails"

    card_brand = fields.Char(string="card_brand")
    last_4 = fields.Char(string="last_4")
    exp_month = fields.Integer(string="exp_month")
    exp_year = fields.Integer(string="exp_year")
    fingerprint = fields.Char(string="fingerprint")
    card_type = fields.Char(string="card_type")
    prepaid_type = fields.Char(string="prepaid_type")
    bin = fields.Char(string="bin")
