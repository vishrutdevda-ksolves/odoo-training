from odoo import models, fields

class OdooStudent(models.Model):
    _name = "odoo.student"
    _description = "Student Details"

    name = fields.Char(string="Student Name")
    dob = fields.Date(string="Date Of Birth")
    contact_number = fields.Char(string="Contact Number")
    email = fields.Char(string="Email")
    class_id = fields.Many2one('odoo.class', string="Class")
    subject_ids = fields.Many2many('odoo.subject', string="Subjects")
    fee_ids = fields.One2many('odoo.fees', 'student_id', string="Fees")
