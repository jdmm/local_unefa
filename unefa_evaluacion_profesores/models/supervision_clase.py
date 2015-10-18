# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class unefa_supervision_clase(osv.osv):
   
    _name ='unefa.supervision.clase'
    _rec_name ='nombre'
    
    def calculo_sub_total_planif(self,cr,uid,ids,field_name,arg, context=None):
        res={}
        suma=0
        for i in self.browse(cr,uid,ids):
            for n in i.planif_registro_control_ids:
                eval_planif_registro_control_obj=self.pool.get('unefa.eval.planif.registro_control')
                eval_planif_registro_control_ids=eval_planif_registro_control_obj.search(cr,uid,[('id','=',int(n.evaluacion))],context=context)
                eval_planif_registro_control_datos=eval_planif_registro_control_obj.browse(cr,uid,eval_planif_registro_control_ids,context=context)
                suma+=eval_planif_registro_control_datos['valor_opcion']
        res[i.id]=suma,
        for a in res[i.id]:
            res[i.id]=a
        return res
        
    def calculo_sub_total_asis(self,cr,uid,ids,field_name,arg, context=None):
        res={}
        suma=0
        for i in self.browse(cr,uid,ids):
            for n in i.asistencia_puntualidad_ids:
                eval_asistencia_puntualidad_obj=self.pool.get('unefa.eval.asistencia.puntualidad')
                eval_asistencia_puntualidad_ids=eval_asistencia_puntualidad_obj.search(cr,uid,[('id','=',int(n.evaluacion))],context=context)
                eval_asistencia_puntualidad_datos=eval_asistencia_puntualidad_obj.browse(cr,uid,eval_asistencia_puntualidad_ids,context=context)
                suma+=eval_asistencia_puntualidad_datos['valor_opcion']
        res[i.id]=suma,
        for a in res[i.id]:
            res[i.id]=a
        return res
        
    def calculo_sub_total_inicio(self,cr,uid,ids,field_name,arg, context=None):
        res={}
        suma=0
        for i in self.browse(cr,uid,ids):
            for n in i.inicio_clase_ids:
                eval_inicio_clase_obj=self.pool.get('unefa.eval.inicio.clase')
                eval_inicio_clase_ids=eval_inicio_clase_obj.search(cr,uid,[('id','=',int(n.evaluacion))],context=context)
                eval_inicio_clase_datos=eval_inicio_clase_obj.browse(cr,uid,eval_inicio_clase_ids,context=context)
                suma+=eval_inicio_clase_datos['valor_opcion']
        res[i.id]=suma,
        for a in res[i.id]:
            res[i.id]=a
        return res
        
    def calculo_sub_total_desarrollo(self,cr,uid,ids,field_name,arg, context=None):
        res={}
        suma=0
        for i in self.browse(cr,uid,ids):
            for n in i.desarrollo_clase_ids:
                eval_desarrollo_clase_obj=self.pool.get('unefa.eval.desarrollo.clase')
                eval_desarrollo_clase_ids=eval_desarrollo_clase_obj.search(cr,uid,[('id','=',int(n.evaluacion))],context=context)
                eval_desarrollo_clase_datos=eval_desarrollo_clase_obj.browse(cr,uid,eval_desarrollo_clase_ids,context=context)
                suma+=eval_desarrollo_clase_datos['valor_opcion']
        res[i.id]=suma,
        for a in res[i.id]:
            res[i.id]=a
        return res
        
    def calculo_sub_total_recursos(self,cr,uid,ids,field_name,arg, context=None):
        res={}
        suma=0
        for i in self.browse(cr,uid,ids):
            for n in i.recursos_didacticos_ids:
                eval_recursos_didacticos_obj=self.pool.get('unefa.eval.recursos.didacticos')
                eval_recursos_didacticos_ids=eval_recursos_didacticos_obj.search(cr,uid,[('id','=',int(n.evaluacion))],context=context)
                eval_recursos_didacticos_datos=eval_recursos_didacticos_obj.browse(cr,uid,eval_recursos_didacticos_ids,context=context)
                suma+=eval_recursos_didacticos_datos['valor_opcion']
        res[i.id]=suma,
        for a in res[i.id]:
            res[i.id]=a
        return res
        
    def calculo_sub_total_cierre(self,cr,uid,ids,field_name,arg, context=None):
        res={}
        suma=0
        for i in self.browse(cr,uid,ids):
            for n in i.cierre_clase_ids:
                eval_cierre_clase_obj=self.pool.get('unefa.eval.cierre.clase')
                eval_cierre_clase_ids=eval_cierre_clase_obj.search(cr,uid,[('id','=',int(n.evaluacion))],context=context)
                eval_cierre_clase_datos=eval_cierre_clase_obj.browse(cr,uid,eval_cierre_clase_ids,context=context)
                suma+=eval_cierre_clase_datos['valor_opcion']
        res[i.id]=suma,
        for a in res[i.id]:
            res[i.id]=a
        return res
        
    def calculo_total(self,cr,uid,ids,field_name,arg, context=None):
        res={}
        total=0
        for i in self.browse(cr,uid,ids):
            total=i.subtotal_planif+i.subtotal_asis+i.subtotal_inicio+i.subtotal_desarrollo+i.subtotal_cierre
        res[i.id]=total,
        for a in res[i.id]:
            res[i.id]=a
        return res
    
    _columns = {
        'nombre': fields.char('Nombres', readonly=False,
                    required=False,
                    ),
        'apellido': fields.char('Apellidos',
                    required=False,
                    ),
        'cedula': fields.integer('Cédula',
                    required=False,
                    ),
        'fecha_evaluacion': fields.datetime('Fecha Evaluación', select=True, readonly=False),
        'periodo_id': fields.many2one('unefa.conf.periodo_academico',
                    'Periodo Académico',
                    required=False,
                    ),
        'carrera': fields.char('Carrera', readonly=False,
                    required=False,
                    ),
        'regimen_id': fields.many2one('unefa.regimen', 'Régimen',),
        'asignatura': fields.char('Asignatura',
                    required=False,
                    ),
        'seccion': fields.char('Seccion',
                    required=False,
                    ),
        'sede': fields.char('Sede',
                    required=False,
                    ),
        'aula': fields.char('Aula',
                    required=False,
                    ),
        'coordinador': fields.char('Coordinador',
                    required=False,
                    ),
        'evaluador': fields.char('Evaluador',
                    required=False,
                    ),
        'estudiantes_inscritos': fields.integer('Estudiantes Inscritos',
                    required=False,
                    ),
        'estudiantes_presentes': fields.integer('Estudiantes Presentes',
                    required=False,
                    ),
        'contenido': fields.char('Contenido',
                    required=False,
                    ),
        'tipo': fields.selection([
                ('teorica', 'Teorica'),
                ('practica', 'Practica'),
                ('teorica_practica', 'Teorica Practica'),
                ], 'Tipo de clase',  help="", select=True),
        
        'planif_registro_control_ids': fields.one2many('unefa.planif.registro.control', 'supervision_clase_id', required=True),
        'asistencia_puntualidad_ids': fields.one2many('unefa.asistencia.puntualidad', 'supervision_clase_id', required=True),
        'inicio_clase_ids': fields.one2many('unefa.inicio.clase', 'supervision_clase_id', required=True),
        'desarrollo_clase_ids': fields.one2many('unefa.desarrollo.clase', 'supervision_clase_id', required=True),
        'recursos_didacticos_ids': fields.one2many('unefa.recursos.didacticos', 'supervision_clase_id', required=True),
        'cierre_clase_ids': fields.one2many('unefa.cierre.clase', 'supervision_clase_id', required=True),
        'cualidades_sobresalientes': fields.text('Cualidades Sobresalientes del Profesor',
                    required=False,
                    ),
        'cualidades_mejorables': fields.text('Cualidades Mejorables del Profesor',
                    required=False,
                    ),
        'observaciones_profesor': fields.text('Observaciones del Profesor',
                    required=False,
                    ),
        'subtotal_planif':fields.function(
                        calculo_sub_total_planif,
                        string="Subtotal",
                        type='integer',
                        help=''),
        'subtotal_asis':fields.function(
                        calculo_sub_total_asis,
                        string="Subtotal",
                        type='integer',
                        help=''),
        'subtotal_inicio':fields.function(
                        calculo_sub_total_inicio,
                        string="Subtotal",
                        type='integer',
                        help=''),
        'subtotal_desarrollo':fields.function(
                        calculo_sub_total_desarrollo,
                        string="Subtotal",
                        type='integer',
                        help=''),
        'subtotal_recursos':fields.function(
                        calculo_sub_total_recursos,
                        string="Subtotal",
                        type='integer',
                        help=''),
        'subtotal_cierre':fields.function(
                        calculo_sub_total_cierre,
                        string="Subtotal",
                        type='integer',
                        help=''),
        'total_evalu':fields.function(
                        calculo_total,
                        string="Total",
                        type='integer',
                        help=''),
    }
    
    
    
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
        res={}
        item_planif_registro_control_obj=self.pool.get('unefa.items.planif.registro_control')
        item_planif_registro_control_ids=item_planif_registro_control_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_planif_registro_control_datos=item_planif_registro_control_obj.browse(cr,uid,item_planif_registro_control_ids,context=context)
        
        item_asistencia_control_obj=self.pool.get('unefa.items.asistencia.evaluacion')
        item_asistencia_control_ids=item_asistencia_control_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_asistencia_control_datos=item_asistencia_control_obj.browse(cr,uid,item_asistencia_control_ids,context=context)
        
        item_inicio_clase_obj=self.pool.get('unefa.items.inicio.clase')
        item_inicio_clase_ids=item_inicio_clase_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_inicio_clase_datos=item_inicio_clase_obj.browse(cr,uid,item_inicio_clase_ids,context=context)
        item_desarrollo_clase_obj=self.pool.get('unefa.items.desarrollo.clase')
        item_desarrollo_clase_ids=item_desarrollo_clase_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_desarrollo_clase_datos=item_desarrollo_clase_obj.browse(cr,uid,item_desarrollo_clase_ids,context=context)
        
        item_recursos_didacticos_obj=self.pool.get('unefa.items.recursos.didacticos')
        item_recursos_didacticos_ids=item_recursos_didacticos_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_recursos_didacticos_datos=item_recursos_didacticos_obj.browse(cr,uid,item_recursos_didacticos_ids,context=context)
        
        
        item_cierre_clase_obj=self.pool.get('unefa.items.cierre.clase')
        item_cierre_clase_ids=item_cierre_clase_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_cierre_clase_datos=item_cierre_clase_obj.browse(cr,uid,item_cierre_clase_ids,context=context)
        items_planif=[]
        items_asis=[]
        items_inic=[]
        items_desar=[]
        items_recur=[]
        items_cierre=[]
        for i in item_planif_registro_control_datos:
            items_planif.append([0,False,{'items_evaluacion':i.id }])
        for i in item_asistencia_control_datos:
            items_asis.append([0,False,{'items_evaluacion':i.id }])
        for i in item_inicio_clase_datos:
            items_inic.append([0,False,{'items_evaluacion':i.id }])
        for i in item_desarrollo_clase_datos:
            items_desar.append([0,False,{'items_evaluacion':i.id }])
        for i in item_recursos_didacticos_datos:
            items_recur.append([0,False,{'items_evaluacion':i.id }])
        for i in item_cierre_clase_datos:
            items_cierre.append([0,False,{'items_evaluacion':i.id }])
        res={
            'planif_registro_control_ids':items_planif,
            'asistencia_puntualidad_ids':items_asis,
            'inicio_clase_ids':items_inic,
            'desarrollo_clase_ids':items_desar,
            'recursos_didacticos_ids':items_recur,
            'cierre_clase_ids':items_cierre,
            }
        return {'value':res}
        
        
        
        
        
    def button_dummy(self, cr, uid, ids, context=None):
        return True

    
