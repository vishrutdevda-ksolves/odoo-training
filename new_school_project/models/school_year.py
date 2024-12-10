from odoo import fields,models,api

class SchoolYear(models.Model):
    _name = 'school.year'
    _description = 'School Year'

    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date', required=True)
    is_current = fields.Boolean('Is Current Year', compute='_compute_is_current')

    @api.depends('start_date', 'end_date')
    def _compute_is_current(self):
        today = fields.Date.today()
        for record in self:
            record.is_current = record.start_date <= today <= record.end_date

