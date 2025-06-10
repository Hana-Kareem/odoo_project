{
    'name':"HMS App",
    'summery':""" """,
    'description':""" """,
    'auther':"Hana Atef",
    'category':"Productivity",
    'version':"17.0.0.1.0",
    'depends':['base',
               'mail',
               'sale_management'],
    'application':True,
    'license': 'LGPL-3',
    'data':[
        'security/ir.model.access.csv',
        'views/base_menus_hms.xml',
        'views/hms_patient.xml',

    ],
}