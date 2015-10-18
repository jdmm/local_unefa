{
    'name':'Unefa Configuración',
    'version': '1.0',
    'depends': ['base_setup'],
    'author': 'IRP unefa (Comunidad Bachaco.ve)',
    'category': '',
    'description': """
    Nuestro primer modulo de estudiantes unefa
    """,
    'update_xml': [],
    "data" : [
        "views/menu_views.xml",
        "views/res_company.xml",
        "views/nucleo_views.xml",
        "views/carrera_views.xml",
        "views/coordinacion_views.xml",
        "views/pisos_views.xml",
        "views/aulas_views.xml",
        "security/unefa_roles.xml",
        "security/group_unefa_admin/ir.model.access.csv",
        "security/group_unefa_coor/ir.model.access.csv",
        "security/group_unefa_est/ir.model.access.csv",
        "security/group_unefa_eval/ir.model.access.csv",
        "security/group_unefa_prof/ir.model.access.csv",
        "security/group_unefa_secret/ir.model.access.csv",
        ],
    'installable': True,
    'auto_install': False,
}
