from odoo import fields,models

class RealPropertyType(models.Model):
    _name='real.property.type'

    name=fields.Char(string="Name")
