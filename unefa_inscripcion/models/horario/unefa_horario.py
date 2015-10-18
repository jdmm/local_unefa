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

class unefa_horario(osv.osv):
    _name = 'unefa.horario'
    #~ _rec_name = ""
    
    _columns = {
        'carrera_id': fields.many2one('unefa.carrera', 'Carrera',),
        'periodo_id': fields.many2one('unefa.conf.periodo_academico',
                    'Periodo Académico',
                    required=True,
                    ),
        'semestre_id': fields.many2one('unefa.semestre', 'Semestre',),
        'aula_id': fields.many2one('unefa.aulas', 'Aula',),
        'fecha': fields.datetime('Fecha', select=True, readonly=True,),
        'observaciones': fields.text('Observaciones'),
        'horarios_ids': fields.one2many('unefa.horarios_master', 'horario_id', required=True),
        'state': fields.selection([
            ('borrador', 'Borrador'),
            ('aprobado', 'Aprobado'),
            ],'Estado', readonly=True, copy=False, help="Este es es estado actual de la oferta académica.", select=True),
    }
    
    _defaults = {
        'fecha': fields.datetime.now,
    }
    
    def aprobar_horario(self, cr, uid, ids, context=None):
        return True
        
    def generar_horario(self, cr, uid, ids, context=None):
        return True
        

class unefa_horarios_master(osv.osv):
    _name = 'unefa.horarios_master'
    
    _columns = {
        'horario_id': fields.many2one('unefa.horario','Horario'),
        'asignatura_id': fields.many2one('unefa.materia', 'Asignatura',),
        'profesor_id': fields.many2one('unefa.profesores', 'Profesor',),
        'hora_inicio': fields.char('Hora Inicio',),
        'hora_final': fields.char('Hora Final',),
        
    }
