from odoo import models, fields, api

class ConcesionarioVenta(models.Model):
    _name = "concesionario.venta"
    _description = "Ventas realizadas en el concesionario"
    """
    Modelo ConcesionarioVenta: Representa las ventas realizadas en el concesionario.

    Requisitos cumplidos en este modelo:

    * 5 tablas o modelos como mínimo
        - Este es uno de los modelos (junto con Cliente, Coche, Marca, Vendedor, Venta)

    * Relaciones:
        - Many2one: cliente_id apunta al cliente de la venta
        - Many2one: coche_id apunta al coche vendido
        - Many2one: vendedor_id apunta al vendedor responsable
        - Relación inversa implícita con venta_ids en ConcesionarioVendedor (One2many)

    * Campos con valores por defecto:
        - name: valor por defecto generado dinámicamente usando lambda y la fecha actual

    * Campos relacionales computados / avanzados:
        - precio_final: campo relacionado (related) con coche_id.precio, almacenado en la BBDD (store=True)

    * ORM:
        - Se puede usar search(), create(), browse(), write() para gestionar ventas

    * Manejo de errores:
        - Campos cliente_id y coche_id son obligatorios, evitando registros inválidos
    """

    name = fields.Char(
        default=lambda self: "VENTA-" + fields.Date.today().strftime("%Y%m%d")
    )
    """Identificador de la venta, generado automáticamente con la fecha actual"""

    cliente_id = fields.Many2one(
        "concesionario.cliente",
        required=True
    )
    """Relación Many2one con el cliente que realiza la compra (obligatorio)"""

    coche_id = fields.Many2one(
        "concesionario.coche",
        required=True
    )
    """Relación Many2one con el coche vendido (obligatorio)"""

    vendedor_id = fields.Many2one(
        "concesionario.vendedor"
    )
    """Relación Many2one con el vendedor responsable de la venta"""

    precio_final = fields.Float(
        related="coche_id.precio",
        store=True
    )
    """Precio final de la venta, campo relacionado con coche.precio, almacenado en la BBDD"""
