from odoo import models, fields

class OdooFees(models.Model):
    _name = "odoo.fees"
    _description = "Fees Details"

    month = fields.Char(string="Month")
    amount = fields.Float(string="Amount")
    student_id = fields.Many2one('odoo.student', string="Student")
