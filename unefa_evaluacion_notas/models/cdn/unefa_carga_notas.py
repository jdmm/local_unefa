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
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

class unefa_carga_notas(osv.osv):
    
    _name="unefa.carga.notas"
    #~ _rec_name = 'corte'
    
    _columns={
    #~ de aqui en adelante son los llamados son los llamados a g1,g2,g3
	
	'nucleo':fields.char("Nucleo",size=20,required=False, readonly=True, help="grupo1"),#grupo1---
	'carrera':fields.char("Carrera",size=40, required=False, readonly=True, help="grupo1"),#grupo1---
	'division':fields.char("Division",size=20,required=False, readonly=True, help="grupo1"),#grupo1---
	'aula':fields.integer("Aula",size=10, required=False, readonly=True, help="grupo1"),#grupo1---
	'piso':fields.integer("Piso", size=10, required=False, readonly=True,  help="grupo1"),#grupo1---
	
	'ciProfesor':fields.integer("Cedula de Identidad",size=8, required=False, readonly=True, help="grupo2"),#grupo2---
	'materia':fields.char("Materia", size=20, required=False, readonly=True, help="grupo2"),#grupo2 ---aginatura
	'materia_id':fields.many2one('unefa.materia','Materia'),
	'nombreProfesor':fields.char("Nombre Profesor", size=40, required=False, readonly=True, help="grupo2"),#grupo2---
	'apellidoProfesor':fields.char("Apellido Profesor", size=40, required=False, readonly=True, help="grupo2"),#grupo2---
	'nombreEstudiante':fields.char("Nombre Estudiante", size=40, required=False, readonly=True, help="grupo2"),#grupo2---
	'apellidoEstudiante':fields.char("Apellido Estudiante", size=40, required=False, readonly=True, help="grupo2"),#grupo2---
	'ciEstudiante':fields.integer("Cedula Estudiante", size=8, required=False, readonly=True, help="grupo2"),#grupo2---
	
	'seccion':fields.char("Seccion", size=10, required=False, readonly=True, help="grupo3"),#grupo3---
	'seccion_id':fields.many2one('unefa.conf.seccion','Seccion'),
	'semestre':fields.selection([('one','1'),('two','2'),('thre','3'),('for','4'),('five','5'),('five','5'),('six','6'),('seven','7'),('eight','8'),('nine','9'),('then','10'),('eleven','11'),('twelve','12'),('thirty','13'),('fourty','14'),('fivety','15'),('sixty','16'),('seventy','17'),('eigty','18'),('ninety','19'),('twenty','20')],'Semestre', help='Selecionar nota'), #grupo3---
	'semestre_id':fields.many2one('unefa.semestre','Semestre'),
	
	#~ 'corte':fields.selection([('1','1'),('2','2'),('3','3'),('4','4')],'corte', help="Seleccionar corte"),
	#~ 
	#~ de aqui en adelante son requeridos por el grupo
       
	'firmaDigitalProfesor':fields.boolean('Firma Digital Profesor'),
	'firmaDigitalCoordinador':fields.boolean('Firma Digital Coordinador'),
	'state': fields.selection([
            ('borrador', 'Borrador'),
            ('asignado', 'Aprobado'),
            ], 'Estado', readonly=True, copy=False, help="Este es es estado actual de Carga de Notas.", select=True),
	
	'cortes_ids':fields.one2many('unefa.cdn', 'cdn_id', 'Cortes', required=True),
    
    #~ 'corte_id': fields.many2one('unefa.lista_cortes_semestre','Corte',readonly=True,),
    
	'fecha': fields.datetime('Fecha', select=True, readonly=True),
    
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

        #~ res_company_obj=self.pool.get("res.company")
        #~ res_company_ids=res_company_obj.search(cr, uid, [("id","=",uid)], context=context)
        #~ res_company_datos=res_company_obj.browse(cr, uid, res_company_ids, context=context)
        #~ 
        #~ res_partner_obj=self.pool.get("res.partner")
        #~ res_partner_ids=res_partner_obj.search(cr, uid, [("id","=",res_company_ids)], context=context)
        #~ res_partner_datos=res_partner_obj.browse(cr, uid, res_partner_ids, context=context)
	
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
	    'nombreEstudiante':res_user_datos['name'],
	    'apellidoEstudiante':"por solicitar",
	    'ciEstudiante':res_user_datos['cedula'],
	    'seccion':unefa_conf_seccion_datos['seccion'],
	    'semestre':unefa_semestre_datos['nombre'],
            #~ 'nucleo':res_company_datos['name'],
            #~ 'carrera':res_partner_datos['name'],
        }
        return {'value':res}
        
    def onchange_lista_cortes_semestre(self, cr, uid, ids, context=None):
        res={}
        lista_cortes_obj=self.pool.get('unefa.lista_cortes_semestre')
        lista_cortes_ids=lista_cortes_obj.search(cr,uid,[('activo','=','True')],context=context)
        lista_cortes_datos=lista_cortes_obj.browse(cr,uid,lista_cortes_ids,context=context)
        lista_cortes=[]
        for i in lista_cortes_datos:
            lista_cortes.append([0,False,{'corte_id':i.id }]) 
        res={
            'cortes_ids':lista_cortes,
            }
        return {'value':res}
        
    def create(self,cr,uid,vals,context=None):
        res=self.onchange_cargar_datos(cr, uid, [], context=None)
        res=res.values()
        res=res[0]
        h=super(carga_notas, self).create(cr, uid, vals, context=context)
        self.write(cr,uid,h,res,context=context)
        return h
	



    

 
