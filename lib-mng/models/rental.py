# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Rental Info'
    
    book_id = fields.Many2one(comodel_name='library.management',
                               string='Rental',
                               ondelete='cascade',
                               required=True)
    
    name = fields.Char(string='Title', related='book_id.name')
        
        
    customer_id = fields.Many2many(comodel_name='res.partner',
                                   string='Customers')
    
    address_id = fields.Many2one(comodel_name='res.partner',
                                   string='Customers')
    
    customer_name = fields.Char(string='Customer_Name', related='customer_id.company_name')
