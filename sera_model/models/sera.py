from odoo import api, fields, models

class SeraModel(models.Model):
    _name = 'sera.model'
    _description = 'Sera Model'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(String = "Name", required = True)
    description = fields.Text(string = 'Description')

    start_date = fields.Datetime(string="Start Date", default=fields.Datetime.now)

    end_date = fields.Datetime(string="End Date")

    status = fields.Selection([('Planned', 'Planned'),
                              ('In Progress', 'In Progress'),
                              ('Done', 'Done')], string="Status",default="planned")

