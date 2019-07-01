{
    'name': 'Deutschland SKR49 - Accounting',
    'version': '11.0.1.0.0',
    'author': 'humanilog',
    'website': 'https://humanilog.org',
    'category': 'Localization',
    'description': """
Dieses Modul beinhaltet einen deutschen Kontenrahmen basierend auf dem SKR49.
=========================================================================================

German accounting chart and localization for the SKR49.
  """,
    'depends': ['account'],
    'data': [
        'data/account_account_tags_data.xml',
        'data/account_chart.xml',
        'data/account_tax_fiscal_position.xml',
        'data/account.chart.template.yml',
    ],
    'installable': True,
}
