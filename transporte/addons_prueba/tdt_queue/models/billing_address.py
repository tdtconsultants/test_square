# -*- coding: utf-8 -*-
from odoo import models, fields


class BillingAddress(models.Model):
    _name = "BillingAddress"

    address_line_1 = fields.Char(string="street1")
    address_line_2 = fields.Char(string="street2")
    locality = fields.Char(string="locality")
    administrative_district_level_1 = fields.Char(string="administrative district level")
    postal_code = fields.Char(string="postal code")
    country = fields.Char(string="country")
    first_name = fields.Char(string="first name")
    last_name = fields.Char(string="last name")
