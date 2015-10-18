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

class unefa_cdn(osv.osv):
    _name = "unefa.cdn"
    _rec_name = 'corte_id'
    
    _columns = {
        #~ 'corte':fields.selection([('1','1er Corte'),('2','2do Corte'),('3','3er Corte'),('4','4to Corte')],'Corte', help='Seleccionar el corte para cargar las evaluaciones'),
        'corte_id':fields.many2one('unefa.lista_cortes_semestre','Corte',readonly=True,),
        'evaluacion_continua_ids':fields.one2many('unefa.evaluacion.continua','evaluacion_continua_id', 'Evaluaciones', required=True),
        'cdn_id':fields.many2one('unefa.carga.notas','Cortes'),
 }
 
    def onchange_lista_estudiantes_prueba(self, cr, uid, ids, context=None):
        res={}
        lista_estudiantes_obj=self.pool.get('unefa.lista_estudiantes_prueba')
        lista_estudiantes_ids=lista_estudiantes_obj.search(cr,uid,[('activo','=','True')],context=context)
        lista_estudiantes_datos=lista_estudiantes_obj.browse(cr,uid,lista_estudiantes_ids,context=context)
        lista_estudiantes=[]
        for i in lista_estudiantes_datos:
            lista_estudiantes.append([0,False,{'estudiante_id':i.id }])
        res={
            'evaluacion_continua_ids':lista_estudiantes,
            }
        return {'value':res}
    
    

 
