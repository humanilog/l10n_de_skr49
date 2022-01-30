{
  'name': 'Deutschland SKR49 - Accounting',
  'version': '12.0.1.0.0',
  'author': 'humanilog',
  'website': 'https://humanilog.org',
  'category': 'Localization',
  'description': """
German accounting chart and localization based on SKR49.
=========================================================================================
Be aware, the dependency to 'l10n_de' module will istall as well the account charts for 
skr03 and skr04 which should be deinstalled after the installation of this module, in 
order to mitigate the usage of wrong accounts from these charts. Same applies for odoo 
databases created using Germany as country and German as language.
  """,
  'depends': ['l10n_de'],
  'data': [
    'data/l10n_de_skr49_chart_data.xml',
    'data/data_account_type.xml',
    'data/account_account_tags_data.xml',
    'data/account_chart.xml',
    'data/l10n_de_skr49_chart_post_data.xml',
    'data/account_tax_fiscal_position.xml',
    'data/account_chart_template_data.xml',
  ],
  'installable': True,
}
