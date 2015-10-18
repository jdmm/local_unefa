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
from dateutil.relativedelta import *
import time

class acta_contrato_aprendizaje(osv.osv):
    
    _name="unefa.acta.contrato.aprendizaje"
    
    _columns={
    
    #~ de aqui en adelante son los llamados son los llamados a g1,g2,g3
    
    'nucleo':fields.char("Nucleo",size=20,required=False, readonly=True,help="grupo1"),#grupo1---
    'carrera':fields.char("Carrera",size=40, required=False, readonly=True,help="grupo1"),#grupo1---
    'division':fields.char("Division",size=20,required=False, readonly=True,help="grupo1"),#grupo1---
    'aula':fields.integer("Aula",size=10, required=False, readonly=True,help="grupo1"),#grupo1---
    'piso':fields.integer("Piso", size=10, required=False, readonly=True, help="grupo1"),#grupo1---
    
    'ciProfesor':fields.integer("Cedula de Identidad",size=8, required=False, readonly=True, help="grupo2"),#grupo2---
    'nombreProfesor':fields.char("Nombre Profesor", size=40, required=False, readonly=True, help="grupo2"),#grupo2---
    'apellidoProfesor':fields.char("Apellido Profesor", size=40, required=False, readonly=True, help="grupo2"),#grupo2---
    'nombreCoordinador':fields.char("Nombre Coordinador",size=40, required=False, readonly=True, help="grupo2"),#grupo2
    
    
    #~ de aqui en adelante son requeridos por el grupo
    'firmaDigitalEstudiante':fields.boolean('Firma Digital Estudiante'),
    'firmaDigitalProfesor':fields.boolean('Firma Digital Profesor'),
    'firmaDigitalCoordinador':fields.boolean('Firma Digital Coordinador'),
    'fecha': fields.datetime('Fecha', select=True, readonly=True),
    
    'state': fields.selection([
	('borrador', 'Borrador'),
	('asignado', 'Aprobado'),
	], 'Estado', readonly=True, copy=False, help="Este es es estado actual del acta e contrato de aprendizaje.", select=True),
    
    'cortes_ids':fields.one2many('unefa.acda', 'acda_id', required=True),
    
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
	
	unefa_nucleo_obj=self.pool.get('unefa.nucleo')
	unefa_nucleo_ids=unefa_nucleo_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_nucleo_datos=unefa_nucleo_obj.browse(cr,uid,unefa_nucleo_ids,context=context)
	
	unefa_carrera_obj=self.pool.get('unefa.carrera')
	unefa_carrera_ids=unefa_carrera_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_carrera_datos=unefa_carrera_obj.browse(cr,uid,unefa_carrera_ids,context=context)

	unefa_aulas_obj=self.pool.get('unefa.aulas')
	unefa_aulas_ids=unefa_aulas_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_aulas_datos=unefa_aulas_obj.browse(cr,uid,unefa_aulas_ids,context=context)
	
	unefa_pisos_obj=self.pool.get('unefa.pisos')
	unefa_pisos_ids=unefa_pisos_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_pisos_datos=unefa_pisos_obj.browse(cr,uid,unefa_pisos_ids,context=context)

	unefa_materia_obj=self.pool.get('unefa.materia')
	unefa_materia_ids=unefa_materia_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_materia_datos=unefa_materia_obj.browse(cr,uid,unefa_materia_ids,context=context)
	
        res_user_obj=self.pool.get('res.users')
        res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)

	unefa_conf_seccion_obj=self.pool.get('unefa.seccion')
	unefa_conf_seccion_ids=unefa_conf_seccion_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_conf_seccion_datos=unefa_conf_seccion_obj.browse(cr,uid,unefa_conf_seccion_ids,context=context)
	
	unefa_semestre_obj=self.pool.get('unefa.semestre')
	unefa_semestre_ids=unefa_semestre_obj.search(cr,uid,[('id','=',uid)],context=context)
	unefa_semestre_datos=unefa_semestre_obj.browse(cr,uid,unefa_semestre_ids,context=context)
        
        res={
            
	    'nucleo':unefa_nucleo_datos['nombre'],
	    #~ 'carrera':unefa_carrera_datos['nombre'],
	    'division':"por solicitar",
	    'aula':unefa_aulas_datos['numero'],
	    'piso':unefa_pisos_datos['numero'],
	    'ciProfesor':res_user_datos['cedula'],
	    'materia':unefa_materia_datos['materia'],
	    'nombreProfesor':res_user_datos['name'],
	    'apellidoProfesor':"por solicitar",
	    'nombreCoordinador':"por solicitar",
	    'seccion':unefa_conf_seccion_datos['seccion'],
	    'semestre':unefa_semestre_datos['nombre'],
        }
        return {'value':res}
        
    def create(self,cr,uid,vals,context=None):
        res=self.onchange_cargar_datos(cr, uid, [], context=None)
        res=res.values()
        res=res[0]
        h=super(acta_contrato_aprendizaje, self).create(cr, uid, vals, context=context)
        self.write(cr,uid,h,res,context=context)
        return h
	
    def onchange_lista_estudiantes_prueba(self, cr, uid, ids, context=None):
        res={}
        lista_estudiantes_obj=self.pool.get('unefa.lista_estudiantes_prueba')
        lista_estudiantes_ids=lista_estudiantes_obj.search(cr,uid,[('activo','=','True')],context=context)
        lista_estudiantes_datos=lista_estudiantes_obj.browse(cr,uid,lista_estudiantes_ids,context=context)
        lista_estudiantes=[]
        for i in lista_estudiantes_datos:
            lista_estudiantes.append([0,False,{'nombreEstudiante_id':i.id }])
        res={
            'cortes_ids':lista_estudiantes,
            }
        return {'value':res}
	
    

class unefa_acda(osv.osv):
    _name = "unefa.acda"
    
    _columns = {
    'acda_id': fields.many2one('unefa.acda_1', required=True),
    'nombreEstudiante_id':fields.many2one('unefa.lista_estudiantes_prueba','Estudiante',readonly=True,),
    'apellidoEstudiante':fields.char("Apellido", size=40, required=False,readonly=True, help="grupo2"),#grupo2---
    'ciEstudiante':fields.integer("Cedula de Identidad", size=8, required=False,readonly=True, help="grupo2"),#grupo2---
    #~ 'firmaDigitalEstudiante':fields.boolean('Firma Digital Estudiante'),
        
 }
 
    