class unefa_planif_registro_control(osv.osv):
   
    _name = 'unefa.planif.registro.control'
    _rec_name = 'items_evaluacion'

    _columns = {
        
        'supervision_clase_id': fields.many2one('unefa.supervision.clase', 'Supervisión',),
        'items_evaluacion': fields.many2one('unefa.items.planif.registro_control', 'Items de evaluación',),
        'evaluacion': fields.many2one('unefa.eval.planif.registro_control', 'Evaluación',),
        }

class unefa_eval_planif_registro_control(osv.osv):
   
    _name = 'unefa.eval.planif.registro_control'
    _rec_name = 'evaluacion'

    _columns = {
        
        'evaluacion': fields.char('Opción de Evaluación',
                    required=True,
                    help="",
                    ),
        'valor_opcion': fields.integer('Valor',
                        help="",
                    ),
    }

class unefa_items_planif_registro_control(osv.osv):
   
    _name = 'unefa.items.planif.registro_control'
    _rec_name = 'item_evaluacion'

    _columns = {
        
        'item_evaluacion': fields.char('Item de evaluación',
                    required=True,
                    help="",
                    ),
        'item_activo': fields.boolean('Item Activo',
                        help="",
                    ),
    }


class unefa_asistencia_puntualidad(osv.osv):
   
    _name = 'unefa.asistencia.puntualidad'
    _rec_name = 'items_evaluacion'

    _columns = {
        
        'supervision_clase_id': fields.many2one('unefa.supervision.clase', 'Supervisión',),
        'items_evaluacion': fields.many2one('unefa.items.asistencia.evaluacion', 'Items de evaluación',),
        'evaluacion': fields.many2one('unefa.eval.asistencia.puntualidad', 'Evaluación',),
    }

