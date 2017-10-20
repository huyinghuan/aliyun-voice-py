# -*- coding:utf-8 -*-
import unittest
import os
from aliyun_voice.voice import Voice
#设置access_id
ACCESS_ID = ""
#设置access_key
ACCESS_KEY = ""

class TestVoice(unittest.TestCase):
  def test_getVoice(self):
    auth = Voice(ACCESS_ID, ACCESS_KEY)
    content = auth.get_voice("你好")
    self.assertIsNotNone(content)
  def test_save_voice(self):
    auth = Voice(ACCESS_ID, ACCESS_KEY)
    dist = os.path.join(os.path.expanduser('~'), "Desktop", "test.mp3")
    auth.save_voice("你好", dist)