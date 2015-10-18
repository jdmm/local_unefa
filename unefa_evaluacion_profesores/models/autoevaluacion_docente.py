# -*- coding: utf-8 -*-

from openerp.osv import fields, osv

class unefa_autoevaluacion_docente(osv.osv):
   
    _name ='unefa.autoevaluacion_docente'
    _rec_name ='docente'
    
    def get_select_porcentaje(desde,hasta):
        porc=[]
        for i in range(desde,hasta):
            porc.append((str(i),str(i)))
        return porc


    _columns = {
        'docente': fields.char('Docente', readonly=False,
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
        'n_secciones_asignadas': fields.integer('N° Secciones Asignadas',
                    required=False,
                    ),
        'secciones_evaluada': fields.char('Sección Evaluada',
                    required=False,
                    ),
        'sede': fields.char('Sede',
                    required=False,
                    ),
        'coordinador': fields.char('Coordinador',
                    required=False,
                    ),
        'evaluador': fields.char('Evaluador',
                    required=False,
                    ),
        
        'asistencia_puntualidad_ids': fields.one2many('unefa.asis.puntualidad', 'asistencia_puntualidad_id', required=True),
        
        'planif_registro_control_ids': fields.one2many('unefa.planificacion.registro.control', 'planif_registro_control_id', required=True),
        'interaccion_doce_estu_ids': fields.one2many('unefa.interaccion.docente.estudiante', 'interac_docente_estudiante_id', required=True),
        'praxis_academica_ids': fields.one2many('unefa.praxis.academica', 'praxis_academica_id', required=True),
        'estrategias_ense_ids': fields.one2many('unefa.estrategia.ensenanza', 'estrat_ensen_id', required=True),
        'recursos_didacticos': fields.one2many('unefa.recur.didacticos', 'recursos_didacticos_id', required=True),
        'evaluacion_aprendizaje_ids': fields.one2many('unefa.eval.aprendizaje', 'eval_aprendizaje_id', required=True),
        'aspecto_positivo': fields.text('Aspectos Positivos',
                    required=False,
                    ),
        'aspectos_cambiar': fields.text('Aspectos Positivos',
                    required=False,
                    ),
        'aspectos_mejoras': fields.text('Aspectos Positivos',
                    required=False,
                    ),
        'califi_personal': fields.text('Aspectos Positivos',
                    required=False,
                    ),
        'calificacion': fields.selection(
                    get_select_porcentaje(1,21),
                    'Calificación', select=True),
        'comentarios_adic': fields.text('Comentarios Adicionales',
                    required=False,
                    ),

        
    }
    
    
    def onchange_cargar_datos_autoevaluacion (self, cr, uid, ids, context=None):
        res={}
        item_asis_puntualidad_obj=self.pool.get('unefa.items.asis.puntualidad')
        item_asis_puntualidad_ids=item_asis_puntualidad_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_asis_puntualidad_datos=item_asis_puntualidad_obj.browse(cr,uid,item_asis_puntualidad_ids,context=context)
        
        item_planificacion_registro_control_obj=self.pool.get('unefa.items.planificacion.registro.control')
        item_planificacion_registro_control_ids=item_planificacion_registro_control_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_planificacion_registro_control_datos=item_planificacion_registro_control_obj.browse(cr,uid,item_planificacion_registro_control_ids,context=context)
       
        item_interaccion_docente_estudiante_obj=self.pool.get('unefa.items.interaccion.docente.estudiante')
        item_interaccion_docente_estudiante_ids=item_interaccion_docente_estudiante_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_interaccion_docente_estudiante_datos=item_interaccion_docente_estudiante_obj.browse(cr,uid,item_interaccion_docente_estudiante_ids,context=context)
        
        
        item_praxis_academica_obj=self.pool.get('unefa.items.praxis.academica')
        item_praxis_academica_ids=item_praxis_academica_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_praxis_academica_datos=item_praxis_academica_obj.browse(cr,uid,item_praxis_academica_ids,context=context)
       
        item_estrategia_ensenanza_obj=self.pool.get('unefa.items.estrategia.ensenanza')
        item_estrategia_ensenanza_ids=item_estrategia_ensenanza_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_estrategia_ensenanza_datos=item_estrategia_ensenanza_obj.browse(cr,uid,item_estrategia_ensenanza_ids,context=context)
        
        item_recursos_didacticos_obj=self.pool.get('unefa.items.recur.didacticos')
        item_recursos_didacticos_ids=item_recursos_didacticos_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_recursos_didacticos_datos=item_recursos_didacticos_obj.browse(cr,uid,item_recursos_didacticos_ids,context=context)
        
        item_eval_aprendizaje_obj=self.pool.get('unefa.items.eval.aprendizaje')
        item_eval_aprendizaje_ids=item_eval_aprendizaje_obj.search(cr,uid,[('item_activo','=','True')],context=context)
        item_eval_aprendizaje_datos=item_eval_aprendizaje_obj.browse(cr,uid,item_eval_aprendizaje_ids,context=context)
        
        items_asis_punt=[]
        items_planif=[]
        items_interac=[]
        items_praxis=[]
        items_estrat=[]
        items_recur=[]
        items_eval=[]
        for i in item_asis_puntualidad_datos:
            items_asis_punt.append([0,False,{'items_evaluacion':i.id }])
        for i in item_planificacion_registro_control_datos:
            items_planif.append([0,False,{'items_evaluacion':i.id }])
        for i in item_interaccion_docente_estudiante_datos:
            items_interac.append([0,False,{'items_evaluacion':i.id }])
        for i in item_praxis_academica_datos:
            items_praxis.append([0,False,{'items_evaluacion':i.id }])
        for i in item_estrategia_ensenanza_datos:
            items_estrat.append([0,False,{'items_evaluacion':i.id }])
        for i in item_recursos_didacticos_datos:
            items_recur.append([0,False,{'items_evaluacion':i.id }])
        for i in item_eval_aprendizaje_datos:
            items_eval.append([0,False,{'items_evaluacion':i.id }])
        
        res={
            'asistencia_puntualidad_ids':items_asis_punt,
            'planif_registro_control_ids':items_planif,
            'interaccion_doce_estu_ids':items_interac,
            'praxis_academica_ids':items_praxis,
            'estrategias_ense_ids':items_estrat,
            'recursos_didacticos':items_recur,
            'evaluacion_aprendizaje_ids':items_eval,
            }
        return {'value':res}

class unefa_asis_puntualidad(osv.osv):
   
    _name = 'unefa.asis.puntualidad'
    _rec_name = 'items_evaluacion'

    _columns = {
        
        'asistencia_puntualidad_id': fields.many2one('unefa.autoevaluacion_docente', 'Autoevaluación',),
        'items_evaluacion': fields.many2one('unefa.items.asis.puntualidad', 'Items de evaluación',),
        'evaluacion': fields.selection([
                    ('nunca', 'Nunca'),
                    ('algunas', 'Algunas Veces'),
                    ('casi', 'Casi Siempre'),
                    ('siempre', 'Siempre'),
            ], 'Evaluación', readonly=True, select=True),
        }
        

class unefa_items_asis_puntualidad(osv.osv):
   
    _name = 'unefa.items.asis.puntualidad'
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
    
    
    
class unefa_planificacion_registro_control(osv.osv):
   
    _name = 'unefa.planificacion.registro.control'
    _rec_name = 'items_evaluacion'

    _columns = {
         
        'planif_registro_control_id': fields.many2one('unefa.autoevaluacion_docente', 'Autoevaluación',),
        'items_evaluacion': fields.many2one('unefa.items.planificacion.registro.control', 'Items de evaluación',),
        'evaluacion': fields.selection([
                    ('nunca', 'Nunca'),
                    ('algunas', 'Algunas Veces'),
                    ('casi', 'Casi Siempre'),
                    ('siempre', 'Siempre'),
            ], 'Evaluación', readonly=True, select=True),
        }
        

class unefa_items_planif_registro_control(osv.osv):
   
    _name = 'unefa.items.planificacion.registro.control'
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
    
    
    
class unefa_interaccion_docente_estudiante(osv.osv):
   
    _name = 'unefa.interaccion.docente.estudiante'
    _rec_name = 'items_evaluacion'

    _columns = {
 
        'interac_docente_estudiante_id': fields.many2one('unefa.autoevaluacion_docente', 'Autoevaluación',),
        'items_evaluacion': fields.many2one('unefa.items.interaccion.docente.estudiante', 'Items de evaluación',),
        'evaluacion': fields.selection([
                    ('nunca', 'Nunca'),
                    ('algunas', 'Algunas Veces'),
                    ('casi', 'Casi Siempre'),
                    ('siempre', 'Siempre'),
            ], 'Evaluación', readonly=True, select=True),
        }
        

class unefa_items_planif_registro_control(osv.osv):
   
    _name = 'unefa.items.interaccion.docente.estudiante'
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
    
    
    
class unefa_praxis_academica(osv.osv):
   
    _name = 'unefa.praxis.academica'
    _rec_name = 'items_evaluacion'

    _columns = {

        'praxis_academica_id': fields.many2one('unefa.autoevaluacion_docente', 'Autoevaluación',),
        'items_evaluacion': fields.many2one('unefa.items.praxis.academica', 'Items de evaluación',),
        'evaluacion': fields.selection([
                    ('nunca', 'Nunca'),
                    ('algunas', 'Algunas Veces'),
                    ('casi', 'Casi Siempre'),
                    ('siempre', 'Siempre'),
            ], 'Evaluación', readonly=True, select=True),
        }
        

class unefa_items_praxis_academica(osv.osv):
   
    _name = 'unefa.items.praxis.academica'
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
    
    
    
class unefa_estrategia_ensenanza(osv.osv):
   
    _name = 'unefa.estrategia.ensenanza'
    _rec_name = 'items_evaluacion'

    _columns = {
        

        'estrat_ensen_id': fields.many2one('unefa.autoevaluacion_docente', 'Autoevaluación',),
        'items_evaluacion': fields.many2one('unefa.items.estrategia.ensenanza', 'Items de evaluación',),
        'evaluacion': fields.selection([
                    ('nunca', 'Nunca'),
                    ('algunas', 'Algunas Veces'),
                    ('casi', 'Casi Siempre'),
                    ('siempre', 'Siempre'),
            ], 'Evaluación', readonly=True, select=True),
        }
        

class unefa_items_estrategia_ensenanza(osv.osv):
   
    _name = 'unefa.items.estrategia.ensenanza'
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
    
    
class unefa_recur_didacticos(osv.osv):
   
    _name = 'unefa.recur.didacticos'
    _rec_name = 'items_evaluacion'

    _columns = {
         
        'recursos_didacticos_id': fields.many2one('unefa.autoevaluacion_docente', 'Autoevaluación',),
        'items_evaluacion': fields.many2one('unefa.items.recur.didacticos', 'Items de evaluación',),
        'evaluacion': fields.selection([
                    ('nunca', 'Nunca'),
                    ('algunas', 'Algunas Veces'),
                    ('casi', 'Casi Siempre'),
                    ('siempre', 'Siempre'),
            ], 'Evaluación', readonly=True, select=True),
        }
        

class unefa_items_recur_didacticos(osv.osv):
   
    _name = 'unefa.items.recur.didacticos'
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
    
    
class unefa_eval_aprendizaje(osv.osv):
   
    _name = 'unefa.eval.aprendizaje'
    _rec_name = 'items_evaluacion'

    _columns = {
        
        'eval_aprendizaje_id': fields.many2one('unefa.autoevaluacion_docente', 'Autoevaluación',),
        'items_evaluacion': fields.many2one('unefa.items.eval.aprendizaje', 'Items de evaluación',),
        'evaluacion': fields.selection([
                    ('nunca', 'Nunca'),
                    ('algunas', 'Algunas Veces'),
                    ('casi', 'Casi Siempre'),
                    ('siempre', 'Siempre'),
            ], 'Evaluación', readonly=True, select=True),
        }
        

class unefa_items_eval_aprendizaje(osv.osv):
   
    _name = 'unefa.items.eval.aprendizaje'
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


