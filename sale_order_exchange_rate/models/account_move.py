# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_order_id = fields.Many2one('sale.order', 'Sale Order ID')
    
    invoice_has_exchange_rate = fields.Boolean('Invoice has currency exchange rate')
    invoice_exchange_rate = fields.Float('Currency Exchange Rate Value', default=1)
    currency_rate_raw = fields.Float("TRM", help="Native field calc from res currency rates")
    amount_total_exchange_rate = fields.Monetary(string='Total with Exchange Rate apply',
                                                 store=True, readonly=True, compute='_amount_all_with_exchange_rate', tracking=4)
    invoice_exchange_allow_ok = fields.Boolean('Allow Exchange Rate', compute="_compute_invoice_exchange_allow_ok")


    @api.depends('invoice_has_exchange_rate','amount_total')
    def _amount_all_with_exchange_rate(self):
        for rec in self:
            if rec.invoice_has_exchange_rate and rec.invoice_exchange_rate > 1:
                amount_total_exchange_rate = rec.amount_total * rec.invoice_exchange_rate
            elif not rec.invoice_has_exchange_rate and rec.currency_rate_raw > 1:
                amount_total_exchange_rate = rec.amount_total * rec.currency_rate_raw
            else:
                amount_total_exchange_rate = 0.0

            rec.amount_total_exchange_rate = amount_total_exchange_rate


    @api.depends('currency_id', 'company_currency_id', 'company_id', 'invoice_has_exchange_rate')
    def _compute_invoice_exchange_allow_ok(self):
        self.invoice_exchange_allow_ok = False
        if self.currency_id != self.company_currency_id:
            self.invoice_exchange_allow_ok = True

    @api.onchange('invoice_exchange_rate')
    def _onchange_invoice_exchange_rate(self):
        if self.invoice_has_exchange_rate:
            self.amount_total_exchange_rate = self.amount_total * self.invoice_exchange_rate

    @api.onchange('invoice_has_exchange_rate')
    def _onchange_invoice_has_exchange_rate(self):
        if self.invoice_has_exchange_rate:
            self.amount_total_exchange_rate = self.amount_total * self.invoice_exchange_rate
        else:
            self.invoice_exchange_rate = 1
            self.amount_total_exchange_rate = self.amount_total * self.currency_rate_raw

    @api.onchange('currency_id')
    def _onchange_currency_id(self):
        if not self.currency_id:
            self.currency_rate_raw = 1
            self.invoice_has_exchange_rate = False
            self.invoice_exchange_rate = 1
            self.amount_total_exchange_rate = 0
        else:
            date = self._context.get('date') or datetime.today()
            self.env['res.currency.rate'].flush(['rate', 'currency_id', 'company_id', 'name'])
            query = """SELECT c.id,
                COALESCE((SELECT r.rate FROM res_currency_rate r
                    WHERE r.currency_id = c.id AND r.name <= %s
                    AND (r.company_id IS NULL OR r.company_id = %s)
                    ORDER BY r.company_id, r.name DESC
                    LIMIT 1), 1.0) AS rate
                    FROM res_currency c
                WHERE c.id = %s"""
            company_obj = self.env['res.company'].browse(self.env.company.id)
            self._cr.execute(query, (date, company_obj.id, self.currency_id.id))
            currency_rates = dict(self._cr.fetchall())
            rate = currency_rates.get(self.currency_id.id) or 1.0
            self.currency_rate_raw = 1 / rate if rate > 0 else 1


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4