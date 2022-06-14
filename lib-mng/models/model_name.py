# -*- coding: utf-8 -*-

from odoo import models, fields, api

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
    
    active = fields.Boolean(string='Active', default=True)