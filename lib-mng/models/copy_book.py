# -*- coding: utf-8 -*-

from odoo import models, fields, api

class CopyBook(models.Model):
    _inherits = 'library.management'

    rental_id = fields.Many2one(comodel_name='library.rental',
        string='Related rental', ondelete='set null')


    

   