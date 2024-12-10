{
    'name':"Real Estate",
    'depends':['base','mail'],
    'installable':True,
    'application':True,
    'auto_install':False,
    'data':[
        'security/security.xml',
        "security/ir.model.access.csv",
        "views/real_estate_view.xml",

    ]

}