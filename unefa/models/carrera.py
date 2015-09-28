# -*- coding: utf-8 -*-
import time
from openerp.osv import fields, osv

class carrera(osv.osv):
    _name='unefa.carrera'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre',size=80,required=True,help='Aquí se coloca el nombre del nucleo'),
        'codigo':fields.char('Codigo',help='Aquí se coloca el codigo de la carrera'),
        'nucleo_ids':fields.many2many('unefa.nucleo','unefa_nucleo_carrera', 'carrera_id','nucleo_id', 'Nucleos'),
        'tipo':fields.selection([('corta','Carrera Corta'),('larga','Carrera Larga')],'Tipo', required=True, help='Aquí se coloca el Telefono del nucleo'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
    }
    
    _defaults={
        'active':True,
    }
