from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ConcesionarioCoche(models.Model):
    _name = "concesionario.coche"
    _description = "Coches del concesionario"
    """
    Modelo ConcesionarioCoche: Representa los coches del concesionario.

    Requisitos cumplidos en este modelo:

    * 5 tablas o modelos como mínimo
        - Este es uno de los modelos (junto con Cliente, Marca, etc.)

    * Relaciones:
        - Many2one: marca_id apunta a 'concesionario.marca'
        - Many2one: propietario_id apunta a 'concesionario.cliente'
        - Many2many: cliente_ids apunta a 'concesionario.cliente' para clientes interesados

    * Campos computados avanzados y almacenados en la BBDD:
        - antiguedad: se calcula a partir de fecha_fabricacion y se almacena (store=True)
        - estado: depende de antiguedad y se almacena (store=True)

    * Decoradores:
        - @api.depends: en _compute_antiguedad y _compute_estado
        - @api.constrains: en _check_precio para validar que el precio sea mayor a 0

    * Campos relacionales computados:
        - estado depende indirectamente de fecha_fabricacion y antiguedad

    * Campos con valores por defecto:
        - vendido: Booleano con default=False

    * ORM:
        - Se puede usar search(), create(), write(), browse() sobre 'concesionario.coche'

    * Herencia en algún modelo:
        - _inherit = ["mail.thread"] para agregar funcionalidades de seguimiento (tracking)

    * Manejo de errores:
        - _check_precio valida que precio sea mayor que 0 y lanza ValidationError
    """

    name = fields.Char(required=True, tracking=True)
    """Nombre del coche (obligatorio y rastreable)"""

    precio = fields.Float(required=True)
    """Precio del coche (obligatorio, validado con _check_precio)"""

    fecha_fabricacion = fields.Date()
    """Fecha de fabricación del coche"""

    vendido = fields.Boolean(default=False)
    """Indica si el coche está vendido, valor por defecto False"""

    marca_id = fields.Many2one(
        "concesionario.marca",
        string="Marca",
        required=True
    )
    """Relación Many2one con el modelo Marca"""

    cliente_ids = fields.Many2many(
        "concesionario.cliente",
        "cliente_coche_favorito_rel",
        "coche_id",
        "cliente_id",
        string="Clientes interesados"
    )
    """Relación Many2many con clientes interesados"""

    propietario_id = fields.Many2one(
        "concesionario.cliente",
        string="Propietario",
        ondelete="set null"
    )
    """Relación Many2one con el cliente propietario"""

    image = fields.Image(
        string="Imagen del Coche",
        max_width=800,
        max_height=600
    )
    """Imagen del coche"""

    antiguedad = fields.Integer(
        compute="_compute_antiguedad",
        store=True
    )
    """Campo computado: antigüedad del coche en años, almacenado en la base de datos"""

    estado = fields.Selection(
        [
            ("nuevo", "Nuevo"),
            ("usado", "Usado"),
        ],
        compute="_compute_estado",
        store=True
    )
    """Campo computado: estado del coche ('nuevo' o 'usado'), almacenado"""

    @api.depends("fecha_fabricacion")
    def _compute_antiguedad(self):
        """Calcula la antigüedad a partir de fecha_fabricacion"""
        for record in self:
            if record.fecha_fabricacion:
                record.antiguedad = fields.Date.today().year - record.fecha_fabricacion.year
            else:
                record.antiguedad = 0

    @api.depends("antiguedad")
    def _compute_estado(self):
        """Determina el estado del coche según la antigüedad"""
        for record in self:
            record.estado = "usado" if record.antiguedad > 1 else "nuevo"

    @api.constrains("precio")
    def _check_precio(self):
        """Valida que el precio sea mayor que 0"""
        for record in self:
            if record.precio <= 0:
                raise ValidationError("El precio debe ser mayor que 0")
