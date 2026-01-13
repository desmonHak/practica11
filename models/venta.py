from odoo import models, fields, api

class ConcesionarioVenta(models.Model):
    _name = "concesionario.venta"
    _description = "Venta"

    name = fields.Char(
        default=lambda self: "VENTA-" + fields.Date.today().strftime("%Y%m%d")
    )

    cliente_id = fields.Many2one(
        "concesionario.cliente",
        required=True
    )

    coche_id = fields.Many2one(
        "concesionario.coche",
        required=True
    )

    vendedor_id = fields.Many2one(
        "concesionario.vendedor"
    )

    precio_final = fields.Float(
        related="coche_id.precio",
        store=True
    )