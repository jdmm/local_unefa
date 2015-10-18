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


class unefa_seguimiento(osv.osv):
    _name="unefa.seguimiento"
    
    _columns={
        'estudiante_id': fields.many2one('res.users','Cedula'),
        'nombre_estudiante': fields.many2one('res.users','Nombre'),
        'apellido_estudiante': fields.many2one('res.users','Apellido'),
        'pensum_id': fields.many2one('unefa.pensum','Pensum'),
        'carrera_id': fields.many2one('unefa.carrera','Carrera'),
        'seg_notas_ids': fields.one2many('unefa.seg_notas','seguimiento_id',''),
    }
    
    _defaults={
    }
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
        #~ res={}
        #~ res_user_obj=self.pool.get('res.users')
        #~ res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
        #~ 
        #~ unefa_pensum_obj=self.pool.get('unefa.pensum')
        #~ unefa_pensum_ids=unefa_materia_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_pensum_datos=unefa_pensum_obj.browse(cr,uid,unefa_pensum_ids,context=context
        #~ 
        #~ carrera_obj=self.pool.get('unefa.carrera')
        #~ carrera_ids=carrera_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ carrera_datos=carrera_obj.browse(cr,uid,carrera_ids,context=context)
        #~ 
        #~ res={
            #~ 'estudiante_id':res_user_datos['name'],
            #~ 'nombre_estudiante':res_user_datos['name'],
            #~ 'apellido_estudiante':res_user_datos['name'],
            #~ 'pensum_id':unefa_pensum_datos['nombre'],
            #~ 'carrera_id':carrera_datos['nombre'],
        #~ }
        #~ return {'value':res}
        return True

class unefa_seg_notas(osv.osv):
    _name="unefa.seg_notas"
    
    _columns={
        'seguimiento_id': fields.many2one('unefa.seguimiento','Seguimiento'),
        'nombre_profesor': fields.many2one('res.users','Nombre del Profesor'),
        'apellido_profesor': fields.many2one('res.users','Apellido del Profesor'),
        'periodo_id': fields.many2one('unefa.conf.periodo_academico','Periodo'),
        'semestre_id': fields.many2one('unefa.semestre','Semestre'),
        'materia_id': fields.many2one('unefa.materia','Materia'),
        'codigo': fields.many2one('unefa.materia','Codigo de Materia'),
        'credito': fields.many2one('unefa.materia','UC'),
        'seccion_id': fields.many2one('unefa.seccion','Seccion'),
        'nota_final_id': fields.many2one('unefa.evaluacion.continua','Nota'),
        'nota_rep_id': fields.many2one('unefa.notas_rep','Nota de Reparacion'),
        'observaciones':fields.text('Observaciones',size=300),
        'correlativo':fields.char('Correlativo',size=10),
    }
    
    _defaults={
    }
    
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
        #~ res={}
        #~ res_user_obj=self.pool.get('res.users')
        #~ res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
        #~ 
        #~ unefa_conf_periodo_academico_obj=self.pool.get('unefa.conf.periodo_academico')
        #~ unefa_conf_periodo_academico_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_conf_periodo_academico_datos=res_user_obj.browse(cr,uid,unefa_conf_periodo_academico_ids,context=context)
        #~ 
        #~ unefa_semestre_obj=self.pool.get('unefa.semestre')
        #~ unefa_semestre_ids=unefa_semestre.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_semestre_datos=unefa_semestre_obj.browse(cr,uid,unefa_semestre_ids,context=context)
        #~ 
        #~ unefa_materia_obj=self.pool.get('unefa.materia')
        #~ unefa_materia_ids=unefa_materia_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_materia_datos=unefa_materia_obj.browse(cr,uid,unefa_materia_ids,context=context
        #~ 
        #~ unefa_conf_seccion_obj=self.pool.get('unefa.conf.seccion')
        #~ unefa_conf_seccion_ids=unefa_conf_seccion_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_conf_seccion_datos=unefa_conf_seccion_obj.browse(cr,uid,unefa_conf_seccion_ids,context=context)
        #~ 
        #~ unefa_cdn_nuevo_obj=self.pool.get('unefa.cdn_nuevo')
        #~ unefa_cdn_nuevo_ids=unefa_cdn_nuevo_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_cdn_nuevo_datos=unefa_cdn_nuevo_obj.browse(cr,uid,unefa_cdn_nuevo_ids,context=context)
        #~ 
        #~ unefa_notas_rep_obj=self.pool.get('unefa.notas_rep')
        #~ unefa_notas_rep_ids=unefa_conf_seccion_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ unefa_notas_rep_datos=unefa_notas_rep_obj.browse(cr,uid,unefa_notas_rep_ids,context=context)
        #~ 
        #~ res={
            #~ 'nombre_profesor':res_user_datos['name'],
            #~ 'apellido_profesor':res_user_datos['name'],
            #~ 'periodo_id':unefa_conf_periodo_academico_datos['periodo_academico'],
            #~ 'semestre_id':unefa_semestre_datos['nombre'],
            #~ 'materia_id':unefa_materia_datos['materia'],
            #~ 'codigo':unefa_materia_datos['codigo'],            
            #~ 'credito':unefa_materia_datos['uc'],
            #~ 'seccion_id':unefa_conf_seccion_datos['seccion'],
            #~ 'nota_final_id':unefa_cdn_nuevo['nota'],
            #~ 'nota_rep_id':unefa_notas_rep['nota_rep'],
        #~ }
        #~ return {'value':res}
        return True
        
    def generar_observaciones():
        return True
