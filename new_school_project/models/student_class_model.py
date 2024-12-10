from odoo import fields,models

class StudentClass(models.Model):
    _name = 'school.student.class'
    _description = 'Student Class'

    student_id = fields.Many2one('school.student', 'Student', required=True)
    class_id = fields.Many2one('school.class', 'Class', required=True)
    subjects = fields.One2many('school.class.subject', 'class_id', 'Subjects')


