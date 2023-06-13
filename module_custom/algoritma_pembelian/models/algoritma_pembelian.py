from odoo import models, fields, _

class algoritma_pembelian(models.Model):
    _name = 'algoritma.pembelian'

    name = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal")
    status = fields.Selection([('draft','Draft'),('to_approve','To Approve'),('approved','Approved'),('done','Done')], default='draft')