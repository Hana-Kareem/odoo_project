from odoo import fields, models

class Ticket(models.Model):
    _name= 'do.ticket'
    _description = 'Ticket'

    name = fields.Char()
    number = fields.Integer()
    tag = fields.Char()
    state = fields.Selection([
        ('new','New'),
        ('doing','Doing'),
        ('done','Done'),
    ],string='Status', default='new')
    file_data = fields.Binary(string="Attachment",attachment=True)
    file_name= fields.Char(string="File Name")
    assign_to = fields.Many2one('res.users', string='Assign To')
    description = fields.Text()

