# -*- coding: utf-8 -*-

{

    'name': 'Library Management',

    'summary': """Management for a local library""",

    'description': """

        Library Management:
        Management for a local library.

    """,

    'author': 'daav-odoo',

    'website': 'https://www.odoo.com',

    'category': 'Training',

    'version': '0.1',

    'depends': ['base','website'],

    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menuitems.xml',
        'views/library_views.xml',
        'views/rental_views.xml',
        'views/book_copy_views.xml',
        'report/rental_report_templates.xml',
        'views/library_web_templates.xml',
        #'views/addenda_test.xml',
],

    'demo': [
    'demo/library_demo.xml',
],

}
