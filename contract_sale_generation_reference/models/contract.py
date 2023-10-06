# Copyright 2023 Jaime Millán - Xtendoo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models


class ContractContract(models.Model):
    _inherit = "contract.contract"

    client_order_ref = fields.Char(
        string="Client Order Reference",
        help="Client Order Reference",
    )

    def _prepare_sale(self, date_ref):
        self.ensure_one()
        sale = self.env["sale.order"].new(
            {
                "partner_id": self.partner_id,
                "date_order": fields.Date.to_string(date_ref),
                "origin": self.name,
                "company_id": self.company_id.id,
                "user_id": self.partner_id.user_id.id,
                "analytic_account_id": self.group_id.id,
                "client_order_ref": self.client_order_ref,
            }
        )
        if self.payment_term_id:
            sale.payment_term_id = self.payment_term_id.id
        if self.fiscal_position_id:
            sale.fiscal_position_id = self.fiscal_position_id.id
        return sale._convert_to_write(sale._cache)
