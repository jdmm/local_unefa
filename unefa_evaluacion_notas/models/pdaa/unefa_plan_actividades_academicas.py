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


class plan_actividades_academicas(osv.osv):
    
    _name="unefa.plan.actividades.academicas"
    
    _columns={
    
    #~ de aqui en adelante son los llamados son los llamados a g1,g2,g3
    
    'carrera':fields.char("Carrera",size=40, required=False, readonly=True, help="grupo1"),#grupo1---
    'sede':fields.char("Sede",size=20,required=False, readonly=True, help="grupo1"),#grupo1---
    'regimen':fields.char("Turno",size=20,required=False, readonly=True, help="grupo1"),#grupo1---
    'aula':fields.integer("Aula",size=10, required=False, readonly=True, help="grupo1"),#grupo1---
    
    'ciProfesor':fields.integer("Cedula de Identidad",size=8, required=False, readonly=True, help="grupo2"),#grupo2---
    'nombreProfesor':fields.char("Nombre Profesor", size=40, required=False, readonly=True, help="grupo2"),#grupo2---
    'apellidoProfesor':fields.char("Apellido Profesor", size=40, required=False, readonly=True, help="grupo2"),#grupo2---
    'nombreCoordinador':fields.char("Nombre Coordinador",size=40, required=False, readonly=True, help="grupo2"),#grupo2---
    'emailProfesor':fields.char("Correo Profesor", size=100, required=False, readonly=True, help="grupo2"),#grupo2---
    'telefonoProfesor':fields.integer("Telefono Profesor", size=20, required=False, readonly=True, help="grupo2"),#grupo2---
    
    'seccion':fields.char("Seccion", size=10, required=False, readonly=True, help="grupo3"),#grupo3---
    'periodoAcademico':fields.char("Periodo Academico", size=10, required=False, readonly=True, help="grupo3"),#grupo3---
    
    #~ de aqui en adelante son requeridos por el grupo
    'dias':fields.integer('Dia a Evaluar',size=2,required=False, readonly=True,help='Dias a Evaluar'),
    
    'recibidoPor':fields.boolean('Recibido Por el Coordinador'),
    
    'state': fields.selection([
	('borrador', 'Borrador'),
	('asignado', 'Aprobado'),
	], 'Estado', readonly=True, copy=False, help="Este es es estado actual del plan actividades academicas.", select=True),
    
    'cortes_ids':fields.one2many('unefa.pdaa', 'pdaa_id', required=True),
    'plan_ids':fields.one2many('unefa.pde.pdaa', 'pde_pdaa_id', required=True),
    'referencias_ids':fields.one2many('unefa.referencias.pdaa', 'referencias_id', required=True),
    'fecha': fields.datetime ('Fecha', select=True, readonly=True),
    
    'semestre_id':fields.many2one('unefa.semestre','Semestre'),
    'materia_id':fields.many2one('unefa.materia','Materia'),
    'seccion_id':fields.many2one('unefa.conf.seccion','Seccion'),
}
    _defaults={

	'active':True,
        'fecha': fields.datetime.now,
    }
    
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
        res={}
	
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
	
	unefa_conf_periodo_academico_obj=self.pool.get('unefa.conf.periodo_academico')
	unefa_conf_periodo_academico_ids=unefa_conf_periodo_academico_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_conf_periodo_academico_datos=unefa_conf_periodo_academico_obj.browse(cr,uid,unefa_conf_periodo_academico_ids,context=context)
	
        res={
        #~ 'carrera':unefa_carrera_datos['nombre'],
	    'sede':"por solicitar",
	    'regimen':"por solicitar",
	    'aula':unefa_aulas_datos['numero'],
	    'ciProfesor':res_user_datos['cedula'],
	    'nombreProfesor':res_user_datos['name'],
	    'apellidoProfesor':"por solicitar",
	    'nombreCoordinador':"por solicitar",
	    'emailProfesor':res_user_datos['login'],
	    'telefonoProfesor':res_user_datos['telefono_local'],
	    'seccion':unefa_conf_seccion_datos['seccion'],
	    'periodoAcademico':unefa_conf_periodo_academico_datos['periodo_academico'],
	    'dias':666
        }
        return {'value':res}
        
    def create(self,cr,uid,vals,context=None):
        res=self.onchange_cargar_datos(cr, uid, [], context=None)
        res=res.values()
        res=res[0]
        h=super(plan_actividades_academicas, self).create(cr, uid, vals, context=context)
        self.write(cr,uid,h,res,context=context)
        return h
    

class unefa_pdaa(osv.osv):
    _name = "unefa.pdaa"
    
    _columns = {
    'pdaa_id': fields.many2one('unefa.pdaa_1', required=True),
    'semestre':fields.selection([('one','1'),('two','2'),('thre','3'),('for','4'),('five','5'),('six','6'),('seven','7'),('eigth','8'),('nine','9'),('ten','10')],'Semestre', help="Seleccionar semestre"),
    'fechaEntrega':fields.date("Fecha de Entrega",required=False,help="Fehca de entrega de la evaluacion"),
    'numeroUnidades':fields.selection([('one','1'),('two','2'),('thre','3'),('for','4'),('five','5')],'N° de Unidades',help='Unidades a Evaluar'),
    'objetivoUnidad':fields.selection([('one','1'),('two','2'),('thre','3'),('for','4'),('five','5')],'Obj. Unidad', help='Seleccionar objetivo de la unidad'),
    'contenido':fields.selection([('one','1'),('two','2'),('thre','3'),('for','4'),('five','5')],'Contenido', help='Seleccion de contenido de la materia'),
    'estrategiaEnsenanza':fields.selection([('one','1'),('two','2'),('thre','3'),('for','4'),('five','5')],'Estrategia de Enseñanza',help='Estrategia de la materia'),
    'tipos_evaluacion':fields.selection([('one','Taller'),('two','Examen'),('thre','Exposicion'),('for','Debate'),('five','Proyecto')],'Tipos de Evaluacion', help='Seleccion de tipos de evaluacion'),
 }

class unefa_pde_pdaa(osv.osv):
    _name = 'unefa.pde.pdaa'
    
    _columns = {
    'pde_pdaa_id': fields.many2one('unefa.pde_2', required=True),
    'actividades_evaluativas':fields.selection([('one','1'),('two','2'),('thre','3'),('for','4'),('five','5')],'Actividades Evaluativas', help='Actividades Evaluativas de la materia'),
    'porcentaje':fields.selection([('ten','10%'),('fifty','15%'),('twenty','20%'),('twenty five','25%')],'Porcentaje %',help="Maximo 25 porciento por corte"),
    'fecha_aplicacion':fields.date("Fecha de Aplicacion",help="Fecha de Evaluacion de la materia" ),
 }
 
class unefa_referencias_pdaa(osv.osv):
    _name = 'unefa.referencias.pdaa'
    
    _columns = {
    'referencias_id': fields.many2one('unefa.referencias_1', required=True),
    'referencia_bibliografica': fields.text('Bibliografica',size=500,required=False, help='Referencia Bibliografica de la materia'),
    'referencia_hemerografica':fields.text('Hemerografica',size=500,required=False,help='Referencia Hemerografica de la materia'),
    'referencia_electronicas':fields.text('Electronica',size=500,required=False,help='Referencia Electronicas de la materia'),
 }
