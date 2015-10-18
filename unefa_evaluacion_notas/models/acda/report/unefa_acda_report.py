 # -*- encoding: utf-8 -*-

from openerp.osv import osv
import time
from openerp.report import report_sxw

class unefa_acda_report(report_sxw.rml_parse):
   
    def __init__(self , cr, uid, name, context):
        super(unefa_acda_report,self).__init__(cr,uid,name,context)
        self.localcontext.update({
            'time':time,
        })
        self.context = context
    
        
class report_unefa_acda(osv.AbstractModel):
    _name = "unefa_acta_contrato_aprendizaje.report.id_template_unefa_acda_qweb"
    _inherit = "report.abstract_report"
    _template = "unefa_acta_contrato_aprendizaje.id_template_unefa_acda_qweb"
    _wrapped_report_class = unefa_acda_report
    
# report_sxw.report_sxw('unefa_pensum', 'unefa.pensum', 'local_addons/unefa_pensum/report/unefa_pensum.rml', parser=unefa_pensum_report)
