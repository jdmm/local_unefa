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

class unefa_evaluacion_pde(osv.osv):
     
    _name = "unefa.evaluacion.pde"
    _rec_name = 'evaluacion'
     
    _columns = {
	#~ 'corte_pde_ids':fields.many2many('unefa.corte.pde','unefa_evaluacion_corte_pde','corte_pde_id','evaluacion_pde_id','Cortes'),
        'evaluacion':  fields.many2one ('unefa.tipo.evaluacion','Tipo Evaluacion', required=True),
	'evaluacion_pde_id':fields.many2one('unefa.corte.pde','Evaluacion'),
        'ponderacion': fields.selection([('five','5%'),('ten','10%'),('fifty','15%'),('twenty','20%'),('twenty five','25%')],'Ponderacion', help='Seleccion de ponderacion de la evaluacion'),
        'fecha':fields.date('Fecha de Evaluacion',required=True),
        'contenido': fields.many2one ('unefa.contenido.pde','Contenido', required=True),
        'semana': fields.char("Semana",size=20,required=False, help="semana"),
        'observaciones': fields.text('Observaciones'),
     
     }
  
