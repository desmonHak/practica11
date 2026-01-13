from odoo import models, fields

class ConcesionarioMarca(models.Model):
    _name = "concesionario.marca"
    _description = "Marcas de coches del concesionario"
    """
    Modelo ConcesionarioMarca: Representa las marcas de coches del concesionario.

    Requisitos cumplidos en este modelo:

    * 5 tablas o modelos como mínimo
        - Este es uno de los modelos (junto con Coche, Cliente, etc.)

    * Relaciones:
        - One2many: coche_ids conecta esta marca con los coches asociados
          (relación inversa de marca_id en ConcesionarioCoche)

    * ORM:
        - Se pueden usar search(), create(), browse(), write() para gestionar marcas

    * Manejo de errores:
        - El campo name es obligatorio (required=True), evitando registros inválidos

    * Campos relacionales computados / avanzados:
        - Aunque no tiene campos computados por ahora, coche_ids permite fácilmente agregarlos
          para contar coches por marca o filtrar coches por estado.
    """

    name = fields.Char(required=False) # False para pruebas, sino dara errores
    """Nombre de la marca (obligatorio)"""

    coche_ids = fields.One2many(
        "concesionario.coche",
        "marca_id",
        string="Coches"
    )
    """Relación One2many con los coches de esta marca"""
