{
    'name': "Hospital",

    'author': "Hotkey Daria",
    'website': "https://www.hotkey.ua/",

    'depends': ['base'],

    'category': 'Customizations',
    'version': '15.0.1.0.0',

    'data': [
        'security/ir.model.access.csv',
        'views/hospital_menus.xml',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/diagnosis_views.xml',
        'views/patient_chart_views.xml',
    ],

    'installable': True,
    'auto_install': False,

    'images': [
        'static/description/icon.png',
    ],

    'price': 0,
    'currency': 'EUR',
    'license': ''

}
