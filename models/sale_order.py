import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Monetary(string="Credit Limit", default=1000.0)

class SaleOrder(models.Model):
    _inherit = 'sale.order'
  
    def action_confirm(self):
        _logger.info(">>> Credit Limit Check Started <<<")
        for order in self:
            # current_balance is the 'credit' field from the partner
            current_balance = order.partner_id.credit
            limit = order.partner_id.credit_limit

            _logger.info("Customer: %s | Balance: %s | Limit: %s", order.partner_id.name, current_balance, limit)

            if current_balance > limit:
                raise ValidationError(_(
                    "CREDIT LIMIT EXCEEDED: The balance of %s is over the limit of %s."
                ) % (current_balance, limit))
        
        return super(SaleOrder, self).action_confirm()