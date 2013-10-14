#!/usr/bin/env python
# -*- coding: utf-8 -*-
### Python build-in library
from collections import Counter
from collections import defaultdict
from collections import OrderedDict

from datetime import datetime, date, time
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
from google.appengine.ext import db


class JSONEncoder(json.JSONEncoder):
  """
  This JSONEncoder is provided from:
  http://stackoverflow.com/questions/13311363/appengine-making-ndb-models-json-serializable
  """
  def default(self, o):
    # If this is a key, you might want to grab the actual model.
    if isinstance(o, ndb.Key):
      o = db.get(o)

    if isinstance(o, ndb.Model):
      return o.to_dict()

    elif isinstance(o, (datetime, date, time)):
      return str(o)  # Or whatever other date format you're OK with...


class GetPatient(BaseHandler):
  def get(self, search_string):
    patient = models.patient.Patient.QueryPaitent(search_string)
    
    if patient:
      entity_key = patient[0].key.id()
      patient_json = JSONEncoder().encode(patient)
      patient_json_trim = patient_json.replace('}]', ',')
      entity_key_string = "\"patient_uuid\":\"%s\"}]" % entity_key
      logging.info(patient_json_trim+entity_key_string)
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(patient_json_trim+entity_key_string)
    
    else:
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(patient)

class GetAppointment(BaseHandler):
  pass


class ModifyPatientCheckIn(BaseHandler):
  def post(self, patient_uuid):
    patient_status = 'check_in'
    modify_type = 'patient_status'    
    populate_data = {'patient_status':patient_status}
    
    models.patient.Patient.EditPatient(modify_type, patient_uuid, populate_data)


class ModifyAppointment(BaseHandler):
  def post(self, entity_key, modify_type, value):
    models.appointment.Appointment.EditAppointment(entity_key, modify_type, value)
    #self.error(500)


class MainAdmin(BaseHandler):
  def get(self):
    appointments = models.appointment.Appointment.QueryAppointment()
    template_dict = {'appointments': appointments.fetch()}
    self.render_template('admin_main.html', template_dict)


class AddPatient(BaseHandler):
  def get(self):
    pass

  def post(self):
    first_name = self.request.get('first_name')
    middle_name = self.request.get('middle_name', default_value='')
    last_name = self.request.get('last_name')
    email = self.request.get('email', default_value='')
    address = self.request.get('address', default_value='')
    zip_code = self.request.get('zip_code', default_value='')
    phone_primary = self.request.get('phone_primary', default_value='')
    phone_secondary = self.request.get('phone_secondary', default_value='')
    birthday = self.request.get('birthday', default_value='')
    blood = self.request.get('blood', default_value='')
    gender = self.request.get('gender', default_value='')
    ssn = self.request.get('ssn', default_value='')
    driver_license = self.request.get('driver_license', default_value='')
    insurance_type = self.request.get('insurance_type', default_value='')
    insurance_id = self.request.get('insurance_id', default_value='')

    phone =[]
    name = []
    [phone.append(i) for i in phone_primary, phone_secondary]
    if not middle_name:
      [name.append(i) for i in first_name.lower(),
                               last_name.lower()]
    else:
      [name.append(i) for i in first_name.lower(),
                               middle_name.lower(),
                               last_name.lower()]      
    populate_data = {
      'id': str(uuid.uuid1().int) + '_' + name[0],
      'name':name,
      'email':[email],
      'address':[address],
      'zip_code':zip_code,
      'phone':phone,
      'birthday':birthday,
      'blood':blood.lower(),
      'gender':gender.lower(),
      'patient_status': 'baby',
      'ssn':ssn ,
      'driver_license':driver_license ,
      'insurance_type':insurance_type.lower() ,
      'insurance_id':insurance_id ,
    }

    patient = models.patient.Patient.AddPatient(populate_data)
    patient_json = JSONEncoder().encode(patient.get())

    ### TODO, need to reload page after submiited.
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(patient_json)

 



