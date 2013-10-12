#!/usr/bin/env python
# -*- coding: utf-8 -*-
### Python build-in library
from collections import Counter
from collections import defaultdict
from collections import OrderedDict

import datetime
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


def _json_encode_for_ndb(obj):
    return json.dumps(obj.to_dict())
    

class MainPage(BaseHandler):
  def get(self):
    available_doctor = models.employee.Employee.QueryAvailableDoctor().fetch()
    template_dict = {'available_doctor': available_doctor}
    self.render_template('index.html', template_dict)

  def post(self, data):
    pass


class MakeAppointment(BaseHandler):
  def get(self):
    pass

  def post(self):
    form = self.request.get_all('form_data')
    populate_data = {
      'appointment_datetime': datetime.datetime.strptime(form[1], "%Y%m%d%H"),
      'appointment_dr_name': form[0],
      'appointment_status': 'on_track',
      'email': [(form[5])],
      'name': form[2],
      'phone': [(form[4])],
      'ssn': form[3],
    }

    models.appointment.Appointment.AddAppointment(populate_data)

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(form))