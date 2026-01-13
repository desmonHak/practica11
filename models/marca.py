from odoo import models, fields

class ConcesionarioMarca(models.Model):
    _name = "concesionario.marca"
    _description = "Marca"

    name = fields.Char(required=True)

    coche_ids = fields.One2many(
        "concesionario.coche",
        "marca_id",
        string="Coches"
    )