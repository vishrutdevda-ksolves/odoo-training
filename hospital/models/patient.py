

from odoo import fields,models

class Patient(models.Model):
    _name="hospital.patient"
    _description="Patient Information File"


    name=fields.Char(string="Name",required=True)
    date_of_birth=fields.Date(string="DOB")



