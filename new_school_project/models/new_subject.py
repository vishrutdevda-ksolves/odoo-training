from odoo import models, fields

class Subject(models.Model):
    _name = 'school.subject'
    _description = 'Subject'

    name = fields.Char('Subject Name', required=True)
    subject_id = fields.Char('Subject ID', required=True)
