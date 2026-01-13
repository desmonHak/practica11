from odoo import models, fields

class ConcesionarioVendedor(models.Model):
    _name = "concesionario.vendedor"
    _description = "Vendedor"

    name = fields.Char(required=True)

    venta_ids = fields.One2many(
        "concesionario.venta",
        "vendedor_id"
    )
