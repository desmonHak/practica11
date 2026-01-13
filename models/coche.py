from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ConcesionarioCoche(models.Model):
    _name = "concesionario.coche"
    _description = "Coche"
    _inherit = ["mail.thread"]  # HERENCIA

    name = fields.Char(required=True, tracking=True)
    precio = fields.Float(required=True)
    fecha_fabricacion = fields.Date()
    vendido = fields.Boolean(default=False)

    marca_id = fields.Many2one(
        "concesionario.marca",
        string="Marca",
        required=True
    )

    cliente_ids = fields.Many2many(
        "concesionario.cliente",
        "cliente_coche_favorito_rel",  # misma tabla intermedia
        "coche_id",                     # columna que apunta a coche
        "cliente_id",                   # columna que apunta a cliente
        string="Clientes interesados"
    )
    
    propietario_id = fields.Many2one(
        "concesionario.cliente",
        string="Propietario",
        ondelete="set null"
    )
    
    # CAMPO DE IMAGEN
    image = fields.Image(
        string="Imagen del Coche",  # Nombre visible en la vista
        max_width=800,               # ancho máximo de la imagen
        max_height=600               # alto máximo
    )

    antiguedad = fields.Integer(
        compute="_compute_antiguedad",
        store=True
    )

    estado = fields.Selection(
        [
            ("nuevo", "Nuevo"),
            ("usado", "Usado"),
        ],
        compute="_compute_estado",
        store=True
    )

    @api.depends("fecha_fabricacion")
    def _compute_antiguedad(self):
        for record in self:
            if record.fecha_fabricacion:
                record.antiguedad = fields.Date.today().year - record.fecha_fabricacion.year
            else:
                record.antiguedad = 0

    @api.depends("antiguedad")
    def _compute_estado(self):
        for record in self:
            record.estado = "usado" if record.antiguedad > 1 else "nuevo"

    @api.constrains("precio")
    def _check_precio(self):
        for record in self:
            if record.precio <= 0:
                raise ValidationError("El precio debe ser mayor que 0")
