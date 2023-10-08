# Copyright 2023 Xtendoo
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    account_expense_text = fields.Char(
        compute="_compute_account_expense_text",
        string="Cuenta de gastos/ingresos",
        store=True,
    )

    @api.depends("line_ids")
    def _compute_account_expense_text(self):
        self.account_expense_text = ""
        for invoice in self:
            for line in invoice.line_ids:
                if line and line.account_id and line.account_id.code and line.account_id.code[0] in ["2", "3", "6", "7"]:
                    invoice.account_expense_text = line[0].account_id.code + " - " + line[0].account_id.name
