#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import os
import webapp2
from handlers import *

session_config = {}
session_config['webapp2_extras.sessions'] = {
    'secret_key': config.SESSION_SECRET_KEY,
    'cookie_name': config.SESSION_COOKIE_NAME,
}

session_config['webapp2_extras.jinja2'] = {
    'template_path': config.I18N_TEMPLATE_PATH,
    'environment_args': config.I18N_ENV_ARGS,
    'globals': config.GLOBALS_SET,
}

application = webapp2.WSGIApplication(
    [('/', MainPage),
     ('/(.*)/about', About),
     ('/hygie', AboutHygie),
     ('/activate/(.*)/(.*)', ActivateUser),
    ],
    debug=True, config=session_config)