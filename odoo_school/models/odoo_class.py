from odoo import models, fields

class OdooClass(models.Model):
    _name = "odoo.class"
    _description = "Class Details"

    name = fields.Char(string="Class Name", required=True)
    student_ids = fields.One2many('odoo.student', 'class_id', string="Students")
