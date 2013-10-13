# -*- coding: utf-8 -*-
import datetime
import logging

import report

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from google.appengine.datastore.datastore_query import Cursor


class Patient(ndb.Model):
  address = ndb.StringProperty(repeated=True)
  admin_notes = ndb.TextProperty()
  bill = ndb.IntegerProperty()
  blood = ndb.StringProperty()
  credit = ndb.IntegerProperty()
  gender = ndb.StringProperty()
  date_created_this_patient = ndb.DateTimeProperty(auto_now_add=True)
  date_last_updated = ndb.DateTimeProperty(auto_now=True)
  email = ndb.StringProperty(repeated=True)
  insurance_type = ndb.StringProperty()
  insurance_id = ndb.StringProperty()
  name = ndb.StringProperty()
  passport = ndb.StringProperty()
  patient_status = ndb.BooleanProperty()
  phone = ndb.StringProperty(repeated=True)
  report = ndb.StructuredProperty(report.Report)
  ssn = ndb.StringProperty()
  zip_code = ndb.StringProperty()


  @classmethod
  def AddPatient(cls, populate_data):
    patient = Patient(
      address = populate_data.get('address'),
      admin_notes = populate_data.get('admin_notes'),
      bill = populate_data.get('bill'),
      blood = populate_data.get('blood'),
      credit = populate_data.get('credit'),
      gender = populate_data.get('gender'),
      email = populate_data.get('email'),
      insurance_type = populate_data.get('insurance_type'),
      insurance_id = populate_data.get('insurance_id'),
      name = populate_data.get('name'),
      passport = populate_data.get('passport'),
      patient_status = populate_data.get('patient_status'),
      phone = populate_data.get('phone'),
      ssn = populate_data.get('ssn'),
      zip_code = populate_data.get('zip_code'))
    patient.put_async()


  @classmethod
  def QueryPaitentByUuid(cls, uuid):
    return cls.query(User.dr_status == 'Working')

  @classmethod
  def QueryPaitent(cls, search_string):
    result = cls.query(Patient.name == search_string).fetch()
    if result:
      logging.info('name')
      return result

    while not result:
      logging.info('Going to try various searchs')
      result = cls.query(Patient.email == search_string).fetch()
      
      if result:
        logging.info('email:%s', result)
        return result

      result = cls.query(Patient.ssn == search_string).fetch()
      if result:
        logging.info('ssn:%s', result)
        return result

      result = cls.query(Patient.phone == search_string).fetch()
      if result:
        logging.info('phone:%s', result)
        return result

      else:
        logging.info('we cant get anything')
        return result
    


  # @classmethod
  # def QueryPaitentByType(cls, search_type, search_string):
  #   if search_type == 'ssn':
  #     return cls.query(Patient.ssn == search_string)

  #   elif search_type == 'email':
  #     return cls.query(Patient.email == search_string)

  #   elif search_type == 'phone':
  #     return cls.query(Patient.phone == search_string)
