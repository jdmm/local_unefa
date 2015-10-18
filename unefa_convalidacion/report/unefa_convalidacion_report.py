# -*- encoding: utf-8 -*-

from openerp.osv import osv
import time
from openerp.report import report_sxw
from datetime import datetime

class unefa_convalidacion_report(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
        super(unefa_convalidacion_report,self).__init__(cr,uid,name,context)
        self.localcontext.update({
            'time': time,
            
        
        })
        self.context = context


class report_unefa_convalidacion(osv.AbstractModel):
    _name = "report.unefa_convalidacion.id_unefa_convalidacion_report_qweb"
    _inherit = "report.abstract_report"
    _template = "unefa_convalidacion.id_unefa_convalidacion_report_qweb"
    _wrapped_report_class = unefa_convalidacion_report
        

# report_sxw.report_sxw('unefa_convalidacion.models', 'unefa.convalidacion', 'unefa_convalidacion/report/id_unefa_convalidacion_report_qweb.rml',parser=unefa_convalidacion_report)
