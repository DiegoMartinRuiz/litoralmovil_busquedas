# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Litoral Movil',
    'version': '1.0',
    'category': 'Litoral Movil Busquedas',
    'author': 'Diego Ruiz',
    'depends': [],
    'description': """
Modulo personalizados para actividades propias de Litoral Movil y Grupo de empresas
    """,
    'data': [
        'views/busquedas_view.xml',
        'views/lm_principal.xml',
        'security/ir.model.access.csv', 
    ],
 
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': True, 
}
