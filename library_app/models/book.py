from email.policy import default

from odoo import fields, models, api
from odoo.exceptions import ValidationError


class Book(models.Model):
    _name = 'book'
    _description = 'Book'
    # rec_name = 'name'
    _sql_constraints = [
        ('unique_name','unique("name")','This name is exist')
    ]

    name = fields.Char(required=True)
    code = fields.Char(required=True)
    ref = fields.Char(default='New')
    active = fields.Boolean(default=True)
    published_date = fields.Date()
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
    ])
    publisher_id = fields.Many2one('library.publisher')
    image = fields.Binary()


    def action_add_publisher(self):
        action = self.env['ir.actions.actions']._for_xml_id('library_app.publisher_wizard_action')
        action['context'] = {
            'default_book_id': self.id,
        }
        return action

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    # def action_published(self):
    #     for rec in self:
    #         rec.state = 'published'

    def server_published_state(self):
        for rec in self:
            rec.state = 'confirm'

    @api.model
    def create(self, vals):
        res = super(Book,self).create(vals)
        res.ref = self.env['ir.sequence'].next_by_code('book_ref_seq')
        return res

    def write(self, vals):
        res = super(Book, self).write(vals)
        print("inside the write method!")
        return res


    # @api.constrains('publisher_id')
    # def _check_publisher_id (self):
    #     for rec in self:
    #         if not rec.publisher_id:
    #             raise ValidationError("Publisher is required!")
