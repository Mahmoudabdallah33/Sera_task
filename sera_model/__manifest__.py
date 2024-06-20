
{
    'name' : 'Sera Task',
    'version' : '1.2',
    'summary': ' ',
    'sequence': 0,
    'description': """ Task From Sera Group  """,
    'category': 'New Model',
    'website': ' ',
    'depends' : ['mail', ],
    'data': [
        'security/ir.model.access.csv',
        'security/security_group.xml',
        'views/menu.xml',
        'views/sera_view.xml',
        'report/sera_model_report.xml',
        'report/sera_report_template.xml',


    ],
    'demo': [     ],
    'installable': True,
    'application': True,
    'assets': {

    },
    'license': 'LGPL-3',
}
