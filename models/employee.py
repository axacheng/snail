# -*- coding: utf-8 -*-
import datetime
import logging

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from google.appengine.datastore.datastore_query import Cursor


class Employee(polymodel.PolyModel):
  dr_description = ndb.TextProperty()
  dr_major = ndb.StringProperty()
  dr_name = ndb.StringProperty()
  dr_status = ndb.StringProperty()


  @classmethod
  def AddEmployee(cls, populate_data):
    employee = Employee(dr_description = populate_data['dr_description'],
                        dr_major = populate_data['dr_major'],
                        dr_name = populate_data['dr_name'],
                        dr_status = populate_data['dr_status'])
    employee.put()


  @classmethod
  def QueryAvailableDoctor(cls, date=None):
    return cls.query(Employee.dr_status == 'Working')