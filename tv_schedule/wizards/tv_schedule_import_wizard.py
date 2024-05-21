from odoo import models, fields, api
import base64
import csv
from io import StringIO

class TVScheduleImportWizard(models.TransientModel):
    _name = 'tv.schedule.import.wizard'
    _description = 'TV Schedule Import Wizard'

    file = fields.Binary(string='CSV File', required=True)
    filename = fields.Char(string='Filename')

    @api.model
    def _create_schedule(self, row):
        self.env['tv.schedule'].create({
            'name': row.get('name'),
            'broadcast_date': row.get('broadcast_date'),
            'start_time': float(row.get('start_time', 0)),
            'end_time': float(row.get('end_time', 0)),
            'channel': row.get('channel'),
        })

    def import_file(self):
        if not self.file:
            return

        data = base64.b64decode(self.file)
        file_input = StringIO(data.decode("utf-8"))
        reader = csv.DictReader(file_input)

        for row in reader:
            self._create_schedule(row)
