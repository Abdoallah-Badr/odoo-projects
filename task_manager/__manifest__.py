{
    'name':"Task manager",
    'description':'''
        Task manager for handling:
         - create tasks
         - track todos
    ''',
    'author':"abduallah badr",
    'category': 'Tools',
    'version': '1.0',
    'depends': ['base'],
    'data':['views/view.xml',
            'security/ir.model.access.csv'
    ],
    'installable':True,
    'application': True,
}