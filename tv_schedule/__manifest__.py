{
    'name': 'TV Schedule Management',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Manage TV and Radio Schedule',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/tv_schedule_views.xml',
        'views/tv_schedule_import_views.xml',
    ],
    'installable': True,
    'application': True,
}
