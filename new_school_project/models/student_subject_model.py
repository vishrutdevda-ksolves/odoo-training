from odoo import fields,models

class StudentSubject(models.Model):
    _name = 'school.student.subject'
    _description = 'Student Subject'

    student_id = fields.Many2one('school.student', 'Student', required=True)
    subject_id = fields.Many2one('school.subject', 'Subject', required=True)
