# -*- coding: utf-8 -*-
import datetime
import logging

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from google.appengine.datastore.datastore_query import Cursor


class Report(polymodel.PolyModel):
  """docstring for Profile"""
  report_date = ndb.DateTimeProperty(auto_now_add=True)
  report_diagnose = ndb.TextProperty()
  report_dr_notes = ndb.TextProperty()
  report_image = ndb.BlobProperty()
  report_side_effect = ndb.StringProperty(repeated=True)
  report_signature = ndb.StringProperty()
  report_tooth_position = ndb.StringProperty()
  report_treatment = ndb.StringProperty(repeated=True)
