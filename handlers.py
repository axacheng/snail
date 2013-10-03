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
from mockup.generate_mockup import *
import config
import models
import webapp2

### GAE自己的 或其他3nd party的library
from google.appengine.ext import ndb


def _json_encode_for_ndb(obj):
    return json.dumps(obj.to_dict())


class MainPage(BaseHandler):
  def get(self):
    available_doctor = models.User.QueryAvailableDoctor().fetch()
    template_dict = {'available_doctor': available_doctor}
    #self.response.headers['Content-Type'] = 'application/json'
    #self.response.out.write(json.dumps(available_doctor.map(_json_encode_for_ndb)))

    self.render_template('index.html', template_dict)



  def post(self, data):
    pass


class MakeAppointment(BaseHandler):
  def get(self, form):
    pass

  def post(self):
    form = self.request.get_all('form_data')
    logging.info('xxxxxxxxx:%s', form)

    populate_data = {
      'appointment_datetime': datetime.datetime.strptime(form[1], "%Y%m%d%H"),
      'appointment_dr_name': form[0],
      'appointment_status': 'on_track',
      'email': form[4],
      'name': form[2],
      'phone': form[3],
    }

    models.Patient.AddAppointment(populate_data)

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(form))



class ShowAvailableTimeline(BaseHandler):
  def get(self, doctor, date_time):
    converted_date_time = datetime.datetime.strptime(date_time, "%Y%m%d")
    timelines = models.Patient.QueryAppointmentAvailableTimetable(doctor, converted_date_time)
    appointments = timelines.fetch()
    appointment_times = Counter()

    for appointment in appointments:
      appointment_times[appointment.appointment_datetime] += 1

    all_work_hours = range(9, 17)  # 9-16
    all_work_hours.remove(12)  # remove lunch time.
    mockup_times = []
    full_times = []
    available_times = []

    for i in all_work_hours:
      new_date_time = date_time + str(i)
      mockup_times.append(datetime.datetime.strptime(new_date_time, "%Y%m%d%H"))

    for count_by_times in appointment_times.items():
      if count_by_times[1] >= 3:  # we actually can take = 3 instead.
        full_times.append(count_by_times[0])

    available_times_set = set(mockup_times) - set(full_times)

    for available_time in available_times_set:
      available_times.append(available_time)

    # convert all datetime object to string type, and only get HOUR field.
    available_times = sorted(map(lambda i: i.strftime("%H"), available_times ))
    self.response.out.write(json.dumps(available_times))


class ShowAvailableDoctor(BaseHandler):
  def get(self, date):
    if not date:
      available_doctor = models.User.QueryAvailableDoctor()
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(json.dumps(available_doctor.map(_json_encode_for_ndb)))

    else:
      available_doctor = models.User.QueryAvailableDoctor(date)
      self.response.headers['Content-Type'] = 'application/json'
      self.response.out.write(json.dumps(available_doctor.map(_json_encode_for_ndb)))

  def post(self):
    pass