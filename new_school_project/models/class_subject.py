from odoo import fields,models

class ClassSubject(models.Model):
    _name = 'school.class.subject'
    _description = 'Class Subject'

    subject_id = fields.Many2one('school.subject', 'Subject', required=True)
    class_id = fields.Many2one('school.class', 'Class', required=True)
    max_marks = fields.Integer('Max Marks', required=True)
    division_id=fields.Many2one('school.division',string="Division Id")

