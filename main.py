#!/usr/bin/env python
# -*- coding: utf-8 -*-
import config
import os
import webapp2

from admin.admin_handlers import *
from api.api_handlers import *
from mockup.generate_mockup import *
from web.appointment import *

from google.appengine.ext import ndb

session_config = {}
session_config['webapp2_extras.sessions'] = {
    'secret_key': config.SESSION_SECRET_KEY,
    'cookie_name': config.SESSION_COOKIE_NAME,
}

session_config['webapp2_extras.jinja2'] = {
    'template_path': config.I18N_TEMPLATE_PATH,
    'globals': config.GLOBALS_SET,
}

application = ndb.toplevel(webapp2.WSGIApplication(
    [('/', MainPage),

     ### /appointment/make/POST_DATA
     ('/appointment/make/', MakeAppointment),

     ### /appointment/query/timeline/DOCTOR/DATE
     ('/appointment/query/timeline/(.*)/(.*)', ShowAvailableTimeline),

     ### /api/query/token
     ('/api/query/(.*)', GetPatientInfo),

     ### mockup
     ('/mockup', MockData),

     ### /snail_admin
     ('/snail_admin', MainAdmin),

     ### /snail_admin/appointment/modify/urlsafe_entity_key/appointment_status/value
     ('/snail_admin/appointment/modify/(.*)/(.*)/(.*)', ModifyAppointment),


     ### /snail_admin/search/patient/email/axa@google.com
     ('/snail_admin/search/patient/(.*)/(.*)', GetPatient),


    ],
    debug=True, config=session_config))

###
