from odoo import fields,models

class EstatePropertyOffer(models.Model):
    _name="estate.property.offer"
    _description="Offers"

    name = fields.Char(string="Name")
    offer_id = fields.Many2one('practice.practice',string="offerType")