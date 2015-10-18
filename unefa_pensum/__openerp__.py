# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Unefa Pensum',
    'version': '1.0',
    'depends': ['base_setup','unefa_configuracion'],
    'author': 'Unefa Grupo N°2 Janeth camacho, ELvis Pacheco',
    'category': '',
    'description': """
    Modulo "Pensum" : "Materias, codigos, unidades de credito, prelacion y contenidos programatico de materias".
    """,
    'update_xml': [],
    "data" : [
        'data/unefa_pensum_data.xml',
        'views/unefa_materia_view.xml',
        'views/unefa_semestre_view.xml',
        'views/unefa_pensum_view.xml',
        'views/unefa_contenido_view.xml',
        'security/per_admin_sist/ir.model.access.csv',
        'security/per_coordinador/ir.model.access.csv',
        'security/per_estudiantes/ir.model.access.csv',
        'security/per_evaluador/ir.model.access.csv',
        'security/per_profesores/ir.model.access.csv',
        'security/per_secretaria/ir.model.access.csv',
    
        ],
    'installable': True,
    'auto_install': False,
}
