from odoo import models, fields, api
import base64
import csv
from io import StringIO

class TVScheduleImportWizard(models.TransientModel):
    _name = 'tv.schedule.import.wizard'
    _description = 'TV Schedule Import Wizard'

    file = fields.Binary(string='File', required=True)
    filename = fields.Char(string='Filename')

    def import_file(self):
        if self.file:
            file_content = base64.b64decode(self.file)
            file_content = file_content.decode('utf-8')
            csv_reader = csv.DictReader(StringIO(file_content))
            for row in csv_reader:
                self.env['tv.schedule'].create({
                    'name': row['name'],
                    'broadcast_date': row['broadcast_date'],
                    'start_time': float(row['start_time']),
                    'end_time': float(row['end_time']),
                    'channel': row['channel'],
                })
