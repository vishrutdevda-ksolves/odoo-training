from odoo import models,api,fields

class AccountMove(models.Model):
    _inherit='account.move'

    assistant=fields.Char(string='Vishrut')


