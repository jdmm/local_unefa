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
# from json import dumps, loads, JSONEencoder, JSONDecoder
from dateutil.relativedelta import * 
from openerp import tools


class unefa_estudiantes(osv.osv):
    _name = "unefa.estudiantes"
    _inherits = {'res.users':'user_id'}


    _columns={
        'user_id':fields.many2one('res.users','Usuarios'),

        
    }
    
    def on_change_login(self, cr, uid, ids, login, context=None):
        users_obj=self.pool.get('res.users')
        users_id=users_obj.on_change_login(cr,uid,ids,login,context)
        return users_id
    
    _defaults={
        'is_estudiante':True,
    }
    
class unefa_profesores(osv.osv):
    _name = "unefa.profesores"
    _inherits = {'res.users':'user_id'}

    def _get_attachment_number(self, cr, uid, ids, fields, args, context=None):
        res = dict.fromkeys(ids, 0)
        for app_id in ids:
            res[app_id] = self.pool['ir.attachment'].search_count(cr, uid, [('res_model', '=', 'unefa.profesores'), ('res_id', '=', app_id)], context=context)
        return res
        
    _columns={
        'user_id':fields.many2one('res.users','Usuarios'),
        'attachment_number': fields.function(_get_attachment_number, string='Number of Attachments', type="integer"),

        
    }
    
    def on_change_login(self, cr, uid, ids, login, context=None):
        users_obj=self.pool.get('res.users')
        users_id=users_obj.on_change_login(cr,uid,ids,login,context)
        return users_id
        
    def action_get_attachment_tree_view(self, cr, uid, ids, context=None):
        model, action_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'base', 'action_attachment')
        action = self.pool.get(model).read(cr, uid, action_id, context=context)
        action['context'] = {'default_res_model': self._name, 'default_res_id': ids[0]}
        action['domain'] = str(['&', ('res_model', '=', self._name), ('res_id', 'in', ids)])
        return action
    
    _defaults={
        'is_profesor':True,
    }
    
    
    
class unefa_coordinador(osv.osv):
    _name = "unefa.coordinador"
    _inherits = {'res.users':'user_id'}

    def _get_attachment_number(self, cr, uid, ids, fields, args, context=None):
        res = dict.fromkeys(ids, 0)
        for app_id in ids:
            res[app_id] = self.pool['ir.attachment'].search_count(cr, uid, [('res_model', '=', 'unefa.coordinador'), ('res_id', '=', app_id)], context=context)
        return res
        
        
    _columns={
        'user_id':fields.many2one('res.users','Usuarios'),
        'attachment_number': fields.function(_get_attachment_number, string='Number of Attachments', type="integer"),

        
    }
    
    def on_change_login(self, cr, uid, ids, login, context=None):
        users_obj=self.pool.get('res.users')
        users_id=users_obj.on_change_login(cr,uid,ids,login,context)
        return users_id
        
    def action_get_attachment_tree_view(self, cr, uid, ids, context=None):
        model, action_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'base', 'action_attachment')
        action = self.pool.get(model).read(cr, uid, action_id, context=context)
        action['context'] = {'default_res_model': self._name, 'default_res_id': ids[0]}
        action['domain'] = str(['&', ('res_model', '=', self._name), ('res_id', 'in', ids)])
        return action
    
    _defaults={
        'is_coordinador':True,
    }
    
    
class unefa_secretariado(osv.osv):
    _name = "unefa.secretariado"
    _inherits = {'res.users':'user_id'}


    def _get_attachment_number(self, cr, uid, ids, fields, args, context=None):
        res = dict.fromkeys(ids, 0)
        for app_id in ids:
            res[app_id] = self.pool['ir.attachment'].search_count(cr, uid, [('res_model', '=', 'unefa.secretariado'), ('res_id', '=', app_id)], context=context)
        return res

    _columns={
        'user_id':fields.many2one('res.users','Usuarios'),
        'attachment_number': fields.function(_get_attachment_number, string='Number of Attachments', type="integer"),

        
    }
    
    def on_change_login(self, cr, uid, ids, login, context=None):
        users_obj=self.pool.get('res.users')
        users_id=users_obj.on_change_login(cr,uid,ids,login,context)
        return users_id
        
    def action_get_attachment_tree_view(self, cr, uid, ids, context=None):
        model, action_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'base', 'action_attachment')
        action = self.pool.get(model).read(cr, uid, action_id, context=context)
        action['context'] = {'default_res_model': self._name, 'default_res_id': ids[0]}
        action['domain'] = str(['&', ('res_model', '=', self._name), ('res_id', 'in', ids)])
        return action
    
    _defaults={
        'is_secretaria':True,
    }
    
class unefa_evaluador(osv.osv):
    _name = "unefa.evaluador"
    _inherits = {'res.users':'user_id'}

    
    def _get_attachment_number(self, cr, uid, ids, fields, args, context=None):
        res = dict.fromkeys(ids, 0)
        for app_id in ids:
            res[app_id] = self.pool['ir.attachment'].search_count(cr, uid, [('res_model', '=', 'unefa.evaluador'), ('res_id', '=', app_id)], context=context)
        return res
        
        
    _columns={
        'user_id':fields.many2one('res.users','Usuarios'),
        'attachment_number': fields.function(_get_attachment_number, string='Number of Attachments', type="integer"),

        
    }
    
    def on_change_login(self, cr, uid, ids, login, context=None):
        users_obj=self.pool.get('res.users')
        users_id=users_obj.on_change_login(cr,uid,ids,login,context)
        return users_id
        
    def action_get_attachment_tree_view(self, cr, uid, ids, context=None):
        model, action_id = self.pool.get('ir.model.data').get_object_reference(cr, uid, 'base', 'action_attachment')
        action = self.pool.get(model).read(cr, uid, action_id, context=context)
        action['context'] = {'default_res_model': self._name, 'default_res_id': ids[0]}
        action['domain'] = str(['&', ('res_model', '=', self._name), ('res_id', 'in', ids)])
        return action
    
    _defaults={
        'is_evaluador':True,
    }
    
    
