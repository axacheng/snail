# -*- coding: utf-8 -*-
import datetime
import logging

import report

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from google.appengine.datastore.datastore_query import Cursor


class Appointment(ndb.Model):
  appointment_datetime = ndb.DateTimeProperty()
  appointment_dr_name = ndb.StringProperty()
  appointment_status = ndb.StringProperty()
  date_last_updated = ndb.DateTimeProperty(auto_now=True)
  email = ndb.StringProperty(repeated=True)  
  name = ndb.StringProperty()
  phone = ndb.StringProperty(repeated=True)
  ssn = ndb.StringProperty()


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
