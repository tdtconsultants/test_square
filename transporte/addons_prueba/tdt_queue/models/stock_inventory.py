from odoo import models, fields


class StockInventory(models.Model):

    _inherit = 'stock.inventory'

    square_inventory_adjustment = fields.Boolean(string="is square adjustment")
