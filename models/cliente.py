from odoo import models, fields

class ConcesionarioCliente(models.Model):
    _name = "concesionario.cliente"
    _description = "Cliente"

    name = fields.Char(required=True)
    email = fields.Char()

    coche_favorito_ids = fields.Many2many(
        "concesionario.coche",
        "cliente_coche_favorito_rel",  # nombre de la tabla intermedia
        "cliente_id",                  # columna que apunta a cliente
        "coche_id",                    # columna que apunta a coche
        string="Coches favoritos"
    )
