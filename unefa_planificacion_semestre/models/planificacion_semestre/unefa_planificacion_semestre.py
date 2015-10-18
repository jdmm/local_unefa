# -*- coding: utf-8 -*-
##############################################################################
#
#    Programa realizado por, Jeison Pernía y Jonathan Reyes en el marco
#    del plan de estudios de la UNEFA, como TRABAJO ESPECIAL DE GRADO,
#    con el de optar al título de Ingeniero de Sistemas.
#
##############################################################################

from openerp.osv import fields, osv
import sys
reload(sys)
sys.setdefaultencoding('UTF8')


class unefa_planificacion_semestre(osv.osv):
    _name = 'unefa.planificacion_semestre'
   
    
    _columns = {
        'carrera_id': fields.many2one(
                                'unefa.carrera',
                                'Carrera',
                                required=True,
                                readonly=True,
                                states={'borrador': [('readonly', False)]},
                                ),
        'periodo_id': fields.many2one(
                                'unefa.conf.periodo_academico',
                                'Período Académico',
                                required=True,
                                readonly=True,
                                states={'borrador': [('readonly', False)]},
                                ),
        'fecha': fields.datetime(
                            'Fecha'
                            ,),
        'observaciones': fields.text(
                                'Observaciones'
                                ),
        'actividad_ids': fields.one2many(
                                    'unefa.cronograma_inscripcion', 
                                    'planif_id', 
                                    'Actividad',
                                    required=True),
        'cronograma_actividad_ids': fields.one2many(
                                            'unefa.cronograma_actividades', 
                                            'crono_activ_id', 
                                            'Actividad',),
        'state': fields.selection([
                            ('borrador', 'Borrador'),
                            ('aprobado', 'Aprobado'),], 
                            'Estado', 
                            readonly=True, 
                            help="Este es es estado actual del cronograma.",
                            ),
    }
    
    _defaults = {
        'fecha': fields.datetime.now,
        'state': 'borrador',
    }
    
    def onchange_cronograma_inscripcion(self, cr, uid, ids, context=None):
        res={}
        cronograma_obj=self.pool.get('unefa.cronograma_actividades_inscripcion')
        cronograma_ids=cronograma_obj.search(cr,uid,[('activo','=','True')],context=context)
        cronograma_datos=cronograma_obj.browse(cr,uid,cronograma_ids,context=context)
        list_actividad=[]
        for i in cronograma_datos:
            list_actividad.append([0,False,{'actividad_id':i.id }])
        res={
            'actividad_ids':list_actividad,
            }
        return {'value':res}
        
    def onchange_cronograma_semestre(self, cr, uid, ids, context=None):
        res={}
        cronograma_semestre_obj=self.pool.get('unefa.cronograma_actividades_semestre')
        cronograma_semestre_ids=cronograma_semestre_obj.search(cr,uid,[('activo','=','True')],context=context)
        cronograma_semestre_datos=cronograma_semestre_obj.browse(cr,uid,cronograma_semestre_ids,context=context)
        list_actividad_semestre=[]
        for i in cronograma_semestre_datos:
            list_actividad_semestre.append([0,False,{'actividad_id':i.id }])
        res={
            'cronograma_actividad_ids':list_actividad_semestre,
            }
        return {'value':res}
    
    def aprobar_planificacion(self, cr, uid, ids, context=None):
        return self.write(cr, uid, ids, {'state':'aprobado'})
        
    def generar_cronograma(self, cr, uid, ids, context=None):
        return True
        
    def generar_planificacion(self, cr, uid, ids, context=None):
        return True
        
    def create(self,cr,uid,vals,context=None):
        ids=self.search(cr,uid,[('periodo_id','=',vals['periodo_id'])])
        if len(ids)==1:
            peridodo_obj=self.pool.get('unefa.conf.periodo_academico')
            periodo_ids=peridodo_obj.search(cr,uid,[('id','=',vals['periodo_id'])],context=context)
            periodo_datos=peridodo_obj.browse(cr,uid,periodo_ids,context=context)
            raise osv.except_osv(('Error !'), ('Ya existe un Cronograma Académico con el periodo '+periodo_datos['periodo_academico'].upper()+' no esta asignado al parque.'))
        return super(unefa_planificacion_semestre,self).create(cr,uid,vals,context=context)
    
    
class cronograma_inscripcion(osv.osv):
    _name = 'unefa.cronograma_inscripcion'

    
    _columns = {
        'planif_id': fields.many2one(
                                'unefa.planificacion_semestre',
                                'Actividad'
                                ),
        'actividad_id': fields.many2one(
                                    'unefa.cronograma_actividades_inscripcion',
                                    'Actividad',
                                    readonly=True,
                                    ),
        'fecha_desde': fields.date(
                                    'Fecha Inicio',
                                    required=True,
                                    ),
        'fecha_hasta': fields.date(
                                    'Fecha Final',
                                    required=True,
                                    ),
    }
    
    
        
    
    def onchange_fecha(self, cr, uid, ids, fecha_desde, fecha_hasta, context=None):
        res={}
        warning={}
        if fecha_desde:
            if cmp(fecha_desde,fecha_hasta)==1:
                res={
                    'fecha_hasta':'',
                    }
                warning={
                    'title':('Error de fechas'),
                    'message':('La fecha de inicio no puede ser mayo a la fecha final'),
                    }
        else:
            res={
                'fecha_hasta':'',
                }
            warning={
                    'title':('Error'),
                    'message':('Debe seleccionar una fecha de inicio'),
                    }
            
        return {'warning':warning,'value':res}
                
           


class cronograma_actividades(osv.osv):
    _name = 'unefa.cronograma_actividades'
    _description = 'Cronograma de actividades'
    
    _columns = {
        'crono_activ_id': fields.many2one(
                                    'unefa.planificacion_semestre',
                                    'Actividad'
                                    ),
        'actividad_id': fields.many2one(
                                    'unefa.cronograma_actividades_semestre',
                                    'Actividad',
                                    readonly=True,
                                    ),
        'fecha_desde': fields.date(
                                    'Fecha Inicio',
                                    required=True,
                                    ),
        'fecha_hasta': fields.date(
                                    'Fecha Final',
                                    required=True,
                                    ),
        'actividades': fields.char(
                                    'Actividades', 
                                    ),
        'responsable_id': fields.many2one(
                                    'unefa.responsable',
                                    'Responsable',
                                    required=True,
                                    ),
        'observaciones': fields.text(
                                    'Observaciones'
                                    ),
                }
    
    def onchange_fecha_actividad(self, cr, uid, ids, fecha_desde, fecha_hasta, context=None):
        res={}
        warning={}
        validar_fecha=self.pool.get('unefa.cronograma_inscripcion').onchange_fecha(cr, uid, ids, fecha_desde, fecha_hasta, context)
        warning=validar_fecha.values()[0]
        res=validar_fecha.values()[1]
        return {'warning':warning,'value':res}


