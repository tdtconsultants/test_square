# -*- coding: utf-8 -*-
from odoo import models, fields


class LineItemDiscount(models.Model):

    _name = "line.item.discount"

    amount_money_amount = fields.Float(string="amount")
    amount_money_currency = fields.Many2one(comodel_name="res.currency", string="amount currency")
    applied_money_amount = fields.Float(string="amount applied")
    applied_money_currency = fields.Many2one(comodel_name="res.currency", string="applied currency")
    catalog_object_id = fields.Char(string="catalog object id")
    metadata = fields.One2many(comodel_name="metadata", string="metadata")
    name = fields.Char(string="name")
    percentage = fields.Char(string="percentage of discount")
    scope = fields.Selection([('other_discoutn_scope', 'OTHER_DISCOUTN_SCOPE'),('line_item', 'LINE_ITEM'),('order', 'ORDER')])
    type = fields.Selection([('unknown_discount','UNKNOWN_DISCOUNT'), ('fixed_percentage', 'FIXED_PERCENTAGE'),
                             ('fixed_amount', 'FIXED_AMOUNT'), ('variable_percentage', 'VARIABLE_PERCENTAGE'), ('variable_amount', 'VARIABLE_AMOUNT')])
    uid = fields.Char(string="id of discounts within the order")
