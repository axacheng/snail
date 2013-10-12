# -*- coding: utf-8 -*-

import csv
import datetime
import logging
import models
import os
import random
import time
import webapp2

from models.appointment import *
from models.patient import *
from models.employee import *

from google.appengine.ext import ndb
from google.appengine.ext.webapp import template


class MockData(webapp2.RequestHandler):
    @ndb.toplevel
    def get(self):
        ### Add Employee ###
        populate_data = {'dr_description': 'General Medicine',
                         'dr_major': 'dental',
                         'dr_name': 'Lin',
                         'dr_status': 'Working'}
        models.employee.Employee.AddEmployee(populate_data)

        populate_data = {'dr_description': 'Paediatrics',
                         'dr_major': 'paediatrics',
                         'dr_name': 'Cheng',
                         'dr_status': 'Working'}
        models.employee.Employee.AddEmployee(populate_data)

        populate_data = {'dr_description': 'Trauma and Orthopaedics',
                         'dr_major': 'trauma and orthopaedics',
                         'dr_name': 'Axa',
                         'dr_status': 'On Leave'}
        models.employee.Employee.AddEmployee(populate_data)
        

        ### Add Appointment ###
        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Axa Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Bibi Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Bibi Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 10, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Bibi Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)


        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 10, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Bibi Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 14, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Bibi Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 14, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Bibi Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)


        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 15, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Bibi Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)


        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 15, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'VV Cheng',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)


        populate_data = {'appointment_datetime': datetime.datetime(2013, 10, 14, 15, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'JUJU',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 11, 18, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'JUJU',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)

        populate_data = {'appointment_datetime': datetime.datetime(2013, 12, 20, 9, 0),
                         'appointment_dr_name': 'Lin',
                         'appointment_status': 'on_track',
                         'email': [('axa.cheng@gmail.com')],
                         'name': 'Kiki',
                         'phone': [('28825252')]}
        models.appointment.Appointment.AddAppointment(populate_data)


        ### Add Patient
        populate_data ={'address':[('1600 Amphitheatre Pkwy, Mountain View, CA')],
                        'admin_notes':'good patient',
                        'bill': 899,
                        'blood':'o',
                        'credit': 80,
                        'gender': 'male',
                        'email': [('axa@google.com')],
                        'insurance_type': 'social',
                        'insurance_id': '88888888',
                        'name': 'Axa Cheng',
                        'passport': '273282882',
                        'patient_status': True,
                        'phone': [('(798) 087-9789')],
                        'ssn': '123456789',
                        'zip_code':'94043'}
        models.patient.Patient.AddPatient(populate_data)

        populate_data ={'address':[('1717 Harrison St San Francisco, CA')],
                        'admin_notes':'good patient',
                        'bill': 40,
                        'blood':'a',
                        'credit': 100,
                        'gender': 'male',
                        'email': [('georgeecheng@gmail.com')],
                        'insurance_type': 'social',
                        'insurance_id': '9999999',
                        'name': 'George Cheng',
                        'passport': '87379372',
                        'patient_status': True,
                        'phone': [('(123) 199-9999')],
                        'ssn': '666',
                        'zip_code':'94103-4226'}
        models.patient.Patient.AddPatient(populate_data)



        self.redirect("/")
