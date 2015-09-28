# -*- coding: utf-8 -*-
import time
from openerp.osv import fields, osv

class coordinacion(osv.osv):
    _name='unefa.coordinacion'
    _rec_name='nombre'
    
    _columns={
        'nombre':fields.char('Nombre',size=80,
            required=True,help='Aquí se coloca el nombre del nucleo'),
        'regimen':fields.selection(
            [('Diurno','Diurno'),('Nocturno','Nocturno')], 
            'Regimen',required=True,help="""Regimen"""),
        'descripcion':fields.text('Descripcion',
            help='Aquí se coloca la descripcion de la coordinacion'),
        'ubicacion':fields.char('Codigo',
            help='Aquí se coloca el codigo de la coordinacion'),
        'telefono':fields.char('Telefono',
            help='Aquí se coloca el telefono de la coordinacion'),
        'email':fields.char('Email',
            help='Aquí se coloca el Email de la coordinacion'),
        'carrera_ids':fields.many2many('unefa.carrera',
            'unefa_carrera_coordinacion', 'coordinacion_id',
            'carrera_id', 'Carrera'),
        'user_ids':fields.many2many('res.users',
            'cfg_coordinacion_usuarios','coordinacion_ids',
            'usuarios_ids','Usuarios',),
        'active':fields.boolean('Activo',
            help='Si esta activo el motor lo incluira en la vista...'),
    }
    
    _defaults={
        'active':True,
    }
