#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import pickle
import hashlib
import json
import hmac
import urllib
from base64 import b64decode, b64encode
from binascii import unhexlify

""" api private key """
API_PRIVATE_KEY = 'a2c59c942095d348121c5a822cfedfd845d72725'


def substr(s, start, length=None):
  if len(s) < start:
    return False
  if not length:
    return s[start:]
  elif length > 0:
    return s[start:start + length]
  else:
    return s[start:length]


def get_rand_iv(iv_len):
  import random
  iv = ""
  while(iv_len > 0):
    iv += chr(random.randint(0, sys.maxint) & 0xff)
    iv_len = iv_len-1
  return iv


def strxor(s0, s1):
  l = [chr(ord(a) ^ ord(b)) for a, b in zip(s0, s1)]
  return ''.join(l)


def md5_encrypt(plain_dict, password="", iv_len=16):
  if not password:
  	password = API_PRIVATE_KEY

  plain_text = urllib.urlencode(plain_dict)
  plain_text += "\x13"
  n = len(plain_text)
  if(n % 16):
    plain_text += "\0" * (16 - (n % 16))
  i = 0
  enc_text = get_rand_iv(iv_len)
  iv = substr(strxor(password, enc_text), 0, 512)
  while (i < n):
    block = strxor(substr(plain_text, i, 16), unhexlify(hashlib.md5(iv).hexdigest()))
    enc_text += block
    iv = strxor(substr(block + iv, 0, 512), password)
    i = i + 16
  return b64encode(enc_text)


def md5_decrypt(enc_text, password="", iv_len=16):	
  import re

  if not password:
  	password = API_PRIVATE_KEY

  enc_text = b64decode(enc_text)
  n = len(enc_text)
  i = iv_len
  plain_text = ""
  iv = substr(strxor(password, substr(enc_text, 0, iv_len)), 0, 512)
  while (i < n):
    block = substr(enc_text, i, 16)
    plain_text += strxor(block, unhexlify(hashlib.md5(iv).hexdigest()))
    iv = strxor(substr(block + iv, 0, 512), password)
    i = i + 16
  plain_text = re.sub('[\x00-\x08\x0B-\x1F]', '', plain_text)
  try:
  	return dict([p.split('=') for p in plain_text.split('&')])
  except ValueError:
  	return False
