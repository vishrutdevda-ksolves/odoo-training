from odoo import models,fields

class TestModelLine(models.Model):
    _name = "test.model.line"
    _description = "Test Model Line"

    model_id = fields.Many2one("real.estate",string="Trial")
    field_1 = fields.Char(string ="field1")
    field_2 = fields.Char(string="field2")
    field_3 = fields.Char(string="field3")