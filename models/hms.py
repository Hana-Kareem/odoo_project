from odoo import fields, models


class Hms(models.Model):
    _name='hms.patient'
    _description = 'HMS'


    first_name = fields.Char()
    last_name = fields.Char()
    age = fields.Integer()
    birth_date = fields.Date()
    history_data = fields.Html(string="Attachment")
    history_name = fields.Char(string="Filename")
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('O-','O-'),
        ('O+','O+'),
        ('A-','A-'),
        ('A+','A+'),
        ('B-','B-'),
        ('B+','B+'),
        ('AB-','AB-'),
        ('AB+','AB+'),
    ],string='Blood Type', default='AB+')
    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()



