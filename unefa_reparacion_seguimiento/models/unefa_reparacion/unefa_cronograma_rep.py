# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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
from datetime import datetime, timedelta
import time

class unefa_cronograma_rep(osv.osv):
    
    _name="unefa.cronograma_rep"

    _columns={
        'cronograma_actividades_id': fields.many2one('unefa.cronograma_actividad','Cronograma de Actividades'), 
        'carrera_id': fields.many2one('unefa.carrera','Carrera'),
        'regimen_id': fields.many2one('unefa.regimen','Regimen'),
        'periodo_id': fields.many2one('unefa.conf.periodo_academico','Periodo Académico'),
        'crono_prueba_ids': fields.one2many('unefa.crono_prueba','cronograma_rep_id',''),
    }
    
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
        
        #~ res={}
        #~ 
        #~ carrera_obj=self.pool.get('unefa.carrera')
        #~ carrera_ids=carrera_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ carrera_datos=carrera_obj.browse(cr,uid,carrera_ids,context=context)
        #~ 
        #~ unefa_conf_periodo_academico_obj=self.pool.get('unefa.conf.periodo_academico')
        #~ unefa_conf_periodo_academico_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_conf_periodo_academico_datos=res_user_obj.browse(cr,uid,unefa_conf_periodo_academico_ids,context=context)
        #~ 
        #~ res_user_obj=self.pool.get('res.users')
        #~ res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
        #~ 
        #~ res={
            #~ 'carrera_id':carrera_datos['nombre'],
            #~ 'regimen_id':
            #~ 'periodo_id':unefa_conf_periodo_academico_datos['periodo_academico'],
        #~ 
        #~ }
        #~ return {'value':res}
        return True
        
    def onchange_filtrar_datos(self, cr, uid, ids, context=None):
        return True
    
    
class unefa_crono_prueba(osv.osv):
    _name="unefa.crono_prueba"
    
    _columns={
        'cronograma_rep_id': fields.many2one('unefa.cronograma_rep','Cronograma'),
        'profesor_id': fields.many2one('unefa.profesor','Profesor'),
        'semestre_id': fields.many2one('unefa.semestre','Semestre'),
        'seccion_id': fields.many2one('unefa.conf.seccion','Seccion'),
        'materia_id': fields.many2one('unefa.materia','Materia'),
        'pensum_id': fields.many2one('unefa.pensum','Pensum'),
        'fecha_rep':fields.datetime('Fecha',required=True),
        'hora_rep':fields.char('Hora'),
        'observaciones':fields.text('Observaciones',size=300),
    }
    
    def onchange_verificar_estudiantes_reprobados(self, cr, uid, ids, context=None):
            #filtrar seccion
        return True
    
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
        #~ res={}
        #~ res_user_obj=self.pool.get('res.users')
        #~ res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
        #~ 
        #~ unefa_semestre_obj=self.pool.get('unefa.semestre')
        #~ unefa_semestre_ids=unefa_semestre.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_semestre_datos=unefa_semestre_obj.browse(cr,uid,unefa_semestre_ids,context=context)
        #~ 
        #~ unefa_conf_seccion_obj=self.pool.get('unefa.conf.seccion')
        #~ unefa_conf_seccion_ids=unefa_conf_seccion_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_conf_seccion_datos=unefa_conf_seccion_obj.browse(cr,uid,unefa_conf_seccion_ids,context=context)
        #~ 
        #~ unefa_materia_obj=self.pool.get('unefa.materia')
        #~ unefa_materia_ids=unefa_materia_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_materia_datos=unefa_materia_obj.browse(cr,uid,unefa_materia_ids,context=context
        #~ 
        #~ unefa_pensum_obj=self.pool.get('unefa.pensum')
        #~ unefa_pensum_ids=unefa_pensum_obj.search(cr,uid,[('id','=',uid)]pensum,context=context)
        #~ unefa_pensum_datos=unefa_materia_obj.browse(cr,uid,unefa_pensum_ids,context=context) 
        #~ 
        #~ res={
            #~ 'nombre_profesor':res_user_datos['name'],
            #~ 'apellido_profesor':res_user_datos['name'],
            #~ 'semestre_id':unefa_semestre_datos['nombre'],
            #~ 'seccion_id':unefa_conf_seccion_datos['seccion'],
            #~ 'materia_id':unefa_materia_datos['materia'],
            #~ 'pensum_id':unefa_pensum_datos['nombre'],
        #~ }
        #~ return {'value':res}

        return True
        
    def onchange_validar_fecha(self, cr, uid, ids, context=None):
        return True
