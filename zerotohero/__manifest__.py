{
    'name':'Employee Loan Project',
    'author':'Justin',
    'depends':['base','hr','web','mail'],
    'installable':True,
    'auto_install':False,
    'application':True,
    'data':[
        'data/employee_email_template.xml',
        'security/ir.model.access.csv',
        'views/employee_loan_view.xml',
        'reports/loan_employee_report.xml'

    ]

}

