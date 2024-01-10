# -*- coding: utf-8 -*-
{
    'name': "School Module",
    'summary': """ Manage your school moshen updates""",
    'description': """
        School module for managing trainings:
            - training courses
            - teacher realations
            - classes certifications
    """,

    'author': "Abdoallah Badr",
    'category': 'Test',
    'version': '1.0',
    'depends': ['base'],

    'data': [
         'security/ir.model.access.csv',
         'views/schoolmodule.xml',
    ],
    'installable':True,


}
