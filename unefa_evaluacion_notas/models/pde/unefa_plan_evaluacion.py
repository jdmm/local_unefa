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
#~ import sys
#~ reload(sys)
#~ sys.setdefaultencoding('UTF8')

class plan_evaluacion(osv.osv):
    
    _name="unefa.plan.evaluacion"
    #~ _rec_name ='corte_id'
    
    _columns={
	#~ de aqui en adelante son los llamados son los llamados a g1,g2,g3
	
	'nucleo':fields.char("Nucleo",size=20,required=False, readonly=True, help="grupo1"),#grupo1 ---
	'carrera':fields.char("Carrera",size=40, required=False, readonly=True, help="grupo1"),#grupo1 ---
	'division':fields.char("Division",size=20,required=False, readonly=True, help="grupo1"),#grupo1 ---
	'sede':fields.char("Sede",size=20,required=False, readonly=True, help="grupo1"),#grupo1 ---
	'regimen':fields.char("Turno",size=20,required=False, readonly=True, help="grupo1"),#grupo1 ---turno
	'aula':fields.integer("Aula",size=10, required=False, readonly=True, help="grupo1"),#grupo1 ---
	
	'ciProfesor':fields.integer("Cedula de Identidad",size=8, required=False, readonly=True, help="grupo2"),#grupo2 ---
	'materia':fields.char("Materia", size=20, required=False, readonly=True, help="grupo2"),#grupo2 ---
	'materia_id':fields.many2one('unefa.materia','Materia'),
	'codigoMateria':fields.char("Codigo Materia", size=10, required=False, readonly=True, help="grupo2"),#grupo2---
	'nombreCoordinador':fields.char("Nombre Coordinador",size=40, required=False, readonly=True, help="grupo2"),#grupo2 ---
	
	'seccion':fields.char("Seccion", size=10, required=False, readonly=True, help="grupo3"),#grupo3---
	'seccion_id':fields.many2one('unefa.seccion','Seccion'),
	'semestre':fields.integer("Semestre", size=2, required=False, readonly=True, help="grupo3"),#grupo3 ---termino
	'semestre_id':fields.many2one('unefa.semestre','Semestre'),
	'horasSemanales':fields.integer("Horas Semanales", size=2, required=False, readonly=True, help="grupo3"),#grupo3 ---
	'numeroEstudiantesInscritos':fields.integer("Numero Estudiantes Inscritos", size=2, required=False, readonly=True, help="grupo3"),#grupo3 ---
	'periodoAcademico':fields.char("Periodo Academico", size=10, required=False, readonly=True, help="grupo3"),#grupo3 ---
	
	'corte_id': fields.one2many('unefa.corte.pde','corte_pde_id','Corte',required=True),

	'fecha': fields.datetime('Fecha', select=True, readonly=True),
	
	'state': fields.selection([
            ('borrador', 'Borrador'),
            ('aprobado', 'Aprobado'),
            ],'Estado', readonly=True, copy=False, help="Este es es estado actual del plan de Evaluacion.", select=True),
    
    }
    
    _defaults={
    
        'active':True,
        'fecha': fields.datetime.now,
    }
    
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
	res={}

	unefa_nucleo_obj=self.pool.get('unefa.nucleo')
	unefa_nucleo_ids=unefa_nucleo_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_nucleo_datos=unefa_nucleo_obj.browse(cr,uid,unefa_nucleo_ids,context=context)
    
	unefa_carrera_obj=self.pool.get('unefa.carrera')
	unefa_carrera_ids=unefa_carrera_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_carrera_datos=unefa_carrera_obj.browse(cr,uid,unefa_carrera_ids,context=context)	

	unefa_aulas_obj=self.pool.get('unefa.aulas')
	unefa_aulas_ids=unefa_aulas_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_aulas_datos=unefa_aulas_obj.browse(cr,uid,unefa_aulas_ids,context=context)
    
	res_user_obj=self.pool.get('res.users')
	res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
	res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
	
	unefa_conf_seccion_obj=self.pool.get('unefa.seccion')
	unefa_conf_seccion_ids=unefa_conf_seccion_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_conf_seccion_datos=unefa_conf_seccion_obj.browse(cr,uid,unefa_conf_seccion_ids,context=context)
	
	unefa_semestre_obj=self.pool.get('unefa.semestre')
	unefa_semestre_ids=unefa_semestre_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_semestre_datos=unefa_semestre_obj.browse(cr,uid,unefa_semestre_ids,context=context)
	
	unefa_materia_obj=self.pool.get('unefa.materia')
	unefa_materia_ids=unefa_materia_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_materia_datos=unefa_materia_obj.browse(cr,uid,unefa_materia_ids,context=context)
	
	unefa_conf_periodo_academico_obj=self.pool.get('unefa.conf.periodo_academico')
	unefa_conf_periodo_academico_ids=unefa_conf_periodo_academico_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_conf_periodo_academico_datos=unefa_conf_periodo_academico_obj.browse(cr,uid,unefa_conf_periodo_academico_ids,context=context)
	    
	res={
            
	    'nucleo':unefa_nucleo_datos['nombre'],
	    #~ 'carrera':unefa_carrera_datos['nombre'],
	    'division':"por solicitar",
	    'sede':"por solicitar",
	    'regimen':"por solicitar",
	    'aula':unefa_aulas_datos['numero'],
	    'ciProfesor':res_user_datos['cedula'],
	    'seccion':unefa_conf_seccion_datos['seccion'],
	    'semestre':unefa_semestre_datos['nombre'],
	    'materia':unefa_materia_datos['materia'],
	    'codigoMateria':unefa_materia_datos['codigo'],
	    'nombreCoordinador':"por solicitar",
	    'horasSemanales':unefa_materia_datos['teoria'],
	    'numeroEstudiantesInscritos':0,
	    'periodoAcademico':unefa_conf_periodo_academico_datos['periodo_academico'],
        }
	
        return {'value':res}
        
    def create(self,cr,uid,vals,context=None):
        res=self.onchange_cargar_datos(cr, uid, [], context=None)
        res=res.values()
        res=res[0]
        h=super(plan_evaluacion, self).create(cr, uid, vals, context=context)
        self.write(cr,uid,h,res,context=context)
        return h
	
    def aprobar_pde(self, cr, uid, ids, context=None):
        return True
        
    def generar_pde(self, cr, uid, ids, context=None):
        return True



 
