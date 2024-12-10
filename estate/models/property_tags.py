from odoo import fields,models

class PropertyType(models.Model):
    _name="property.tags"
    _description="trial"

    name = fields.Char(required=True)
