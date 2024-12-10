from odoo import fields,models

class StudentExam(models.Model):
    _name = 'school.student.exam'
    _description = 'Student Exam'

    student_id = fields.Many2one('school.student', 'Student', required=True)
    exam_id = fields.Many2one('school.exam', 'Exam', required=True)
    marks = fields.Integer('Marks Obtained')
