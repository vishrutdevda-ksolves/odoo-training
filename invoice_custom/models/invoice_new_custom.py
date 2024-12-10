
from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'


    name = fields.Char('Description')
    quantity = fields.Float('Quantity')
    product_id = fields.Many2one('product.product', 'Product')
    #
    # @api.onchange('quantity')
    # def _onchange_quantity(self):
    #      for line in self:
    #         if line.product_id:
    #             line.name = f'{line.product_id.name} - Quantity: {line.quantity}'
