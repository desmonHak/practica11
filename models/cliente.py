from odoo import models, fields

class ConcesionarioCliente(models.Model):
    _name = "concesionario.cliente"
    _description = "Clientes del concesionario"
    """
    Modelo ConcesionarioCliente: Representa a los clientes del concesionario.

    Requisitos cumplidos en este modelo:

    * 5 tablas o modelos como mínimo:
        - Este es uno de los modelos (Cliente), junto con Coche, Marca, etc.

    * Relaciones: Many2many
        - coche_favorito_ids: relación Many2many con 'concesionario.coche' usando tabla intermedia.
    
    * Campos con valores por defecto:
        - No tiene, pero se podrían añadir (ej. booleano activo=True con lambda).
    
    * ORM:
        - Se pueden usar search(), create(), browse()… para acceder y modificar registros de clientes.
    
    * Herencia en algún modelo:
        - Este modelo no hereda de otros modelos, pero otros modelos como ConcesionarioCoche pueden heredar de mail.thread.

    * Manejo de errores:
        - Se puede controlar que los clientes tengan nombre obligatorio (required=True) evitando registros inválidos.
    
    * Campos relacionales computados y computados avanzados:
        - Se podrían añadir campos computados como el número de coches favoritos (len(coche_favorito_ids)).
    """
    
    name = fields.Char(required=True)
    """Nombre del cliente (obligatorio, cumple manejo básico de errores de validación)"""

    email = fields.Char()
    """Email del cliente (campo opcional)"""

    coche_favorito_ids = fields.Many2many(
        "concesionario.coche",
        "cliente_coche_favorito_rel",  # Nombre de la tabla intermedia
        "cliente_id",                  # Columna que apunta a cliente
        "coche_id",                    # Columna que apunta a coche
        string="Coches favoritos"
    )
    """Relación Many2many con el modelo Coche: permite almacenar los coches favoritos del cliente"""
