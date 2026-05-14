{
    'name': 'Sales Credit Limit Validation',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Prevents sales order confirmation if customer balance exceeds limit',
    'description': """
        This module adds a credit limit field to customers and validates 
        total outstanding receivables before confirming a Sales Order.
    """,
    'depends': ['base','sale',
        'sale_management', 
        'account',
    ],
    'data': [
    'views/partner_view.xml',
],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}