class unefa_eval_asistencia_puntualidad(osv.osv):
   
    _name = 'unefa.eval.asistencia.puntualidad'
    _rec_name = 'evaluacion'

    _columns = {
        
        'evaluacion': fields.char('Opción de Evaluación',
                    required=True,
                    help="",
                    ),
        'valor_opcion': fields.integer('Valor',
                        help="",
                    ),
    }
    
class unefa_items_asistencia_evaluacion(osv.osv):
   
    _name = 'unefa.items.asistencia.evaluacion'
    _rec_name = 'item_evaluacion'

    _columns = {
        
        'item_evaluacion': fields.char('Item de evaluación',
                    required=False,
                    help="",
                    ),
        'item_activo': fields.boolean('Item Activo',
                        help="",
                    ),
    }
    
    
class unefa_inicio_clase(osv.osv):
   
    _name = 'unefa.inicio.clase'
    _rec_name = 'items_evaluacion'

    _columns = {
        
        'supervision_clase_id': fields.many2one('unefa.supervision.clase', 'Supervisión',),
        'items_evaluacion': fields.many2one('unefa.items.inicio.clase', 'Items de evaluación',),
        'evaluacion': fields.many2one('unefa.eval.inicio.clase', 'Evaluación',),
    }

class unefa_eval_inicio_clase(osv.osv):
   
    _name = 'unefa.eval.inicio.clase'
    _rec_name = 'evaluacion'

    _columns = {
        
        'evaluacion': fields.char('Opción de Evaluación',
                    required=True,
                    help="",
                    ),
        'valor_opcion': fields.integer('Valor',
                        help="",
                    ),
    }
    
