from odoo import fields,models


class E(models.Model):
    _name="estate.property.tag"
    _description="Property Tag"

    name=fields.Char(string="Name",required=True)

