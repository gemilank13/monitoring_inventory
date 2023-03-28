    # -*- coding: utf-8 -*-
{
    'name': "INHERIT JPPI - Monitoring Inventory",

    'summary': """Inherit Modul Monitoring Inventory JPPI """,
    'description': """ Inherit Modul Monitoring Inventory JPPI """,
    'author': "PT JPPI - Geger Gemilank",
    'website': "http://www.jppi.co.id",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['ab_inventory','base','uom','hr','board'],

    'data': [
         'security/ir.model.access.csv',
         'views/view.xml',
         'views/dashboard.xml',

    ],
    
    'demo': [],
}
