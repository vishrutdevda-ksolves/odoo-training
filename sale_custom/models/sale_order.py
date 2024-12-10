
from odoo import models , fields, api




class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_quantity = fields.Integer('Total Quantity' , compute='_compute_total_quantity')

    @api.depends('order_line.product_uom_qty')
    def _compute_total_quantity(self):
        for sale_order in self:
            sale_order.total_quantity = sum([line.product_uom_qty for line in sale_order.order_line])


    def action_open_wizard(self):
        action = {
            'type': 'ir.actions.act_window',
            'name': 'Sales Order',
            'res_model': 'sale.order',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'current',  # Opens the record in the current window
            'res_id': self.id,    # Opens the current sale order record
        }
        return action



