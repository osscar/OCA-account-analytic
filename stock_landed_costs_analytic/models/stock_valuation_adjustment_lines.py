# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)


class StockValuationAdjustmentLines(models.Model):

    _inherit = "stock.valuation.adjustment.lines"

    def _create_account_move_line(
        self, move, credit_account_id, debit_account_id, qty_out, already_out_account_id
    ):
        _logger.debug('caml call >>>: %s', self)
        _logger.debug('caml call move >>>: %s', move)
        res = super(StockValuationAdjustmentLines, self)._create_account_move_line(
            move, credit_account_id, debit_account_id, qty_out, already_out_account_id
        )
        cost_line = self.cost_line_id
        for line in res:
            _logger.debug('caml call for >>>: %s', line)
            # mod'd to fit poi mods
            # if line[2]["account_id"] == cost_line.account_id.id:
            if line["account_id"] == cost_line.account_id.id:
                if cost_line.analytic_account_id:
                    _logger.debug('caml call if account >>>: %s', line)
                    # mod'd to fit poi mods
                    # line[2].update(
                    line.update(
                        {"analytic_account_id": cost_line.analytic_account_id.id}
                    )
                if cost_line.analytic_tag_ids:
                    _logger.debug('caml call if analyt_tags >>>: %s', line)
                    # mod'd to fit poi mods
                    # line[2].update(
                    line.update(
                        {"analytic_tag_ids": [(6, 0, cost_line.analytic_tag_ids.ids)]}
                    )
        return res
