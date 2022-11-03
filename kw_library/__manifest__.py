{
    'name': "Library",

    'summary': '',

    'author': 'Hotkey Daria',
    'website': 'https://www.hotkey.ua/',

    'category': 'Customizations',
    'version': '15.0.1.0.0',

    'depends': [

    ],

    'external_dependencies': {'python': ['pyisbn'], },

    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml'
        'views/menu.xml',
        'views/kw_book.xml',
        'views/kw_author.xml',
        'views/kw_category.xml',
        'views/kw_book_instance.xml',
    ],

    'demo': [

    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/cover.png',
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',
    'license': ''

}
