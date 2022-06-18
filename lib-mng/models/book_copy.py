# -*- coding: utf-8 -*-

from odoo import models, fields, api

class BookCopy(models.Model):
    _name = 'library.management_copy'
    _description = 'Book copy Info'

    _inherits = {
        'library.management':'book_copy',
    }  
    
    book_copy = fields.Many2many('library.management', required=True, ondelete="cascade")
 
