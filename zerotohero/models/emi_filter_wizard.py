from odoo import models, fields, api
from datetime import datetime
from dateutil.relativedelta import relativedelta

class EmiFilterWizard(models.TransientModel):
    _name = 'emi.filter.wizard'
    _description = 'EMI Filter Wizard'

    month = fields.Selection([
        ('01', 'January'), ('02', 'February'), ('03', 'March'),
        ('04', 'April'), ('05', 'May'), ('06', 'June'),
        ('07', 'July'), ('08', 'August'), ('09', 'September'),
        ('10', 'October'), ('11', 'November'), ('12', 'December')
    ], string="Month", required=True)

    emi_line_ids = fields.Many2many(
        'employee.loan.line',
        string='Unpaid EMI Lines'
    )

    @api.onchange('month')
    def _onchange_month(self):

        if self.month:
            selected_month = int(self.month)
            current_year = datetime.today().year
            start_date = datetime(current_year, selected_month, 1)
            end_date = start_date + relativedelta(months=1)


            emi_lines = self.env['employee.loan.line'].search([
                ('emi_date', '>=', start_date),
                ('emi_date', '<', end_date),
                ('paid', '=', False)
            ])

            self.emi_line_ids = [(6, 0, emi_lines.ids)]
        else:

            self.emi_line_ids = [(5, 0, 0)]

    def action_mark_as_paid_all(self):
        for record in self:
            for emi_line in record.emi_line_ids:
                if not emi_line.paid:
                    emi_line.paid = True


    def action_apply_filter(self):
        pass
