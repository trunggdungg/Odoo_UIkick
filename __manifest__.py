{
    'name': 'UIKick - Crowdfunding Website',
    'version': '1.0',
    'summary': 'Kickstarter-style discovery & campaign page (converted from React)',
    'description': """
        Website pages replicating a Kickstarter-like project discovery page
        and campaign detail page, originally built in React + Tailwind and
        ported to Odoo QWeb templates.
    """,
    'category': 'Website',
    'author': 'UIKick',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'data/uikick_data.xml',
        'views/templates.xml',
        'views/uikick_backend_views.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'odoo_uikick/static/src/css/style.css',
            'odoo_uikick/static/src/js/home.js',
            'odoo_uikick/static/src/js/detail.js',
        ],
    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
}
