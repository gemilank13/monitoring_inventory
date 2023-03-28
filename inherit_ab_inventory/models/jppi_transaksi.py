# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class JppiTransaksi(models.Model):
    _name = 'jppi.transaksi'
    _description = 'Transaction'

    name = fields.Char(string="Product Name", required=True)
    item_code = fields.Char(string="Item Code")
    tr_date = fields.Date(string="Transaction Date")
    sub_inventory_id = fields.Many2one('jppi.subinventory', string="Sub Inventory")
    tr_type_id = fields.Many2one('jppi.tr.type', string="transaction Type")
    no_wo = fields.Char(string="No WO/No PO")
    no_ttb = fields.Char(string="No TTB/No SPBG")
    asset = fields.Char(string="Asset")
    uom_id = fields.Many2one('jppi.uom', string="Uom")
    wo_type_id = fields.Many2one('jppi.wo.type', string="WO Type")
    qty_receive = fields.Float(string="Qty Receive")
    qty_issue = fields.Float(string="Qty Issue")
    unit_price = fields.Float(string="Unit Price")
    value_receive = fields.Float(string="Value Receive/Issued")
    keterangan = fields.Text(string="Keterangan")

class JppiTrType(models.Model):
    _name = 'jppi.tr.type'
    _description = 'Transaction Type'

    name = fields.Char(string="Transaction Type", required=True)

class JppiWOType(models.Model):
    _name = 'jppi.wo.type'
    _description = 'WO Type'

    name = fields.Char(string="WO Type", required=True)