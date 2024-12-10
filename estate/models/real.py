from odoo import fields,models,api
from odoo.exceptions import ValidationError


class TestModel(models.Model):
    _name="real.estate"
    _description="Real Estate Project"
    _inherit = ['mail.thread','mail.activity.mixin']



    Fname = fields.Char(string="PropertyOwnerName",required=True)
    Bname=fields.Char(string="PropertyBuyerName",required=True)
    ptype_id=fields.Many2one("property.real.estate",string="TypeName")
    Parea=fields.Text(string="Parea")
    area=fields.Float(string="Area",required=True)
    Price_per_sqft=fields.Float(string="price_per_sqft")
    Pcharacters=fields.Text(string="propertybroker")
    date_of_sell=fields.Date(string="Date")
    tag_ids = fields.Many2many("property.tags",string="tags")
    total_price = fields.Float(string="Total Price")
    property_area_ids=fields.One2many("property.area.area",'property_name_area_id',string="one to many relation")
    action_do_something=fields.Text(string="Action Button")
    property_status=fields.Char(string='Sold or unsold')
    partner_id=fields.Many2one('res.partner',string="Customer")


    description = fields.Char()
    line_ids = fields.One2many("test.model.line", "model_id")

    @api.constrains('area')
    def _check_area(self):
        for record in self:
            if record.area <=0:
                raise ValidationError("area should not be negative")

    @api.onchange("area","Price_per_sqft")
    def _onchange_price_persqft(self):
        for records in self:
            records.total_price = records.area*records.Price_per_sqft


    def action_do_something(self):
        # for record in self:
        #     record.property_status="Sold"
        # return {
        #
        #         "type": "ir.actions.act_window",
        #         "res_model": "product.template",
        #         "views": [[False, "form"]],
        #         # "res_id": 23,
        #         "target": "new",
        #
        # }

        return {'warning': {
            'title': ("Scheduled action disabled"),
            'message': (
                "This scheduled action has been disabled because its interval number is not a strictly positive value.")}
        }

    def action_open_product_form(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "product.template",
            "views": [[False, "form"]],
            "res_id": 23,
            "target": "new",
        }


    def action_open_contact(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "views": [[False, "kanban"]],
            "res_id": 358,
            "target": "new",

        }













    








