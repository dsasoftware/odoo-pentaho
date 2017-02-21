# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo Addon, Open Source Management Solution
#    Copyright (C) 2014-now Equitania Software GmbH(<http://www.equitania.de>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    This program is distributed in the hope that it will be useful,
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import models, fields, api, _
from openerp.osv import osv
from openerp import SUPERUSER_ID
import openerp


class eq_account_payment_term(models.Model):
    """

        eq_name_de -> Das Feld Name mit einem DE Text
        eq_name_en -> Das Feld Name mit einem EN Text
    """

    _inherit = "account.payment.term"

    eq_name_de = fields.Char(compute = '_set_all_fields_de')
    eq_name_en = fields.Char(compute = '_set_all_fields_en')


    def _set_all_fields_de(self):
        """
        Kontext explizit auf Deutsch setzen, damit wir alle Texte korrekt als DE bekommen
        """
        for rec in self:
            localized_rec = rec.with_context(lang="de_DE")
            rec.eq_name_de = localized_rec.name

    def _set_all_fields_en(self):
        """
        Kontext explizit auf English setzen, damit wir alle Texte korrekt als DE bekommen
        """
        for rec in self:
            localized_rec = rec.with_context(lang="en_US")
            rec.eq_name_en = localized_rec.name