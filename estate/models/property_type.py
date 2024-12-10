from odoo import fields,models

class PropertyType(models.Model):
    _name="property.real.estate"
    _description="trial"

    name=fields.Char(required=True)
