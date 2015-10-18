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
#from json import dumps, loads, JSONEencoder, JSONDecoder
from dateutil.relativedelta import * 

class unefa_materia (osv.osv):
     
    _name="unefa.materia"
    _rec_name="materia"
    
        
    _columns={
        
        'materia':fields.char('Materia', required=True,help='ejemplo: "Matemática"'),
        'materia_ids':fields.one2many('unefa.contenido','materia_id','Relacion_contenido_materia'),
        'codigo':fields.char('Codigo',size=10,required=True,help='ejemplo: "Mat010101"'),
        'teoria':fields.selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')],'Horas teoricas',required=True),
        'practica':fields.selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5')],'Horas practicas',required=True),
        'laboratorio':fields.selection([('0','0'),('1','1'),('2','2'),('3','3'),('4','4')],'Horas de laboratorio', required=True),
        'uc':fields.selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6')],'Unidades de Credito',required=True),
        'prelacion':fields.many2many('unefa.materia','rel_pre_mat','relacion_id','materia_id','Prelacion'),
    }
    
    
class unefa_semestre (osv.osv):
     
    _name="unefa.semestre"
    _rec_name="nombre"
    
        
    _columns={
        
        'nombre':fields.char('Semestre',size=20,required=True,help='ejemplo: "1er Semestre"'),
        'codigo':fields.char('Codigo',size=10,required=True,help='ejemplo: "1erSemIngSisD01"'),
        'semestre_id':fields.many2many('unefa.materia','rel_sem_mat','relacion_sem_id','materia_id','Semestre'),
    }
    
    
class unefa_pensum (osv.osv):
     
    _name="unefa.pensum"
    _rec_name="nombre"
    
        
    _columns={
        
        'nombre':fields.char('Pensum',size=20,required=True,help='ejemplo: "Pensum 2010"'),
        'codigo':fields.char('Codigo',size=20,required=True,help='ejemplo: "Pen2010SemIngSisD01"'),
        'fecha':fields.date('Fecha de elaboracion'),
        'pensum_id':fields.many2many('unefa.semestre','rel_pen_sem','relacion_pen_id','semestre_id','Pensum'),
        'attachment_ids': fields.many2many('ir.attachment', 'email_template_attachment_une', 'email_template_id', 'attachment_ids', 'Archivos Adjuntos'),
    }
    
class unefa_contenido (osv.osv):
     
    _name="unefa.contenido"
    _rec_name="nombre"
    
        
    _columns={
        
        'nombre':fields.char('Contenido',size=50,required=True,help='ejemplo: "Unidad I Metodologias de Desarrollo del Software"'),
        'codigo':fields.char('Codigo',size=20,required=True,help='ejemplo: "Pen2010SemIngSisD01"'),
        'fecha':fields.date('Fecha de elaboracion'),
        'contenido_id':fields.many2many('unefa.subcontenido','rel_cont_subcont','relacion_cont_id','subcontenido_id','Contenido'),
        'materia_id':fields.many2one('unefa.materia',"Materia"),
    }
    
    
class unefa_subcontenido (osv.osv):
     
    _name="unefa.subcontenido"
    _rec_name="subcontenido"
    
        
    _columns={
        
        'subcontenido':fields.char('Sub-contenido',size=200,required=True,help='ejemplo: "Analisar las metodologias de desarrollos del software (metodologias agiles, xtreme programing, rup, scrum entre otras)"'),
        'indice':fields.selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')],'Indice',required=True),
    }
