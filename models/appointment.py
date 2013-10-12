# -*- coding: utf-8 -*-
import datetime
import logging

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from google.appengine.datastore.datastore_query import Cursor

import patient


class Appointment(Patient):
  """docstring for Profile"""
  appointment_datetime = ndb.DateTimeProperty()
  appointment_dr_name = ndb.StringProperty()
  appointment_status = ndb.StringProperty()