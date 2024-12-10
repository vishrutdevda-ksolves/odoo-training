from odoo import fields,models

class Class(models.Model):
    _name = 'school.class'
    _description = 'Class'

    name = fields.Char('Class Name', required=True)
    class_id = fields.Char('Class ID', required=True)
