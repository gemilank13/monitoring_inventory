# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class JppiProduct(models.Model):
    _name = 'jppi.product'
    _description = 'Products'

    name = fields.Many2one('jppi.master', string="Item Description", required=True)
    item_code = fields.Char(string="Item Code", related="name.item_code")
    sub_inventory_id = fields.Many2one('jppi.subinventory', string="Sub Inventory")
    qty_oh = fields.Float(string="Qty O.H")
    uom_id = fields.Many2one('jppi.uom', string="Uom")
    avg_cost = fields.Float(string="Avg Cost")
    cost_amount = fields.Float(string="Cost Amount")
    location_id = fields.Many2one('jppi.location', string="Location")


class JppiMaster(models.Model):
    _name = 'jppi.master'
    _description = 'Master Products'

    name = fields.Char(string="Product Name", required=True)
    item_code = fields.Char(string="Item Code")


class JppiSubinventory(models.Model):
	_name = "jppi.subinventory"
	_description = "Sub Inventory"
	_rec_name = 'short_name'

	name = fields.Many2one('jppi.location', string="Location Name", required=True)
	short_name = fields.Char(string="Short Name")
	partner_id = fields.Many2one('res.partner', string="Address")


class JppiUom(models.Model):
	_name = "jppi.uom"
	_description = "Uom"

	name = fields.Char(string="Unit of Measure", required=True)

class JppiLocation(models.Model):
	_name = "jppi.location"
	_description = "Location"

	name = fields.Char(string="Location Name", required=True)