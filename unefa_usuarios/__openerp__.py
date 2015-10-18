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
    'name': 'Unefa Usuarios',
    'version': '1.0',
    'depends': ['base_setup','unefa_configuracion','unefa_pensum','web_fields_masks'],
    'author': 'Unefa Grupo N°2 Janeth camacho, ELvis Pacheco',
    'category': '',
    'description': """
    Modulo "usuarios" base para los sub-modulos: "unefa_estudiantes", "unefa_profesores", "unefa_secretariado" y "unefa_coordinadores".
    """,
    'update_xml': [],
    "data" : [
        'views/unefa_usuarios_view.xml',
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
