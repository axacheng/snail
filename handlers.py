#!/usr/bin/env python
# -*- coding: utf-8 -*-
### Python build-in library
from collections import Counter
from collections import defaultdict
from collections import OrderedDict

import datetime
import jinja2
import json
import cgi
import logging
import os
import time
import urllib
import utils
import uuid

### 我們自己寫的 library
from base_handler import BaseHandler
from apis.drawchart import *
from mockup.generate_mockup import *
from mytest.tagtest import *
from mytest.jquery_ui_autocom import *
from mytest.memcache_test import *
from webapp2_extras import i18n
import config
import error
import models
import webapp2

### GAE自己的 或其他3nd party的library
from google.appengine.ext import ndb
from google.appengine.ext.db import BadValueError
from google.appengine.api import memcache
from google.appengine.api import images
from google.appengine.ext.webapp import template
from sdk.countryinfo import countryinfo
from sdk.oauth2client.client import AccessTokenRefreshError
from sdk.apiclient.errors import HttpError
from sdk.pyipinfodb import pyipinfodb
from sdk.pymobiledetect import detect




class MyBlog(BaseHandler):
  def get(self, disease_name, page):
    hygie_username = self.session.get('hygie_username')

    if not len(page):
      page = 3

    all_blogs_fetched_entities, next_curs, more = models.Report.QueryBlog(disease_name, hygie_username, page)

    all_blogs = []
    for blog_entity in all_blogs_fetched_entities:
      blog = {}
      blog['content'] = blog_entity.content
      blog['date_created'] = datetime.datetime.strftime(blog_entity.date_created, '%Y-%m-%d %H:%M')
      all_blogs.append(blog)

    # 加入 '更舊的日誌' 的 cursor, 之後這cursor會被 myrecord_main.html 裡面的 server_return[3] 用到
    if more and next_curs:
      all_blogs.append(next_curs.urlsafe())
      all_blogs.append(more)

    #logging.info('All blogs %s', all_blogs)
    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(all_blogs))

  def post(self, disease_name, page):
    content = self.request.get('content')
    disease_name = disease_name
    fetched_blog_date = self.request.get_all('blog_date')
    date_created = datetime.datetime(*time.strptime(''.join(fetched_blog_date).encode('utf-8'), "%Y-%m-%d")[0:5])
    hygie_username = self.session.get('hygie_username')
    parent = ndb.Key('Report', hygie_username)
    report_type = 'Blog'

    try:
      models.Report.AddBlog(content, date_created, disease_name, hygie_username, parent, report_type)
      models.Counter.AddBlogCounter(disease_name, hygie_username)
      self.redirect('/me')

    except BadValueError:
      logging.info('bad')
      self.response.out.write('沒有內容')