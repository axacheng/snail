# -*- coding: utf-8 -*-
import logging

from google.appengine.ext import ndb
from google.appengine.ext.ndb import polymodel
from google.appengine.datastore.datastore_query import Cursor


class Report(Patient):
  """docstring for Profile"""
  report_date = ndb.DateTimeProperty(auto_now_add=True)
  report_diagnose = ndb.TextProperty()
  report_dr_notes = ndb.TextProperty()
  report_image = ndb.BlobProperty()
  report_signature = ndb.StringProperty()
  report_tooth_position = ndb.StringProperty()
  report_treatment = ndb.StringProperty(repeated=True)


class Reservation(Patient):
  """docstring for Profile"""
  reservation_date = ndb.DateTimeProperty()
  reservation_dr_name = ndb.StringProperty()
  reservation_status = ndb.StringProperty()
  reservation_time = ndb.DateTimeProperty()


class Patient(polymodel.PolyModel):
  address = ndb.StringProperty()
  admin_notes = ndb.TextProperty()
  bill = ndb.IntegerProperty()
  blood = ndb.StringProperty()
  credit = ndb.IntegerProperty()
  gender = ndb.StringProperty()
  date_created_this_patient = ndb.DateTimeProperty(auto_now_add=True)
  date_last_updated = ndb.DateTimeProperty(auto_now=True)
  email = ndb.StringProperty()
  insurance_type = ndb.StringProperty()
  insurance_id = ndb.StringProperty()
  name = ndb.StringProperty()
  patient_status = ndb.BooleanProperty()
  phone = ndb.StringProperty()
  report = ndb.StructuredProperty(Report)
  reservation = ndb.StructuredProperty(Reservation)
  sid = ndb.StringProperty()
  side_effect = ndb.StringProperty(repeated=True)


  @classmethod
  def QueryReservationAvailableTimetable(cls, reservation_dr_name, reservation_date):
    return cls.query(Patient.reservation_dr_name == reservation_dr_name,
                     Patient.reservation_date == reservation_date).order(-cls.reservation_date)


  @classmethod
  def AddReservation(cls, populate_data):
    reservation = Reservation(
        reservation_date = populate_data['reservation_date'], 
        reservation_dr_name = populate_data['reservation_dr_name'], 
        reservation_status = populate_data['reservation_status'], 
        reservation_time = populate_data['reservation_time'])
    reservation.put_async()

    patient_info = Patient(
        email = populate_data['email'],
        name = populate_data['name'],
        phone = populate_data['phone'])
    patient_info.put_async()


class User(polymodel.PolyModel):
  dr_description = ndb.TextProperty()
  dr_major = ndb.StringProperty()
  dr_name = ndb.StringProperty()
  dr_status = ndb.StringProperty()


  @classmethod
  def QueryAvailableDoctor(cls):
    return cls.query(User.dr_status == 'Working')



