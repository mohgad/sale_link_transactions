from odoo import models, fields,api
 
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_transaction_id = fields.One2many(
        'payment.transaction', 'sale_order_ids', 
        string='Payment Transactions',
        domain="[('sale_order_ids', '=', id)]",
        help="Payment transactions related to this sale order"
    ) 
