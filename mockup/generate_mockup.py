# -*- coding: utf-8 -*-

import csv
import datetime
import logging
import models
import os
import random
import time
import webapp2

from google.appengine.ext import ndb
from google.appengine.ext.webapp import template


class MockData(webapp2.RequestHandler):
    @ndb.toplevel
    def get(self):
        ### Add User ###
        populate_data = {'dr_description': 'General Medicine',
                         'dr_major': 'dental',
                         'dr_name': 'Lin',
                         'dr_status': 'Working'}
        models.User.AddUser(populate_data)

        populate_data = {'dr_description': 'Paediatrics',
                         'dr_major': 'paediatrics',
                         'dr_name': 'Cheng',
                         'dr_status': 'Working'}
        models.User.AddUser(populate_data)

        populate_data = {'dr_description': 'Trauma and Orthopaedics',
                         'dr_major': 'trauma and orthopaedics',
                         'dr_name': 'Axa',
                         'dr_status': 'On Leave'}
        models.User.AddUser(populate_data)
        

        ### Add Appointment ###
        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Axa Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Bibi Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Bibi Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 10, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Bibi Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)


        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 11, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Bibi Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 14, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Bibi Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 14, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Bibi Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)


        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 15, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Bibi Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)


        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 15, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'VV Cheng',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)


        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 3, 15, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'JUJU',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 18, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'JUJU',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 12, 20, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': 'axa.cheng@gmail.com',
                         'name': 'Kiki',
                         'phone': '28825252'}
        models.Patient.AddAppointment(populate_data)









        self.redirect("/")
