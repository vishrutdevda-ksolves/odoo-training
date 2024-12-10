from odoo import fields,models,api
from dateutil.relativedelta import relativedelta

class Student(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char('Student Name', required=True)
    roll_no = fields.Char('Roll Number', required=True)
    dob = fields.Date('Date of Birth')
    age = fields.Integer('Age')

    parent_name = fields.Many2one('res.partner', 'Parent')
    student_history = fields.One2many('school.student.class', 'student_id', 'History')




    def create(self, vals):
        if 'dob' in vals:
            vals['age'] = relativedelta(fields.Date.today(), vals['dob']).years
        return super(Student, self).create(vals)


    def write(self, vals):
        if 'dob' in vals:
            vals['age'] = relativedelta(fields.Date.today(), vals['dob']).years
        return super(Student, self).write(vals)
