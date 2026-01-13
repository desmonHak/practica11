{
    "name": "Concesionario de Coches (Practica 11)",
    "version": "17.0.1.0.0",
    "category": "Tools",
    "summary": "Gestión de concesionario de coches",
    "author": "Alumno",
    "depends": ["base", "web", "mail"],
    "data": [
        "security/ir.model.access.csv",
        'views/views_marca.xml',
        'views/views_cliente.xml',
        'views/views_coche.xml',
        'views/views_vendedor.xml',
        'views/views_venta.xml',
        "views/templates.xml",
        "views/coche_detalle_template.xml"
    ],
    "application": True,
    'installable': True,
}
