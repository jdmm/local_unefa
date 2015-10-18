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


class unefa_evaluacion_continua(osv.osv):
    _name = "unefa.evaluacion.continua"
    #~ _rec_name = 'evaluacion_continua_id'
    
    _columns = {
        'estudiante_id':fields.many2one('unefa.lista_estudiantes_prueba','Estudiante',readonly=True,),
        'ep1': fields.integer("EP1",size=10, required=False, readonly=False, help='Nota de la evaluacion continua numero uno'),
        'ep2': fields.integer("EP2",size=10, required=False, readonly=False, help='Nota de la evaluacion continua numero dos'),
        'ep3': fields.integer("EP3",size=10, required=False, readonly=False, help='Nota de la evaluacion continua numero tres'),
        'ep4': fields.integer("EP4",size=10, required=False, readonly=False, help='Nota de la evaluacion continua numero cuatro'),
        'nota_final':fields.integer('Nota Final',size=2, required=True,readonly=True, help='Nota del estudiante'),
        'nota_letras':fields.char('Nota Letras',size=20,required=True,readonly=True, help='Nota en letra del estudiante'),
        'evaluacion_continua_id':fields.many2one('unefa.cdn','Evaluaciones'),
        'aprobado':fields.boolean("Aprobado", readonly=True),
 }
 
    _defaults={
        'aprobado': False,
    }
 
    def onchange_asignar_valor(self, cr, uid, ids, ep1,ep2,ep3,ep4, context=None):
        res={}        
        
        valor = ["","UNO","DOS" ,"TRES" ,"CUATRO","CINCO","SEIS","SIETE",
                "OCHO","NUEVE","DIEZ", "ONCE","DOCE","TRECE","CATORCE","QUINCE", 
                "DIECISEIS","DIECISIETE","DIECIOCHO","DIECINUEVE", "VEINTE" ]
        
        if ((ep1 >= 0 and ep1 <= 20)or(ep2 >= 0 and ep2 <= 20)or(ep3 >= 0 and ep3 <= 20)or(ep4 >= 0 and ep4 <= 20)):
            nota_final = (ep1+ep2+ep3+ep4)/4
            nota_letras = valor[nota_final]
            res = {
                'nota_letras':nota_letras,
                'nota_final':nota_final,}
            if (nota_final >= 10):
                aprobado = True
                res = {
                    'nota_final':nota_final,
                    'aprobado':True,
                    'nota_letras':nota_letras,
                    }
                return {'value':res}
            else:
                aprobado = False
                res = {
                    'nota_final':nota_final,
                    'aprobado':False,
                    'nota_letras':nota_letras,
                    }
            return {'value':res}
        else:
            warning = {
            'title':'Error',
            'message':'La nota debe estar comprendida entre 1 y 20'
            }
            return {'warning': warning, 'value': res}
            
    #~ def validar_nota(self, cr, uid, ids, context=None):
        #~ for notas_rep in self.browse(cr, uid, ids, context=context):
            #~ if (notas_rep.nota_rep < 1 or notas_rep.nota_rep > 20):
                #~ return False
            #~ return True
     #~ 
    #~ _constraints = [
        #~ (validar_nota, 'Error ! La nota introducida no es valida' , ["nota_rep"])
    #~ ]
    
    

 
