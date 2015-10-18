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

class unefa_prueba_rep(osv.osv):
    _name="unefa.prueba_rep"
    
    _columns={
        'cronograma_rep_id': fields.many2one('unefa.cronograma_rep','Cronograma'),
        'profesor_id': fields.many2one('res.users','Profesor',readonly=True,required=False),
        'periodo_id': fields.many2one('unefa.conf.periodo_academico','Periodo Académico',readonly=True,required=False),
        'semestre_id': fields.many2one('unefa.semestre','Semestre',readonly=True,required=False),
        'materia_id': fields.many2one('unefa.materia','Materia'),
        #~ 'codigo': fields.many2one('unefa.materia','Codigo'),
        #~ 'credito': fields.many2one('unefa.materia','UC'),
        'seccion_id': fields.many2one('unefa.seccion','Seccion'),
        'correlativo':fields.char('Correlativo',size=10),
        'notas_rep_ids': fields.one2many('unefa.notas_rep','prueba_rep_id',''),
        'state': fields.selection([
            ('borrador', 'Borrador'),
            ('aprobado', 'Aprobado'),
            ('finalizado', 'Finalizado'),
            ], 'Estado', readonly=True, copy=False, help="Este es es estado actual de la prueba.", select=True),
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
        #~ res={
            #~ 'profesor_id':res_user_datos['name'],
            #~ 'periodo_id':unefa_conf_periodo_academico_datos['periodo_academico'],
            #~ 'semestre_id':unefa_semestre_datos['nombre'],
            #~ 'materia__id':unefa_materia_datos['materia'],
            #~ 'codigo':unefa_materia_datos['codigo'],
            #~ 'credito':unefa_materia_datos['uc'],
            #~ 'seccion':unefa_conf_seccion_datos['seccion'],
        #~ }
        #~ return {'value':res}
        return True

    def asignar_correlativo():
        return True    
        
    def verificar_autoevaluacion():
        return True
    
    

class unefa_notas_rep(osv.osv):
    _name="unefa.notas_rep"
    _rec_name = "nota_rep"
    
    _columns={
        'prueba_rep_id': fields.many2one('unefa.prueba_rep',''),
        #~ 'numero' : fields.integer('N°',size=2),
        'estudiante_id': fields.many2one('res.users','Cedula'),
        'nombre_estudiante':fields.many2one('res.users','Nombre y Apellido',readonly=True,required=False),
        'nota_rep':fields.integer('Nota en numeros',size=2,required=False,help='Introduzca un valor entre 1 y 20'),
        'nota_letras':fields.char('Nota en letras',size=10,readonly=True,required=False),
        'aprobado':fields.boolean(),
    }
    
    _defaults={
        'aprobado': False,
    }
    
    def onchange_cargar_datos(self, cr, uid, ids, context=None):
        #~ res={}
        #~ res_user_obj=self.pool.get('res.users')
        #~ res_user_ids=res_user_obj.search(cr,uid,[('id','=',uid)],context=context)
        #~ res_user_datos=res_user_obj.browse(cr,uid,res_user_ids,context=context)
        #~ 
        #~ res={   
            #~ 'estudiante_id':res_user_datos['cedula'],
            #~ 'nombre_estudiante':res_user_datos['name'],
        #~ }
        #~ return {'value':res}
        return True
        
    #~ En el metodo onchange_asignar_valor se asigna el valor en letras correspondiente
    #~ a su equivalente numerico intoducido por el usuario, al mismo tiempo si es superior
    #~ a 10 (DIEZ) se sobreescribe el valor por defecto de aprobado a True
    #~ adicionalmente muestra un warning si el valor introducido por el usuario
    #~ es menor a 0 (CERO) o superior a 20 (VEINTE)
    def onchange_asignar_valor(self, cr, uid, ids, nota_rep, context=None):
        res={}
        
        valor = ["","UNO","DOS" ,"TRES" ,"CUATRO","CINCO","SEIS","SIETE",
                "OCHO","NUEVE","DIEZ", "ONCE","DOCE","TRECE","CATORCE","QUINCE", 
                "DIECISEIS","DIECISIETE","DIECIOCHO","DIECINUEVE", "VEINTE" ]
        
        if (nota_rep >= 0 and nota_rep <= 20):
            nota_letras = valor[nota_rep]
            res = {
                'nota_letras':valor[nota_rep],
                'nota_rep':nota_rep,}
            if (nota_rep >= 10):
                aprobado = True
                res = {
                    'nota_rep':nota_rep,
                    'aprobado':True,
                    'nota_letras':valor[nota_rep],
                    }
                return {'value':res}
            return {'value':res}
        else:
            warning = {
            'title':'Error',
            'message':'La nota debe estar comprendida entre 1 y 20'
            }
            return {'warning': warning, 'value': res}
     
    def create(self,cr,uid,vals,context=None):
        res = {}
        nota_rep = vals['nota_rep']
        res=self.onchange_asignar_valor(self, cr, uid, nota_rep, context=None)
        res=res.values()
        res=res[0]
        #~ borrar esta linea luego se queda la de res1
        res.update(res)
        #~ res1=self.onchange_cargar_datos(cr, uid, [], context=None)
        #~ res1=res1.values()
        #~ res1=res1[0]
        #~ res.update(res1)
        h=super(unefa_notas_rep, self).create(cr, uid, vals, context=context)
        self.write(cr,uid,h,res,context=context)
        return h
        
    #~ El metodo validar_nota ejecuta un constraint que evita las notas introducidas por el usuario
    #~ fuera del rango permitido, minimo 1 (UNO) y maximo 20 (VEINTE)
    def validar_nota(self, cr, uid, ids, context=None):
        for notas_rep in self.browse(cr, uid, ids, context=context):
            if (notas_rep.nota_rep < 1 or notas_rep.nota_rep > 20):
                return False
            return True
     
    _constraints = [
        (validar_nota, 'Error ! La nota introducida no es valida' , ["nota_rep"])
    ]
