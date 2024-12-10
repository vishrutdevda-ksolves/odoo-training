from odoo import fields,models

class Exam(models.Model):
    _name = 'school.exam'
    _description = 'Exam'

    name = fields.Char('Exam Name', required=True)
    class_subject_id = fields.Many2one('school.class.subject', 'Class Subject')
    exam_date = fields.Date('Exam Date')
