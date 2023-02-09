from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _
from odoo.exceptions import UserError

class LmEstados(models.Model):
    _name = "lm.busquedas.stage"
    _description = "Busquedas Stages"
    _order = 'sequence'
 

    name = fields.Char("Stage Name", required=True, translate=True)
    sequence = fields.Integer(
        "Sequence", default=10,
        help="Gives the sequence order when displaying a list of stages.")
    requirements = fields.Text("Requirements")