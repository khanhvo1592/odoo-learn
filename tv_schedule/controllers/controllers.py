# -*- coding: utf-8 -*-
# from odoo import http


# class TvSchedule(http.Controller):
#     @http.route('/tv_schedule/tv_schedule', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tv_schedule/tv_schedule/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tv_schedule.listing', {
#             'root': '/tv_schedule/tv_schedule',
#             'objects': http.request.env['tv_schedule.tv_schedule'].search([]),
#         })

#     @http.route('/tv_schedule/tv_schedule/objects/<model("tv_schedule.tv_schedule"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tv_schedule.object', {
#             'object': obj
#         })

