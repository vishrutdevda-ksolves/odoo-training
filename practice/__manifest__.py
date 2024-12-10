

{

    'name':"Vishrut",
    'depends':['base','mail','sale','sale_management'],
    'installable':True,
    'application':True,
    'auto_install':False,
    'data':[
        'security/ir.model.access.csv',
        'data/ir_sequence_estate.xml',
        'views/estate_view.xml',

    ]




}
