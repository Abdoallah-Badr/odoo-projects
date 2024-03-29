# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """ Manage Tranings """,

    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attending registration
    """,

    'author': "Abdoallah Badr",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/openacademy.xml',
        'views/partner.xml',
        # 'views/views.xml',
        # 'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
