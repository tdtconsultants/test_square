# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PosLocation(models.Model):

    _inherit = 'stock.warehouse'

    square_location_id = fields.Char(string="location id in square")
    square_address_id = fields.Many2one(comodel_name="SquareAddress", string="Address in square format")
    business_email = fields.Char(string="business_email")
    business_name = fields.Char(string="business_name")
    description = fields.Char(string="description")
    facebook_url = fields.Char(string="facebook_url")
    instagram_username = fields.Char(string="instagram username")
    language_code = fields.Char(string="language_code")
    mcc = fields.Char(string="mcc")
    name = fields.Char(string="name of location")
    phone_number = fields.Char(string="phone_number")
    status = fields.Char(string="status")
    timezone = fields.Char(string="timezone")
    twitter_username = fields.Char(string="twitter username")
    type = fields.Char(string="type of location")
    website_url = fields.Char(string="website")
    currency = fields.Char(string="currency")
    square_warehouse = fields.Boolean(string="Warehouse managed in square")
