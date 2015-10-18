# -*- coding: utf-8 -*-

{
    'name': 'Unefa Evaluación Profesores',
    'version': '1.0',
    'depends': ['base','unefa_configuracion','unefa_pensum','unefa_usuarios','unefa_planificacion_semestre','unefa_inscripcion'],
    'author': 'Nancy Castellanos',
    'category': 'Configuración',
    'description': """
            Módulo de supervisión y evaluación del personal docente
            """,
    'update_xml': [],
    "data" : [
        'views/supervision_clase_view.xml',
        'views/autoevaluacion_docente_view.xml',
        'security/group_unefa_admin/ir.model.access.csv',
        'security/group_unefa_coor/ir.model.access.csv',
        'security/group_unefa_est/ir.model.access.csv',
        'security/group_unefa_eval/ir.model.access.csv',
        'security/group_unefa_prof/ir.model.access.csv',
        'security/group_unefa_secret/ir.model.access.csv',
        ],
    'installable': True,
    'auto_install': False,
}

