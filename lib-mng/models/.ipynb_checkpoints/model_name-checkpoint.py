# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Libro(models.Model):
    _name = 'library.management'
    _description = 'Management of Books' 
    
    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    author = fields.Text(string='Author')
    
    active = fields.Boolean(string='Active', default=True)