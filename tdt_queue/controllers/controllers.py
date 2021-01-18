# -*- coding: utf-8 -*-
from odoo import http

# class TdtQueue(http.Controller):
#     @http.route('/tdt_queue/tdt_queue/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tdt_queue/tdt_queue/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tdt_queue.listing', {
#             'root': '/tdt_queue/tdt_queue',
#             'objects': http.request.env['tdt_queue.tdt_queue'].search([]),
#         })

#     @http.route('/tdt_queue/tdt_queue/objects/<model("tdt_queue.tdt_queue"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tdt_queue.object', {
#             'object': obj
#         })