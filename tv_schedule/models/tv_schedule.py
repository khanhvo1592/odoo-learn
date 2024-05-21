from odoo import models, fields

class TVSchedule(models.Model):
    _name = 'tv.schedule'
    _description = 'TV Schedule'

    name = fields.Char(string='Program Name', required=True)
    broadcast_date = fields.Date(string='Broadcast Date', required=True)
    start_time = fields.Float(string='Start Time', required=True)
    end_time = fields.Float(string='End Time', required=True)
    channel = fields.Selection([
        ('tv', 'TV'),
        ('radio', 'Radio')
    ], string='Channel', required=True)
