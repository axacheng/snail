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


class GetPatient(BaseHandler):
  def get(self, search_type, search_string):
    x = models.patient.Patient.QueryPaitentByType(search_type, search_string)
    logging.info(x)