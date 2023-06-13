from odoo import models, fields, _

class algoritma_pembelian(models.Model):
    _name = 'algoritma.pembelian'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal")
    status = fields.Selection([('draft','Draft'),('to_approve','To Approve'),('approved','Approved'),('done','Done')], default='draft')
    algoritma_pembelian_ids = fields.One2many('algoritma.pembelian.line', 'algoritma_pembelian_id', string="Algoritma Pembelian Ids")

class algoritma_pembelian_line(models.Model):
    _name = 'algoritma.pembelian.line'

    algoritma_pembelian_id = fields.Many2one('algoritma.pembelian', string="Algoritma Pembelian Id")
    product_id = fields.Many2one('product.product', string="Product Id")
    quantity = fields.Float(string="Quantity", default=0.0)
    uom_id = fields.Many2one('uom.uom', string="Uom Id")