# Copyright 2020 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import models

_logger = logging.getLogger(__name__)

class PurchaseOrderLine(models.Model):

    _inherit = "purchase.order.line"

    def _prepare_stock_moves(self, picking):
        res = super(PurchaseOrderLine, self)._prepare_stock_moves(picking)
        for line in res:
            account_analytic = self.account_analytic_id
            analytic_tags = self.analytic_tag_ids
            _logger.debug('line account_analytic >>>: %s', account_analytic)
            _logger.debug('line analytic_tags >>>: %s', analytic_tags)
            if account_analytic:
                line.update({"analytic_account_id": account_analytic.id})
            if analytic_tags:
                line.update({"analytic_tag_ids": [(6, 0, analytic_tags.ids)]})
        return res
