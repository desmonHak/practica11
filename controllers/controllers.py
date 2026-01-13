from odoo import http
from odoo.http import request, Response
import json

class CocheAPI(http.Controller):
    """
    Clase CocheAPI: Implementa la API REST y vistas web para el módulo Concesionario.

    Requisitos cumplidos en este archivo:

    * ORM: env y métodos search(), create(), browse()… 
      - En todas las funciones se usa request.env para acceder al modelo 'concesionario.coche'.
      - search(): se usa para listar coches en bootstrap_page() y get_coches().
      - browse(): se usa para acceder a un coche específico en coche_detalle().
      - create(): se usa para crear un coche nuevo en create_coche().

    * API-REST para CRUD
      - GET /api/coches en get_coches() para listar coches.
      - POST /api/coche en create_coche() para crear coches nuevos.

    * Bootstrap en alguna vista
      - La función bootstrap_page() renderiza 'practica11.bootstrap_example', que contiene Bootstrap.
      - La función coche_detalle() renderiza 'practica11.coche_detalle_template', que también usa Bootstrap.

    * Manejo de errores
      - La función coche_detalle() verifica si el coche existe usando exists() y devuelve 404 si no existe.
    """

    @http.route("/concesionario/boot", auth="public", website=True)
    def bootstrap_page(self):
        """
        Renderiza la página principal del concesionario usando Bootstrap.

        Cumplimiento de requisitos:
        - ORM: request.env["concesionario.coche"].sudo().search() para obtener todos los coches.
        - Bootstrap: renderiza 'practica11.bootstrap_example' con diseño Bootstrap.
        """
        coches = request.env["concesionario.coche"].sudo().search([])
        return request.render("practica11.bootstrap_example", {
            "coches": coches
        })

    @http.route("/concesionario/coche/<int:coche_id>", auth="public", website=True)
    def coche_detalle(self, coche_id):
        """
        Renderiza la vista de detalle de un coche específico.

        Cumplimiento de requisitos:
        - ORM: request.env["concesionario.coche"].sudo().browse(coche_id) para acceder al registro.
        - Manejo de errores: verifica si el coche existe con exists() y devuelve 404 si no existe.
        - Bootstrap: renderiza 'practica11.coche_detalle_template' para estética.
        """
        coche = request.env["concesionario.coche"].sudo().browse(coche_id)
        if not coche.exists():
            return request.not_found()
        return request.render("practica11.coche_detalle_template", {
            "coche": coche
        })

    @http.route("/api/coches", auth="public", methods=["GET"], csrf=False, type='http')
    def get_coches(self):
        """
        API REST GET para obtener todos los coches en formato JSON.

        Cumplimiento de requisitos:
        - ORM: request.env["concesionario.coche"].sudo().search() para obtener todos los coches.
        - API-REST: devuelve todos los coches en JSON.
        """
        coches = request.env["concesionario.coche"].sudo().search([])
        data = {
            "coches": [
                {"id": c.id, "name": c.name, "precio": c.precio}
                for c in coches
            ]
        }
        return Response(
            json.dumps(data),
            content_type='application/json',
            status=200
        )

    @http.route("/api/coche", auth="public", methods=["POST"], csrf=False, type='http')
    def create_coche(self, **data):
        """
        API REST POST para crear un nuevo coche.

        Cumplimiento de requisitos:
        - ORM: request.env["concesionario.coche"].sudo().create() para crear un registro nuevo.
        - API-REST: recibe JSON con name, precio y marca_id y devuelve el ID del coche creado.
        """
        coche = request.env["concesionario.coche"].sudo().create({
            "name": data.get("name"),
            "precio": float(data.get("precio", 0)),
            "marca_id": int(data.get("marca_id")),
        })
        return Response(
            json.dumps({"id": coche.id}),
            content_type='application/json',
            status=200
        )
