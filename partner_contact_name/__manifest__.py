# Copyright 2020 Moltis Technologies (<http://www.moltis.net>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Company Contact Name",
    "summary": "First Contact Name for the Company Records",
    "version": "13.0.1.0.1",
    "author": "Dhaval Patel, Moltis Technologies",
    "license": "AGPL-3",
    "maintainer": "Moltis Technologies",
    "category": "Extra Tools",
    "depends": ["base_setup"],
    #"post_init_hook": "post_init_hook",
    "data": [
    #    "views/base_config_view.xml",
        "views/res_partner.xml",
    #    "views/res_user.xml",
    ],
    "auto_install": False,
    "installable": True,
}
