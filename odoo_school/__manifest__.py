{
    'name':'Odoo School',
    'depends':['base'],
    'installable':True,
    'auto_install':False,
    'application':True,
    'data':[
        'security/ir.model.access.csv',
        'views/odoo_student_views.xml',
        'views/odoo_subjects.xml',
        'views/odoo_fees.xml',
        'views/odoo_class.xml',
        'views/menu.xml'

    ]
}