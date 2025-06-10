from odoo import fields, models, api


class AddPublisher(models.TransientModel):
    _name = 'publisher.wizard'
    _description = 'Add Publisher Wizard'

    book_id = fields.Many2one('book')
    publisher_id = fields.Many2one('library.publisher')

    def action_add_publisher(self):
        self.book_id.publisher_id = self.publisher_id.id

