# -*- coding: utf-8 -*-

from odoo import http

class Library(http.Controller):

    @http.route('/library/books/', auth='public', website=True)
    def courses(self, **kw):
        books = http.request.env['library.management'].search([])
        return http.request.render('lib-mng.library_website', {
            'books': books,
        })

   