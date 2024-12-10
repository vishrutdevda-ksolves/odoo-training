from odoo import fields,models,api



class Practice(models.Model):
    _name="practice.practice"
    _description="this is my practice model"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",required=True)
    description = fields.Text(string="Title")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Date")
    expected_price = fields.Float(string="Expected Price",required=True)
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms")
    living_area = fields.Integer(string="Living Area")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    property_type_id=fields.Many2one('estate.property.type',string="TypeName")
    sales_person = fields.Many2one('res.users', string='Salesperson')
    buyer=fields.Char(string="Buyers")
    tag_ids=fields.Many2many("estate.property.tag",string="Tag Id",required=True)
    total_area=fields.Float(string="Property Area")
    price_per_sqft=fields.Integer(string="Price Per Sqft")
    total_price=fields.Float(string=" Property Price")
    offer_num_ids=fields.One2many( "estate.property.offer","offer_id",string="Offer")
    date_time_field=fields.Datetime(string="DateTime")
    seq_num=fields.Char(string="Sequence Number",readonly=True,copy=False,index=True,default= 'New')
    image = fields.Binary("Property Image", attachment=True, help="Image of the property", required=False)
    status = fields.Selection([
        ('draft', 'Draft'),
        ('confirm','Confirm'),
        ('ongoing','Ongoing'),
        ('sold', 'Sold'),
        ('cancel', 'Canceled'),
    ], string='Status',default = 'draft')


    @api.onchange('total_area', 'price_per_sqft')
    def _onchange_total_price(self):
        for record in self:
            if record.total_area and record.price_per_sqft:
                record.total_price = record.total_area * record.price_per_sqft
            else:
                record.total_price = 0.0

    @api.model
    def create(self, vals):
        if vals.get('seq_num', 'New') == 'New':
            vals['seq_num'] = self.env['ir.sequence'].next_by_code('practice.seq.estate') or 'New'
        res = super(Practice, self).create(vals)
        return res

    def action_confirm_form(self):
        for rec in self:
            rec.status='confirm'


    def action_ongoing_form(self):
         for rec in self:
             rec.status='ongoing'

    def action_sold_form(self):
         for rec in self:
             rec.status='sold'

    def action_canceled_form(self):
         for rec in self:
             rec.status='cancel'




    # property_area=fields.Float(string="Property Area")
    # price_per_sqft=fields.Float(string="Price per sqft")
    # property_price=fields.Float(string="Property Price")
    # sales_quantity=fields.One2many('sales.order.line',' practice_id',string="Quantity")
    #
    #
    #
    #
    # total_sales_quantity=fields.Float(string='Total Quantity Sum')


    #@api.depends('sale_order_line.partner_id')
    # def _compute_total_sales_quantity(self):
    #     for record in self:
    #










    def action_open_product_form(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "product.template",
            "views": [[False, "form"]],
            "res_id": 23,
            "target": "new",
        }



    # def change_status(self):
    #     properties = self.env['estate.property'].search([('state', '=', 'Cancelled')])
    #     properties.write





























