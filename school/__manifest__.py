# -*- coding: utf-8 -*-
{
    'name': "School",
    'summary': """ Manage your school """,
    'description': """
        School module for managing trainings:
            - training courses
            - teacher realations
            - classes certifications
    """,

    'author': "Upward co.",
    'category': 'Test',
    'version': '17.0',
    'depends': ['base'],

    'data': [
         'security/ir.model.access.csv',
         'views/school_main_views.xml',
         'views/student_views.xml',
         'views/classroom_views.xml',
         'views/teacher_views.xml',
    ],
    # 'assets': {'web.assets_backend':['static/src/css/styles.css']},
    'installable':True,
}


