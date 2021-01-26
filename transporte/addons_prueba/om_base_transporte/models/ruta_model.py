# -*- coding: utf-8 -*-
from odoo import fields, models


class ruta(models.Model):
    _name = "ruta"
    _description = 'Ruta'

    name = fields.Integer(string="Numero de la ruta")
    trayecto = fields.Char(string="Trayecto de la ruta")
    choferes = fields.Many2many(comodel_name='chofer')
    omnibuses = fields.Many2many(comodel_name='omnibus')