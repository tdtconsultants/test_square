# -*- coding: utf-8 -*-
from odoo import models, fields


class FulfillmentsPickup(models.Model):

    _name = "fulfillments.pickup"

    auto_complete_duration = fields.Char(string="The duration of time after which an open and accepted pickup fulfillment will automatically move to the "
                                                "COMPLETED state.Must be in RFC3339 duration format. If not set, this pickup fulfillment will remain accepted "
                                                "until it is canceled or completed.")
    cancel_reason = fields.Char(string="Cancel reason")
    curbside_pickup_buyer_arrived_at = fields.Char(string="Time the buyer arrived and is waiting for pick up")
    curbside_details = fields.Char(string="Curbside details")
    expires_at = fields.Char(string="fulfillment expire time")
    is_curbside_pickup = fields.Boolean(string="is curbside pickup")
    note = fields.Char(string="pickup details")
    pickup_at = fields.Char()
    pickup_window_duration = fields.Char()
    prep_time_duration = fields.Char(string="Time to prepere the fulfillment")
    recipient = fields.Many2one(comodel_name="fulfillments.recipient")
    schedule_type = fields.Selection([('scheduled', 'SCHEDULED'), ('asap', 'ASAP')])
