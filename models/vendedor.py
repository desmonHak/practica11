from odoo import models, fields

class ConcesionarioVendedor(models.Model):
    _name = "concesionario.vendedor"
    _description = "Vendedores del concesionario"
    """
    Modelo ConcesionarioVendedor: Representa a los vendedores del concesionario.

    Requisitos cumplidos en este modelo:

    * 5 tablas o modelos como mínimo
        - Este es uno de los modelos (junto con Cliente, Coche, Marca, Venta, etc.)

    * Relaciones:
        - One2many: venta_ids conecta al vendedor con las ventas realizadas
          (relación inversa de vendedor_id en ConcesionarioVenta)

    * ORM:
        - Se puede usar search(), create(), browse(), write() para gestionar vendedores

    * Manejo de errores:
        - El campo name es obligatorio (required=True), evitando registros inválidos

    * Campos relacionales computados:
        - Se podrían añadir fácilmente campos computados, por ejemplo
          para contar el número de ventas realizadas por el vendedor
    """

    name = fields.Char(required=True)
    """Nombre del vendedor (obligatorio)"""

    venta_ids = fields.One2many(
        "concesionario.venta",
        "vendedor_id"
    )
    """Relación One2many con las ventas realizadas por este vendedor"""
