# -*- coding: utf-8 -*-
from odoo import models, fields


class Address(models.Model):
    _name = "square.address"

    address_line_1 = fields.Char(string="address_line_1")
    address_line_2 = fields.Char(string="address_line_2")
    address_line_3 = fields.Char(string="address_line_")
    administrative_district_level_1 = fields.Char(string="administrative district level1")
    administrative_district_level_2 = fields.Char(string="administrative district level2")
    administrative_district_level_3 = fields.Char(string="administrative district level3")
    country = fields.Char(string="country")
    first_name = fields.Char(string="first_name")
    last_name = fields.Char(string="last_name")
    locality = fields.Char(string="locality")
    organization = fields.Char(string="organization")
    postal_code = fields.Char(string="postal code")
    sublocality = fields.Char(string="sublocality")
    sublocality2 = fields.Char(string="sublocality2")
    sublocality3 = fields.Char(string="sublocality3")

