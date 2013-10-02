#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Holds configuration settings """
SESSION_SECRET_KEY = 'hYgiE_GAe_!@#$ER12348736ABCdefgZ*&^'
SESSION_COOKIE_NAME = 'hygieses'


""" i18n """
I18N_TEMPLATE_PATH = 'templates'
I18N_ENV_ARGS = {'extensions': ['jinja2.ext.i18n']}


""" jinja2 globals """
GLOBALS_SET = {'zip': zip}
