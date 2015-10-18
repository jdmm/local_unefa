# -*- coding: utf-8 -*-
import time
from openerp.osv import fields, osv

class coordinacion(osv.osv):
    _name='unefa.coordinacion'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre',size=80,required=True,help='Aquí se coloca el nombre de la Coordinación'),
        'descripcion':fields.text('Descripcion',help='Aquí se coloca la descripcion de la coordinación'),
        'ubicacion':fields.char('Ubicacion',help='Aquí se coloca la ubicación de la coordinación'),
        'telefono':fields.char('Telefono',help='Aquí se coloca el telefono de la coordinación'),
        'email':fields.char('Email',help='Aquí se coloca el Email de la coordinación'),
        'carrera_ids':fields.many2many('unefa.carrera','unefa_carrera_coordinacion', 'coordinacion_id','carrera_id', 'Carreras'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...'),
        'user_ids':fields.many2many('res.users','unefa_users_coordinacion', 'coordinacion_id','users_id', 'Encargados'),
    }
    
    _defaults={
        'active':True,
    }
