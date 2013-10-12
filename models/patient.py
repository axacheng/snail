# -*- coding: utf-8 -*-
import datetime
import logging

import report

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from google.appengine.datastore.datastore_query import Cursor


class Patient(ndb.Model):
  address = ndb.StringProperty(repeated=True)
  zip_code = ndb.IntegerProperty()
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
  side_effect = ndb.StringProperty(repeated=True)


  @classmethod
  def AddAppointment(cls, populate_data):
    appointment = Appointment(
        appointment_datetime = populate_data['appointment_datetime'], 
        appointment_dr_name = populate_data['appointment_dr_name'], 
        appointment_status = populate_data['appointment_status'],
        email = populate_data.get('email'),
        name = populate_data.get('name'),
        phone = populate_data.get('phone'),
        ssn = populate_data.get('ssn'))
    appointment.put_async()


  @classmethod
  def QueryAppointmentAvailableTimetable(cls, appointment_dr_name, appointment_datetime):
    return cls.query(Appointment.appointment_dr_name == appointment_dr_name,
                     Appointment.appointment_status == 'on_track', #confirmed
                     Appointment.appointment_datetime >= appointment_datetime,
                     Appointment.appointment_datetime < appointment_datetime + datetime.timedelta(days=1),
                    ).order(-Appointment.appointment_datetime)


  @classmethod
  def QueryPaitentByUuid(cls, uuid):
    return cls.query(User.dr_status == 'Working')


  @classmethod
  def QueryPaitentByType(cls, search_type, search_string):
    logging.info('qqqqqqqqqqq')
    return 'xxxxxxxx'
    if search_type == 'ssn':
      return cls.query(Patient.ssn == search_string).fetch()

    elif search_type == 'email':
      return cls.query(Patient.email == search_string).fetch()

    elif search_type == 'phone':
      return cls.query(Patient.phone == search_string).fetch()


class Appointment(Patient):
  """docstring for Profile"""
  appointment_datetime = ndb.DateTimeProperty()
  appointment_dr_name = ndb.StringProperty()
  appointment_status = ndb.StringProperty()