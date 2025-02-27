# -*- coding: utf-8 -*-
##############################################################################
#
# This file is part of email_separator,
# an Odoo module.
#
# Authors: ACSONE SA/NV (<http://acsone.eu>)
#
# email_separator is free software:
# you can redistribute it and/or modify it under the terms of the GNU
# Affero General Public License as published by the Free Software
# Foundation,either version 3 of the License, or (at your option) any
# later version.
#
# email_separator is distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
# PURPOSE. See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with email_separator.
# If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Email Separator',
    'summary': """
Uses plus sign instead of dash as technical email separator
to build bounce return paths""",
    'author': 'ACSONE SA/NV',
    'website': 'https://acsone.eu',
    'category': 'Tools',
    'version': '8.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'mass_mailing',
    ],
    'installable': False,
    'auto_install': False,
    'application': False,
}
