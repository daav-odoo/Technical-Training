# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta

class Rental(models.Model):
    _name = 'library.rental'
    _description = 'Rental Info'
    
    book_id = fields.Many2one(comodel_name='library.management',
                               string='Rental',
                               ondelete='cascade',
                               required=True)
    
    name = fields.Char(string='Title', related='book_id.name')
        
        
    customer_ids = fields.Many2many(comodel_name='res.partner',
                                   string='Customers')
    
    start_date = fields.Date(string='Start Date',
                            default=fields.Date.today)
    
    duration = fields.Integer(string="Rental Days",
                             default=1)
    
    end_date = fields.Date(string='End Date',
                          compute='_compute_end_date',
                          inverse='_inverse_end_date',
                          store='True')
    
    @api.depends('start_date','duration')
    def _compute_end_date(self):
        for record in self:
            if not (record.start_date and record.duration):
                record.end_date = record.start_date
            else:
                duration = timedelta(days=record.duration)
                record.end_date = record.start_date + duration
    
    def _inverse_end_date(self):
        for record in self:
            if record.start_date and record.end_date:
                record.duration = (record.end_date - record.start_date).days + 1
            else:
                continue