from odoo import http
from odoo.http import request

class CocheAPI(http.Controller):

    @http.route("/api/coches", auth="public", methods=["GET"], csrf=False)
    def get_coches(self):
        coches = request.env["concesionario.coche"].sudo().search([])
        return {
            "coches": [
                {"id": c.id, "name": c.name, "precio": c.precio}
                for c in coches
            ]
        }

    @http.route("/api/coche", auth="public", methods=["POST"], csrf=False)
    def create_coche(self, **data):
        coche = request.env["concesionario.coche"].sudo().create({
            "name": data.get("name"),
            "precio": float(data.get("precio", 0)),
            "marca_id": int(data.get("marca_id")),
        })
        return {"id": coche.id}