class unefa_items_inicio_clase(osv.osv):
   
    _name = 'unefa.items.inicio.clase'
    _rec_name = 'item_evaluacion'
    
   
    
    _columns = {
        
        'item_evaluacion': fields.char('Item de evaluación',
                    required=True,
                    help="",
                    ),
        'item_activo': fields.boolean('Item Activo',
                        help="",
                    ),
    }
    
    
class unefa_desarrollo_clase(osv.osv):
   
    _name = 'unefa.desarrollo.clase'
    _rec_name = 'items_evaluacion'

    _columns = {
        
        'supervision_clase_id': fields.many2one('unefa.supervision.clase', 'Supervisión',),
        'items_evaluacion': fields.many2one('unefa.items.desarrollo.clase', 'Items de evaluación',),
        'evaluacion': fields.many2one('unefa.eval.desarrollo.clase', 'Items de evaluación',),
    }

class unefa_eval_desarrollo_clase(osv.osv):
   
    _name = 'unefa.eval.desarrollo.clase'
    _rec_name = 'evaluacion'

    _columns = {
        
        'evaluacion': fields.char('Opción de Evaluación',
                    required=True,
                    help="",
                    ),
        'valor_opcion': fields.integer('Valor',
                        help="",
                    ),
    }
    
class unefa_items_desarrollo_clase(osv.osv):
   
    _name = 'unefa.items.desarrollo.clase'
    _rec_name = 'item_evaluacion'
    
   
    
    _columns = {
        
        'item_evaluacion': fields.char('Item de evaluación',
                    required=True,
                    help="",
                    ),
        'item_activo': fields.boolean('Item Activo',
                        help="",
                    ),
    }
    
    
