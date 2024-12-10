from odoo import fields,models,api


class PropertyWithGarden(models.Model):
    _inherit='real.estate'

    has_garden=fields.Boolean(string="Has Garden",default=False)


    @api.onchange('has_garden')
    def _onchange_has_garden(self):

        if self.has_garden:
            self.property_status='property has garden'

        else:
            self.property_status='not garden'



