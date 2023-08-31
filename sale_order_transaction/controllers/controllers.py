# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderTransaction(http.Controller):
#     @http.route('/sale_order_transaction/sale_order_transaction', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_transaction/sale_order_transaction/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_transaction.listing', {
#             'root': '/sale_order_transaction/sale_order_transaction',
#             'objects': http.request.env['sale_order_transaction.sale_order_transaction'].search([]),
#         })

#     @http.route('/sale_order_transaction/sale_order_transaction/objects/<model("sale_order_transaction.sale_order_transaction"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_transaction.object', {
#             'object': obj
#         })
