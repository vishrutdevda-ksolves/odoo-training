from odoo import models,fields

class LoanRepaymentLine(models.Model):
    _name = 'employee.loan.line'
    _description = 'Employee Loan Repayment Line'

    loan_id = fields.Many2one('employee.loan', string='Loan Repayment')
    emi_number = fields.Integer(string='EMI Number', required=True)
    repayment_amount = fields.Float(string='Repayment Amount', required=True)
    emi_date = fields.Date(string='EMI Date', required=True)
    paid = fields.Boolean(string='Paid', default=False)


