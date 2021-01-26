# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PosPayment(models.Model):

    _inherit = 'pos.payment'

    payment_square_id = fields.Char(string="payment id from square")
    tip_amount = fields.float(string="amount tiped")
    tip_currency_id = fields.Many2one(string="currency id of the tip", comodel_name="res.currency")
    app_fee_amount = fields.float(string="fee amount ")
    app_fee_currency_id = fields.Many2one(string="currency id of the app_fee", comodel_name="res.currency")
    square_customer_id = fields.Char(string="customer id on square")
    square_order_id = fields.Char(string="order id on square")
    square_location_id = fields.Char(string="location id on square")
    buyer_email_address = fields.Char(string="buyer email")
    note = fields.Char(string="notes")
    shipping_address_id = fields.Many2one(comodel_name="ShippingAddress", string="Shipping address")
    billing_address_id = fields.Many2one(comodel_name="BillingAddress", string="Billing address")

    #def create_patner_square(self):
