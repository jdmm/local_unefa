# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Business Applications
#    Copyright (C) 2004-2012 OpenERP S.A. (<http://openerp.com>).
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
from openerp.osv import fields, osv
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import * 
from openerp.osv.expression import get_unaccent_wrapper
from openerp.tools.translate import _

class usuarios(osv.osv):
    _name='res.users'
    _inherit = 'res.users'
    
  
      
    _columns = {
    'is_estudiante':fields.boolean('Estudiante'),
    'is_profesor':fields.boolean('Profesor'),
    'is_coordinador':fields.boolean('Coordinador'),
    'is_secretaria':fields.boolean('Secretaria'),
    'is_evaluador':fields.boolean('Evaluador'),
    'nacionalidad':fields.selection([('E','Extranjero'),('V','Venezolano')],'Nacionalidad' ),
    'cedula':fields.char('Cédula', required=False, size=9),
    'telefono_local':fields.char('Telefono Local'),
    'telefono':fields.char('Telefono Celular'),
    'fecha':fields.date('Fecha de Nacimiento'),
    'sexo':fields.selection([('masculino','Masculino'),('femenino','Femenino')],'Sexo'),
    'estado_civil':fields.selection([('soltero','Soltero'),('casado','Casado'),('divorciado','Divorciado'),('viudo','Viudo')],'Estado Civil'),
    'carrera_id':fields.many2one('unefa.carrera','Carrera', required=True),
    'regimen':fields.selection([('N','Nocturno'),('D','Diurno')],'Régimen', required=True),
    'pensum_id': fields.many2one('unefa.pensum','Pensum', required=True),
    }



    _sql_constraints = [
        ('cedula_uniq', 'unique(cedula)', 'El Número de C.I. !YA EXISTE¡¡¡'),
    ]
       
    


   
  
    
    
 
