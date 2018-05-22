from odoo import models, fields

class PurchaseCustom(models.Model):
    
    _inherit = "purchase.order" #nama model yang ingin kita tambahi field

    deadline = fields.Date("Deadline")
