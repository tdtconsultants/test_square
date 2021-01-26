# -*- coding: utf-8 -*-
from odoo import fields, models
import datetime
from datetime import timedelta


class Panel(models.Model):
    _name = "panel_info"
    _description = "infocliente"

    amount_of_leves = fields.Integer(compute='_compute_amount_of_leave',string='Cantidad de omnibus que salieron en la ultima hora')

    def _compute_amount_of_leave(self):
        actual_date = datetime.datetime.now()
        one_hour_less_date = actual_date - timedelta(hours=1)
        omnibus_cantidad = self.env['omnibus'].search([('fecha_salida', '>=', one_hour_less_date),('fecha_salida', '<=', actual_date)])
        self.amount_of_leves = len(omnibus_cantidad.ids)

