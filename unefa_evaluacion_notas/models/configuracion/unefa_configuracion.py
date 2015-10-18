# -*- coding: utf-8 -*-
##############################################################################
#
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
#
from openerp.osv import fields, osv
from datetime import datetime, timedelta
import time

class lista_cortes_semestre(osv.osv):
    _name = 'unefa.lista_cortes_semestre'
    
    _rec_name = "actividad"
    
    _columns = {
        'actividad':fields.char('Actividad', required=True,),
        'activo':fields.boolean('Actividad Activa',)
    
    }
    
    _defaults={
        'activo':True,
        }

class lista_estudiantes_prueba(osv.osv):
    _name = 'unefa.lista_estudiantes_prueba'
    
    _rec_name = "actividad"
    
    _columns = {
        'actividad':fields.char('Actividad', required=True,),
        'activo':fields.boolean('Actividad Activa',)
    
    }
    
    _defaults={
        'activo':True,
        }
