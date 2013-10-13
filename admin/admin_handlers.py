#!/usr/bin/env python
# -*- coding: utf-8 -*-
### Python build-in library
from collections import Counter
from collections import defaultdict
from collections import OrderedDict

from datetime import datetime, date, time
import jinja2
import json
import logging
import os
import time
import uuid

### 我們自己寫的 library
from base_handler import BaseHandler
from lib import utils
import config
import models
import webapp2

### GAE自己的 或其他3nd party的library
from google.appengine.ext import ndb
from google.appengine.ext import db


class JSONEncoder(json.JSONEncoder):
  def default(self, o):
    # If this is a key, you might want to grab the actual model.
    if isinstance(o, ndb.Key):
        o = db.get(o)

    if isinstance(o, ndb.Model):
        return o.to_dict()

    elif isinstance(o, (datetime, date, time)):
        return str(o)  # Or whatever other date format you're OK with...


class GetPatient(BaseHandler):
  def get(self, search_string):
    patient = models.patient.Patient.QueryPaitent(search_string)
    patient_json = JSONEncoder().encode(patient)

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(patient_json)


class GetAppointment(BaseHandler):
	pass

class ModifyAppointment(BaseHandler):
  def post(self, entity_key, modify_type, value):
  	models.appointment.Appointment.EditAppointment(entity_key, modify_type, value)
  	#self.error(500)


class MainAdmin(BaseHandler):
  def get(self):
  	appointments = models.appointment.Appointment.QueryAppointment()
  	template_dict = {'appointments': appointments.fetch()}
  	self.render_template('admin_main.html', template_dict)



 



