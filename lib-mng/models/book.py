# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Book(models.Model):
    _name = 'library.management'
    _description = 'Book info' 
    
    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    editor = fields.Char(string='Editor')
    publisher = fields.Char(string='Publisher')
    year = fields.Integer(string='Year')
    ISBN = fields.Char(string='ISBN')
    genre = fields.Char(string='Genre')
    note = fields.Text(string='Note')
    
    active = fields.Boolean(string='Active', default=True)
    
    rental_id = fields.One2many(comodel_name='library.rental',
                                  inverse_name='book_id',
                                  string='Rentals')
    
    @api.onchange('ISBN')
    def _onchange_len_isbn(self):
        if len(self.ISBN) < 13:
            raise ValidationError('ISBN cannot be less than 13 characters.')
