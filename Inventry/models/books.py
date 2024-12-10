from odoo import fields,models

class Books(models.Model):
    _name="books.inventory"
    _description="Thriller"

    fname=fields.Char(string="BookName",required=True)
    btype=fields.Char(string="TypeName",required=True)
    bstory=fields.Text(string="Story")
    bcharacters=fields.Text(string="characters_in_the_story",required=True)
    date_of_publish=fields.Date(string="Date_of_publish")
