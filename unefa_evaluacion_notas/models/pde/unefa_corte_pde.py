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

class unefa_corte_pde(osv.osv):
    
    _name = "unefa.corte.pde"
    _rec_name = 'corte'
    
    _columns = {
	'corte':fields.selection([('1','1'),('2','2'),('3','3'),('4','4')],'corte', help='Seleccion de corte'),
	'evaluacion_pde_ids':fields.one2many('unefa.evaluacion.pde','evaluacion_pde_id','Evaluacion', required=True),
	'corte_pde_id':fields.many2one('unefa.plan.evaluacion','Corte'),
    }
 
