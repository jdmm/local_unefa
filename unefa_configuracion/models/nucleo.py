# -*- coding: utf-8 -*-
import time
from openerp.osv import fields, osv

class nucleo(osv.osv):
    _name='unefa.nucleo'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre',size=80,required=True,help='Aquí se coloca el nombre del nucleo'),
        'direccion':fields.text('Dirección',help='Aquí se coloca el dirección del estudiante'),
        'universidad_id':fields.many2one('res.company', 'Universidad',help='Aquí se coloca el dirección del estudiante'),
        'carrera_ids':fields.many2many('unefa.carrera','unefa_nucleo_carrera', 'nucleo_id','carrera_id', 'Carreras'),
        'telefono':fields.char('Teléfono',size=64,required=True,help='Aquí se coloca el Telefono del nucleo'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
    }
    
    _defaults={
        'active':True,
    }
