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
from datetime import datetime, date, time, timedelta
import time

class unefa_inscripcion(osv.osv):
    _name = 'unefa.inscripcion'
    
    def default_usuarios(self, cr, uid, ids, context=None):
        res_user_obj=self.pool.get('res.users')
        res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
        if res_user_datos['is_coordinador']!=True:
            return uid
    
    def total_uc(self, cr, uid, ids, name, args, context=None):
        res={}
        total=0
        for i in self.browse(cr,uid,ids):
            for n in i.inscripcion_asiganatura_ids:
                total+=n.unidades_creditos
            res[i.id]=total
        return res
    
    
    _columns = {
        'estudiante':fields.many2one('unefa.estudiantes',
                    'Nombre y Apellido',
                    required=True,
                    ),
        'periodo_id': fields.many2one('unefa.conf.periodo_academico',
                    'Periodo Académico',
                    required=True,
                    readonly=True
                    ),
        'fecha_inscripcion': fields.datetime('Fecha de inscripción', select=True, readonly=True,),
        'carrera_id': fields.many2one('unefa.carrera', 'Carrera', readonly=True),
        'pensum_id': fields.many2one('unefa.pensum', 'Pensum', readonly=True),
        'regimen':fields.selection([('N','Nocturno'),('D','Diurno')],'Régimen', required=True),
        'observaciones': fields.text('Observaciones'),
        'inscripcion_asiganatura_ids': fields.one2many('unefa.inscripcion_asignatura', 'inscripcion_asiganatura_id', required=True),
        'state': fields.selection([
            ('borrador', 'Borrador'),
            ('preinscrito', 'Preinscrito'),
            ('cancelar', 'Cancelar'),
            ('inscrito', 'Inscrito'),
            ], 'Estado', readonly=True, copy=False, help="Este es es estado actual de la inscripción.", select=True),
        'total_uc': fields.function(total_uc, string='Total UC',type="integer"),
    }
    
    _defaults = {
        'fecha_inscripcion': fields.datetime.now,
        'state':'borrador',
        'create_uid':default_usuarios,
     
    }
    
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
        res={}
        readonly={}
        res_user_obj=self.pool.get('res.users')
        res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
        
        estudiantes_obj=self.pool.get('unefa.estudiantes')
        estudiantes_ids=estudiantes_obj.search(cr,uid,[('user_id','=',res_user_ids)],context=context)
        estudiantes_datos=estudiantes_obj.browse(cr,uid,estudiantes_ids,context=context)
        
        if res_user_datos['is_coordinador']!=True:
            res={
                'estudiante':estudiantes_datos['id']
            }
            
        else:
            readonly={
                'estudiante':False
                }
        return {'value':res}
        
    def button_dummy(self, cr, uid, ids, context=None):
        return True
   
    def cancelar_preinscripcion(self, cr, uid, ids, context=None):
        return self.write(cr,uid,ids,{'state':'cancelar'},context=context)
    
    def preinscribir_materia(self, cr, uid, ids, context=None):
        res_user_obj=self.pool.get('res.users')
        res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
        print res_user_datos['is_coordinador']
        hoy=date.today()
        for i in self.browse(cr,uid,ids,context=context):
            planificacion_semestre_obj=self.pool.get('unefa.planificacion_semestre')
            planificacion_semestre_ids=planificacion_semestre_obj.search(cr,uid,[('periodo_id','=',int(i.periodo_id))],context=context)
            planificacion_semestre_datos=planificacion_semestre_obj.browse(cr,uid,planificacion_semestre_ids,context=context)
            for p in planificacion_semestre_datos:
                for a in p.actividad_ids:
                    fecha_desde=datetime.strptime(a.fecha_desde, '%Y-%m-%d')
                    fecha_desde =datetime.date(fecha_desde)
                    fecha_hasta=datetime.strptime(a.fecha_hasta, '%Y-%m-%d')
                    fecha_hasta =datetime.date(fecha_hasta)
                    if res_user_datos['is_coordinador'] != True:
                        if a.actividad_id.actividad=="Preinscripción":
                            if (cmp(fecha_desde,hoy)==-1 and cmp(hoy,fecha_hasta)==-1) or (cmp(fecha_desde,hoy)==0) or (cmp(hoy,fecha_hasta)==0):
                                print 'hecho'
                                inscripcion_asignatura_obj=self.pool.get('unefa.inscripcion_asignatura')
                                inscripcion_asignatura_ids=inscripcion_asignatura_obj.search(cr,uid,[('inscripcion_asiganatura_id','=',i.id)],context=context)
                                inscripcion_asignatura_datos=inscripcion_asignatura_obj.browse(cr,uid,inscripcion_asignatura_ids,context=context)
                                inscripcion_asignatura_obj.write(cr,uid,ids,{'state':'preinscrito'},context=context)
                                self.write(cr,uid,ids,{'state':'preinscrito'},context=context)
                            else:
                                raise osv.except_osv(
                                                ('Alerta!'),
                                                (u'El proceso de preinscricpción aun no esta habilitado'))
                    else:
                        inscripcion_asignatura_obj=self.pool.get('unefa.inscripcion_asignatura')
                        inscripcion_asignatura_ids=inscripcion_asignatura_obj.search(cr,uid,[('inscripcion_asiganatura_id','=',i.id)],context=context)
                        inscripcion_asignatura_datos=inscripcion_asignatura_obj.browse(cr,uid,inscripcion_asignatura_ids,context=context)
                        inscripcion_asignatura_obj.write(cr,uid,ids,{'state':'preinscrito'},context=context)
                        self.write(cr,uid,ids,{'state':'preinscrito'},context=context)
                        
        return True
        
    def inscribir_materia(self, cr, uid, ids, context=None):
        for i in self.browse(cr,uid,ids,context=context):
            inscripcion_asignatura_obj=self.pool.get('unefa.inscripcion_asignatura')
            inscripcion_asignatura_ids=inscripcion_asignatura_obj.search(cr,uid,[('inscripcion_asiganatura_id','=',i.id)],context=context)
            inscripcion_asignatura_datos=inscripcion_asignatura_obj.browse(cr,uid,inscripcion_asignatura_ids,context=context)
        inscripcion_asignatura_obj.write(cr,uid,ids,{'state':'inscrito'},context=context)
        self.write(cr,uid,ids,{'state':'inscrito'},context=context)
        return True
        
    def generar_planilla(self, cr, uid, ids, context=None):
        return True
        
    def create(self,cr,uid,vals,context=None):
        res=self.onchange_cargar_datos(cr, uid, [], context=None)
        res=res.values()
        res=res[0]
        h=super(unefa_inscripcion, self).create(cr, uid, vals, context=context)
        self.write(cr,uid,h,res,context=context)
        return h
    




