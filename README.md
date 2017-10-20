# 阿里云 智能语音识别 SDK

  Python 语言版本

[Go版本](https://github.com/huyinghuan/aliyun-voice)

----------------------------

Install

```
pip install aliyun_voice
```

## TTS 【语音合成服务】

### Voice(ACCESS_ID, ACCESS_KEY)

阿里云认证。
```
  auth := Voice(ALIYUNACCESSID, ALIYUNACCESSKEY)
```

### auth.get_voice(text, **tts_params)

获取语音文件字节数组，或抛出错误。

###  auth.save_voice(text, dist, **tts_params)

存储语音文件到指定目录【dist】，或抛出错误。

### auth.tts_params

设置语音文件属性,参考：https://help.aliyun.com/document_detail/52793.html?spm=5176.doc30422.6.587.Z6Muvv