class unefa_recursos_didacticos(osv.osv):
   
    _name = 'unefa.recursos.didacticos'
    _rec_name = 'items_evaluacion'

    _columns = {
        
        'supervision_clase_id': fields.many2one('unefa.supervision.clase', 'Supervisión',),
        'items_evaluacion': fields.many2one('unefa.items.recursos.didacticos', 'Items de evaluación',),
        'evaluacion': fields.many2one('unefa.eval.recursos.didacticos', 'Items de evaluación',),
    }

class unefa_eval_recursos_didacticos(osv.osv):
   
    _name = 'unefa.eval.recursos.didacticos'
    _rec_name = 'evaluacion'

    _columns = {
        
        'evaluacion': fields.char('Opción de Evaluación',
                    required=True,
                    help="",
                    ),
        'valor_opcion': fields.integer('Valor',
                        help="",
                    ),
    }
    
class unefa_items_recursos_didacticos(osv.osv):
   
    _name = 'unefa.items.recursos.didacticos'
    _rec_name = 'item_evaluacion'

    _columns = {
        
        'item_evaluacion': fields.char('Item de evaluación',
                    required=True,
                    help="",
                    ),
        'item_activo': fields.boolean('Item Activo',
                        help="",
                    ),
    }


    
    
class unefa_cierre_clase(osv.osv):
   
    _name = 'unefa.cierre.clase'
    _rec_name = 'items_evaluacion'

    _columns = {
        
        'supervision_clase_id': fields.many2one('unefa.supervision.clase', 'Supervisión',),
        'items_evaluacion': fields.many2one('unefa.items.cierre.clase', 'Items de evaluación',),
        'evaluacion': fields.many2one('unefa.eval.cierre.clase', 'Items de evaluación',),
    }

class unefa_eval_cierre_clase(osv.osv):
   
    _name = 'unefa.eval.cierre.clase'
    _rec_name = 'evaluacion'

    _columns = {
        
        'evaluacion': fields.char('Opción de Evaluación',
                    required=True,
                    help="",
                    ),
        'valor_opcion': fields.integer('Valor',
                        help="",
                    ),
    }
    
class unefa_items_desarrollo_clase(osv.osv):
   
    _name = 'unefa.items.cierre.clase'
    _rec_name = 'item_evaluacion'

    _columns = {
        
        'item_evaluacion': fields.char('Item de evaluación',
                    required=True,
                    help="",
                    ),
        'item_activo': fields.boolean('Item Activo',
                        help="",
                    ),
    }