class unefa_inscripcion_asignatura(osv.osv):
    _name = "unefa.inscripcion_asignatura"
    _rec_name="asignatura_id"
    
    _columns = {
        'inscripcion_asiganatura_id': fields.many2one('unefa.inscripcion_asignatura', required=True),
        'semestre_id': fields.many2one('unefa.semestre', 'Semestre',required=True,),
        'asignatura_id': fields.many2one('unefa.materia', 'Asignatura',required=True,),
        'codigo': fields.char('Código', readonly=True,),
        'unidades_creditos': fields.integer('Unidades de crédito', readonly=True,),
        'seccion_id': fields.many2one('unefa.seccion', 'Sección', required=False,),
        'state': fields.selection([
            ('borrador', 'Borrador'),
            ('preinscrito', 'Preinscrito'),
            ('inscrito', 'Inscrito'),
            ('cancelar', 'Cancelar'),
            ], 'Estado', readonly=True, copy=False, help="Este es es estado actual de la inscripción.", select=True),
    }
    
    _defaults = {
        'state':'borrador'
    }
    
    def onchange_semestre(self, cr, uid, ids, semestre_id,accion, context=None):
        res={}
        domain={}
        id_materia=[]
        if accion=='semestre':
            res={
            'asignatura_id':'',
                }
        if semestre_id:
            cr.execute("select materia_id from rel_sem_mat where relacion_sem_id=%s",(str(semestre_id),))
            for i in cr.fetchall():
                id_materia.append(i[0])
        domain = {'asignatura_id': [('id', '=', list(id_materia))]}
        
        return {'value':res,'domain': domain}
        
    def onchange_asignatura(self, cr, uid, ids, asignatura_id,accion, context=None):
        res={}
        materia_obj=self.pool.get('unefa.materia')
        materia_ids=materia_obj.search(cr,uid,[('id','=',asignatura_id)],context=context)
        materia_datos=materia_obj.browse(cr,uid,materia_ids,context=context)
        if asignatura_id:
            res={
            'codigo':materia_datos['codigo'],
            'unidades_creditos':materia_datos['uc'],
                }
        return {'value':res,}

    def create(self,cr,uid,vals,context=None):
        asig=self.onchange_asignatura(cr, uid, [],vals['asignatura_id'],'hola', context=None)
        asig=asig.values()
        asig=asig[0]
        ids=super(unefa_inscripcion_asignatura, self).create(cr, uid, vals, context=context)
        self.write(cr,uid,ids,asig,context=context)
        return ids
        

class unefa_seccion(osv.osv):
    _name = 'unefa.seccion'
    
    _columns = {
        'seccion':fields.char('Sección',
                    required=True,
                    ),
    }
    
   

