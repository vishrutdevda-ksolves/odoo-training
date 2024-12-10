from odoo import models, fields

class OdooSubject(models.Model):
    _name = "odoo.subject"
    _description = "Subject Details"

    name = fields.Char(string="Subject Name", required=True)


