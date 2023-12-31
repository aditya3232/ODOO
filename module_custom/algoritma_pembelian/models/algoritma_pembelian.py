from odoo import models, fields, api, _

class algoritma_pembelian(models.Model):
    _name = 'algoritma.pembelian'

    # button dengan function
    def func_to_approve(self):
        if self.status == 'draft':
            self.status = 'to_approve'
    
    def func_approved(self):
        if self.status == 'to_approve':
            self.status = 'approved'

    def func_done(self):
        if self.status == 'approved':
            self.status = 'done'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal")
    status = fields.Selection([('draft','Draft'),('to_approve','To Approve'),('approved','Approved'),('done','Done')], default='draft')
    algoritma_pembelian_ids = fields.One2many('algoritma.pembelian.line', 'algoritma_pembelian_id', string="Algoritma Pembelian Ids")
    brand_ids = fields.Many2many('algoritma.brand', 'algoritma_pembelian_brand_rel', 'algoritma_pembelian_id', 'brand_id', string='Brand Ids')

class algoritma_pembelian_line(models.Model):
    _name = 'algoritma.pembelian.line'

    @api.onchange('product_id')
    def func_onchange_product_id(self):
        if not self.product_id:
            return ()
        else:
            self.description = self.product_id.name
        return {}
    
    def _func_amount_total(self):
        for line in self:
            line.sub_total = line.quantity * line.price

    algoritma_pembelian_id = fields.Many2one('algoritma.pembelian', string="Algoritma Pembelian Id")
    product_id = fields.Many2one('product.product', string="Product Id")
    description = fields.Char(string="Description")
    quantity = fields.Float(string="Quantity", default=0.0)
    price = fields.Float(string="Price", default=0.0)
    sub_total = fields.Float(string="Sub Total", compute=_func_amount_total)
    uom_id = fields.Many2one('uom.uom', string="Uom Id")

class algoritma_brand(models.Model):
    _name = 'algoritma.brand'

    name = fields.Char(string="Name")