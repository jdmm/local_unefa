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

class unefa_oferta_academica(osv.osv):
    _name = 'unefa.oferta_academica'
    
    _columns = {
        'carrera_id': fields.many2one('unefa.carrera', 'Carrera',),
        'fecha': fields.datetime('Fecha', select=True, readonly=True),
        'periodo_id': fields.many2one('unefa.conf.periodo_academico',
                    'Período Académico',
                    required=True,
                    ),
        'observaciones': fields.text('Observaciones'),
        'cronograma_oferta_ids': fields.one2many('unefa.cronograma_oferta_academica', 'cronograma_oferta_id', required=True),
        'state': fields.selection([
            ('borrador', 'Borrador'),
            ('aprobado', 'Aprobado'),
            ],'Estado', readonly=True, copy=False, help="Este es es estado actual de la oferta académica.", select=True),
    }
    
    _defaults = {
        'fecha': fields.datetime.now,
        'state': 'borrador',
    }
    
    def aprobar_oferta_academica(self, cr, uid, ids, context=None):
        return True
    
    def cargar_oferta_academica(self, cr, uid, ids,periodo_id, context=None):
        inscripcion_obj=self.pool.get('unefa.inscripcion')
        inscripcion_ids=inscripcion_obj.search(cr,uid,[('periodo_id','=',periodo_id),('state','=','preinscrito'),],context=context)
        inscripcion_asignatura_obj=self.pool.get('unefa.inscripcion_asignatura')
        inscripcion_asignatura_ids=inscripcion_asignatura_obj.search(cr,uid,[('inscripcion_asiganatura_id','=',inscripcion_ids)],context=context)
        inscripcion_asignatura_datos=inscripcion_asignatura_obj.browse(cr,uid,inscripcion_asignatura_ids,context=context)
        materia_obj=self.pool.get('unefa.materia')
        materia_ids=materia_obj.search(cr,uid,[],context=context)
        materia_datos=materia_obj.browse(cr,uid,materia_ids,context=context)
        list_materia=[]
        list_oferta=[]
        for m in materia_ids:
            for i in inscripcion_asignatura_datos:
                if m==int(i.asignatura_id):
                    list_materia.append(m)
        list_materia_fil=list(set(list_materia))
        for ids in list_materia_fil:
             list_oferta.append([0,False,{'asignatura_id':ids,'alumnos_inscritos':list_materia.count(ids) }])
        res={
            'cronograma_oferta_ids':list_oferta,
            }
        return {'value':res}
    
    
class cronograma_oferta_academica(osv.osv):
    _name = "unefa.cronograma_oferta_academica"
    
    def get_select_porcentaje(desde,hasta):
        porc=[]
        for i in range(desde,hasta):
            porc.append((str(i),str(i)))
        return porc

    
    _columns = {
        'cronograma_oferta_id': fields.many2one('unefa.oferta_academica', 'Oferta académica', required=True),
        'asignatura_id': fields.many2one('unefa.materia', 'Asignatura',),
        'alumnos_inscritos': fields.integer('Alumnos Preinscritos', readonly=True,),
        'cantidad_secciones': fields.selection(get_select_porcentaje(1,11),'Cantidad Secciones', 
                                        readonly=False, copy=False, 
                                        required=True,
                                        help="Esta es la cantidad de secciones para habilitar.", select=True),
        
    }
