#!/usr/bin/env python
# -*- coding:utf-8 -*-
import hashlib
import base64
import urllib
import time
import hmac
import requests

class Voice(object):
  def __init__(self, access_id, access_key):
    '''
      用阿里云access_id,access_key初始化
    '''
    self.access_id = access_id
    self.access_key = access_key
    self.tts_params = {
      "encode_type": "mp3",
      "voice_name":             "xiaoyun",
			"volume":                 50,
			"sample_rate":            16000,
			"speech_rate":            0,
			"pitch_rate":             0,
			"tss_nus":                1,
			"background_music_id":     -1,
			"background_music_offset": 0,
			"background_music_volume": 50,
    }
    self.__API = "https://nlsapi.aliyun.com/speak?%s"
  
  def __get_tts_auth(self, text, date):
    md5 = hashlib.md5()
    md5.update(text)
    body_md5 = base64.b64encode(md5.digest())
    feature = "%s\n%s\n%s\n%s\n%s" % ("POST", "audio/%s,application/json" % self.tts_params["encode_type"], body_md5, "text/plain", date)
    return base64.b64encode(hmac.new(self.access_key, feature, hashlib.sha1).digest())

  def __get_tts_params(self):
    return urllib.urlencode(self.tts_params)
  
  def get_voice(self, text, **kw):
    '''
      获取文本的声音文件
      @params<string> 文本
      @params<dict>  设置参数，参照aliyun tts的配置。 【注意，文件类型只需传入 [mp3, wav, ...]即可】
      @return<raw> 返回声音的二进制
      @throw error 当参数不符合阿里云要求时会抛出错误
    '''
    for key, value in kw.iteritems():
      self.tts_params[key] = value
    date = time.strftime("%a, %d %b %Y %H:%M:%S GMT", time.gmtime())
    headers = {
      "Authorization": "Dataplus %s:%s" % (self.access_id, self.__get_tts_auth(text, date)),
      "Content-Type": "text/plain",
      "accept": "audio/%s,application/json" % self.tts_params["encode_type"],
      "date": date
    }
    urlstr = self.__API % self.__get_tts_params()
    r = requests.post(urlstr, headers=headers, data=text,  stream=True)
    content_type =  r.headers['Content-Type']
    if content_type.find('json') != -1:
      raise StandardError(r.json())
    else:
      return r.content

  def save_voice(self, text, dist, **kw):
    '''
      存储文本的声音文件
      @params<string> 文本
      @params<string> 声音文件存储路径
      @params<dict>  设置参数，参照aliyun tts的配置。 【注意，文件类型只需传入 [mp3, wav, ...]即可】
      @throw error 当参数不符合阿里云要求时会抛出错误
    '''
    content = self.get_voice(text, **kw)
    with open(dist, 'wb') as fd:
      fd.write(content)