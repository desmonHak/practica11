from odoo import http
from odoo.http import request, Response
import json

class CocheAPI(http.Controller):

    @http.route("/concesionario/boot", auth="public", website=True)
    def bootstrap_page(self):
        # Obtener todos los coches
        coches = request.env["concesionario.coche"].sudo().search([])
        return request.render("practica11.bootstrap_example", {
            "coches": coches
        })

    @http.route("/concesionario/coche/<int:coche_id>", auth="public", website=True)
    def coche_detalle(self, coche_id):
        coche = request.env["concesionario.coche"].sudo().browse(coche_id)
        if not coche.exists():
            return request.not_found()
        return request.render("practica11.coche_detalle_template", {
            "coche": coche
        })

    @http.route("/api/coches", auth="public", methods=["GET"], csrf=False, type='http')
    def get_coches(self):
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
