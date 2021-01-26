# -*- coding: utf-8 -*-
from odoo import api, fields, models


class chofer(models.Model):
    _name = "chofer"
    _description = "Chofer"

    name = fields.Char(string='Nombre del chofer')
    routes = fields.Many2many(comodel_name='ruta', inverse_name="choferes")
    availability = fields.Boolean(compute='_compute_availability',string='Disponibilidad')
    type_of_licence = fields.Selection([('normal', 'Normal'), ('professional', 'Profressional')])
    age = fields.Integer(string='edad')
    omnibus_id = fields.Many2many(comodel_name="omnibus", inverse_name="chofer", string="Omnibus", relate='omnibus')
    multas = fields.Integer(string="Cantidad de multas")

    @api.depends('multas')
    def _compute_availability(self):
        if self.multas >= 3:
            self.availability = False
        else:
            self.availability = True

