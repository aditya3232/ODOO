{
    'name': 'Module Custom Pembelian',
    'version': '13.0.1.latest',
    'category': 'purchase',
    'summary': 'Module Custom Pembelian',
    'description': """
        Ini adalah module custom, untuk pembelajaran
    """,
    'website': '',
    'author': 'Adit',
    'depends': ['web','base'],
    'data': [
        'security/ir.model.access.csv',
        'views/algoritma_pembelian_view.xml',
        'views/algoritma_pembelian_action.xml',
        'views/algoritma_pembelian_menuitem.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'OEEL-1',

}