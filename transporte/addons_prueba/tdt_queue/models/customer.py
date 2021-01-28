# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    square_id = fields.Char(string="id from square")
    birthday = fields.Char(string="birthday")
    street3 = fields.Char(string="Street 3")
    administrative_district_level_1 = fields.Char(string="administrative_district_level_1")
    administrative_district_level_2 = fields.Char(string="administrative_district_level_2")
    administrative_district_level_3 = fields.Char(string="administrative_district_level_3")
    organization = fields.Char(string="organization")
    sublocality = fields.Char(stirng="sublocality")
    sublocality2 = fields.Char(stirng="sublocality2")
    sublocality3 = fields.Char(stirng="sublocality3")
    note = fields.Char(string="note")
    family_name = fields.Char(string="family name")
    given_name = fields.Char(string="given name")

