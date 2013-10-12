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


class GetPatient(BaseHandler):
  def get(self, search_type, search_string):
    patient = models.patient.Patient.QueryPaitentByType(search_type, search_string)
    logging.info(patient)

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(patient.map(_json_encode_for_ndb)))


class Register(BaseHandler):
  def get(self):
    template_dict = {'patient': 'patient'}
    self.render_template('register.html', template_dict)