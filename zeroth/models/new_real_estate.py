from odoo import fields,models



class NewRealEstate(models.Model):
    _name='new.real.estate'
    _description='This is for practice'

    name=fields.Char(string='Name',required=True)
    title=fields.Text(string='Title',default='Title')
    description=fields.Text(string='Description')
    postcode=fields.Char(string='Post Code')
    date_availability=fields.Date(string='Date Availability',copy=False)
    expected_price=fields.Float(string="Expexted Price",required=True)
    selling_price=fields.Float(string="Selling Price",required=True)
    bedrooms=fields.Integer(string="Bedrooms",default='2')
    living_area=fields.Integer(string="Living Area (sqm)")
    fcades=fields.Integer(string="Fcades")
    garage=fields.Boolean(string="Garage")
    garden=fields.Boolean(string="Garden")
    garden_area=fields.Integer(string="Garden Area")
    active = fields.Boolean(default=True)
    property_type_id=fields.Many2one('real.property.type',string='Property Type')
    salesperson_id = fields.Many2one('res.users', string="Salesperson")
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)

    garden_orientation=fields.Selection([
        ("east","East"),
        ("west","West"),
        ("north","North"),
        ("south","South")
    ],string="Garden Orientation")
    state=fields.Selection([
        ('new','New'),
        ('offer_recieved','Offer Recieved'),
        ('offer_accepted','Offer Accepted'),
        ('sold','Sold'),
        ('canceled','Canceled')
    ],string="state",required=True,copy=False,default='new')


