# -*- coding: utf-8 -*-
from odoo import fields, models, api
import datetime
from datetime import timedelta


class omnibus(models.Model):
    _name = "omnibus"
    _description = 'Omnibus'

    capacity = fields.Integer(string="Capacidad del omnibus")
    chofer = fields.Many2many(comodel_name="chofer")
    cost = fields.Integer(string="Costo de mantenimiento")
    type_of_fuel = fields.Selection([('diesel', 'Diesel'), ('gasoline', 'Gasoline'), ('electric', 'Electric')])
    registration_plate = fields.Integer(string="Matricula")
    ruta = fields.Many2one(comodel_name="ruta", string="Ruta")
    active = fields.Boolean(string="Activo")
    fecha_entrada = fields.Datetime(string="fecha de entrada")
    fecha_salida = fields.Datetime(string="fecah de salida")

    def _compute_amount_of_leave(self):
        actual_date = datetime.datetime.now()
        one_hour_less_date = actual_date - timedelta(hours=1)
        amount_of_leave = 0
        omnibus_cantidad = self.env['omnibus'].search([('fecha_salida', '>=', one_hour_less_date),('fecha_salida', '<=', actual_date)])
        amount_of_leave = len(omnibus_cantidad.ids)
