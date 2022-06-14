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

    'depends': ['base'],

    'data': [
        'security/module_security.xml',
        'security/ir.model.access.csv',
        'views/module_menuitem.xml',
],

    'demo': [
    'demo/module_demo.xml',
],

}