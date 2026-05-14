import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class ResPartner(models.Model):
    _inherit = 'res.partner'

    credit_limit = fields.Monetary(string="Credit Limit", default=1000.0)

import logging
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        _logger.info(">>> Credit Limit Check Started <<<")
        for order in self:
            # We add the current order total to the existing balance
            total_risk = order.partner_id.credit + order.amount_total
            limit = order.partner_id.credit_limit

            _logger.info("Customer: %s | Total Risk: %s | Limit: %s", 
                         order.partner_id.name, total_risk, limit)

            # Only block if a limit is actually set (greater than 0)
            if limit > 0 and total_risk > limit:
                raise ValidationError(_(
                    "CREDIT LIMIT EXCEEDED: Including this order, the total risk for %s is %s, "
                    " which exceeds the limit of %s."
                ) % (order.partner_id.name, total_risk, limit))
        
        return super(SaleOrder, self).action_confirm()