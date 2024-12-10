from odoo import models, fields

class Division(models.Model):
    _name = 'school.division'
    _description = 'Division'

    name = fields.Char('Division Name', required=True)
    class_id = fields.Many2one('school.class', 'Class', required=True)
    subjects = fields.One2many('school.class.subject', 'division_id', 'Subjects')

