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
from datetime import datetime, date, time, timedelta
import time


class res_users(osv.Model):
    _inherit= "res.users"
    _rec_name="cedula"
    
    #~ _columns= {
        #~ 'cedula_id':fields.many2one('unefa.convalidacion','Contactos'),
    #~ }
    #~ 
class unefa_convalidacion(osv.osv):
    _name="unefa.convalidacion"
    #~ _inherit="unefa.estudiantes"
    #~ _rec_name="cedula"

    _columns={
        'cedula_id':fields.many2one('res.users','Cédula', required=True),
        'user_id':fields.many2one('unefa.estudiantes','Nombre completo', readonly=True),
        'current_date':fields.datetime('Fecha Actual', required=True, readonly=True),
        'condicion':fields.selection([('civil','Civil'),('militar', 'Militar')],'Condición'),
        'pensum':fields.many2one('unefa.pensum','Pensum', required=True), 
        'semestre':fields.many2one('unefa.semestre','Semestre', required=True), 
        'periodo':fields.char('Periodo', required=True),
        'carrera':fields.char('Carrera', readonly=True), 
        'regimen':fields.char('Regimen', readonly=True), 
        'materia_id':fields.many2many('unefa.materia','unefa_materia_rel','materia_id','relacion_id','Materias'), 
    }

    _defaults = {
        'current_date': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'),
        'carrera': 'Ingeniería de Sistemas',
        'regimen': 'Nocturno',
    }

    def onchange_nombre_estudiante(self,cr,uid,ids,cedula):
        res={}
        nombre_estudiante_obj=self.pool.get('unefa.estudiantes')
        nombre_estudiante_id=nombre_estudiante_obj.search(cr,uid,[('user_id','=',cedula)])
        nombre_estudiante_data=nombre_estudiante_obj.browse(cr,uid,nombre_estudiante_id)
        
        for i in nombre_estudiante_data:
            res={
                'user_id':i.id,
            }
        return {'value':res}
            
