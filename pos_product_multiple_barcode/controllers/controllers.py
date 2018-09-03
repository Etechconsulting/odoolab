# -*- coding: utf-8 -*-
from odoo import http

# class PosProductMultipleBarcode(http.Controller):
#     @http.route('/pos_product_multiple_barcode/pos_product_multiple_barcode/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_product_multiple_barcode/pos_product_multiple_barcode/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_product_multiple_barcode.listing', {
#             'root': '/pos_product_multiple_barcode/pos_product_multiple_barcode',
#             'objects': http.request.env['pos_product_multiple_barcode.pos_product_multiple_barcode'].search([]),
#         })

#     @http.route('/pos_product_multiple_barcode/pos_product_multiple_barcode/objects/<model("pos_product_multiple_barcode.pos_product_multiple_barcode"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_product_multiple_barcode.object', {
#             'object': obj
#         })