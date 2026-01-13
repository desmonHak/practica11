from odoo import models, fields

class ConcesionarioCliente(models.Model):
    _name = "concesionario.cliente"
    _description = "Cliente"

    name = fields.Char(required=True)
    email = fields.Char()

    coche_favorito_ids = fields.Many2many(
        "concesionario.coche",
        string="Coches favoritos"
    )