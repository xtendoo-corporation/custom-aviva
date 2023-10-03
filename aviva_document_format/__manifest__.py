{
    "name": "Aviva Document Format",
    "summary": """Formatos de impresión de AVIVA""",
    "version": "16.0.1.0.1",
    "description": """Formatos de impresión de AVIVA""",
    "author": "Daniel Dominguez",
    "company": "Xtendoo",
    "website": "https://github.com/xtendoo-corporation/custom-aviva",
    "category": "Extra Tools",
    "license": "AGPL-3",
    "depends": [
        "contract_sale_generation",
    ],
    "data": [
        "views/layout/external_layout_bold.xml",
        "views/purchase/purchase_document.xml",
        "views/invoice/invoice_document.xml",
        "views/sale_delivery/sale_order_picking_value.xml",
        "views/sale/sale_order_document.xml",
    ],
    "installable": True,
    "auto_install": False,
}
