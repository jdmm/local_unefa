# -*- coding: utf-8 -*-
##############################################################################
#
#    Programa realizado por, Jeison Pernía y Jonathan Reyes en el marco
#    del plan de estudios de la UNEFA, como TRABAJO ESPECIAL DE GRADO,
#    con el fin de optar al título de Ingeniero de Sistemas.
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

class unefa_conf_periodo_academico(osv.osv):
    _name = 'unefa.conf.periodo_academico'
    _rec_name='periodo_academico'
    
    _columns = {
        'periodo_academico': fields.char('Período académico', required=True,size=6),
        'fecha': fields.datetime('Fecha', select=True, readonly=True,),
    }
    
    _defaults = {
        'fecha': fields.datetime.now,
    }


#~ class unefa_conf_seccion(osv.osv):
    #~ _name = "unefa.conf.seccion"
    #~ _rec_name = "seccion"
    #~ 
    #~ _columns = {
        #~ 'seccion': fields.char('Sección', required=True),
        #~ 'fecha': fields.datetime('Fecha', select=True, readonly=True,),
    #~ }
    #~ 
    #~ _defaults = {
        #~ 'fecha': fields.datetime.now,
    #~ }

class cronograma_actividades_inscripcion(osv.osv):
    _name = 'unefa.cronograma_actividades_inscripcion'
    
    _rec_name = "actividad"
    
    _columns = {
        'actividad':fields.char('Actividad', required=True,),
        'activo':fields.boolean('Actividad Activa',)
    
    }
    
    _defaults={
        'activo':True,
        }
        
        
        
class cronograma_actividades_semestre(osv.osv):
    _name = 'unefa.cronograma_actividades_semestre'
    
    _rec_name = "actividad"
    
    _columns = {
        'actividad':fields.char('Actividad', required=True,),
        'activo':fields.boolean('Actividad Activa',)
    
    }
    
    _defaults={
        'activo':True,
        }

class unefa_responsable(osv.osv):
    _name = 'unefa.responsable'
    _rec_name = "responsable"
    
    _columns = {
        'responsable': fields.char(
                        'Responsable', 
                        required=True,
                        ),
        }
