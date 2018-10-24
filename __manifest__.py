{
  'name': 'Deutschland SKR49 HLO - Accounting',
  'version': '2.0',
  'author': 'humanilog',
  'website': 'https://humanilog.org',
  'category': 'Localization/Account Charts',
  'description': """
Dieses Modul beinhaltet einen deutschen Kontenrahmen basierend auf dem SKR49.
=========================================================================================

German accounting chart and localization for the SKR49.
  """,
  'depends': ['l10n_de'],
  'data': [
    'data/account.account.type.csv',
    'data/account_chart.xml',
    'data/account_tax_fiscal_position.xml',
    'data/account.chart.template.yml',
  ],
  'installable': True,
}
