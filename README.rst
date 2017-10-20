阿里云 智能语音 SDK
===================

Python 语言版本

`Go版本`_

--------------

Install

::

    pip install aliyun_voice

TTS 【语音合成服务】
--------------------

Voice(ACCESS\_ID, ACCESS\_KEY)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

阿里云认证。

::

    from aliyun_voice.voice import Voice
    auth = Voice(ALIYUNACCESSID, ALIYUNACCESSKEY)

auth.get\_voice(text, \*\*tts\_params)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

获取语音文件字节数组，或抛出错误。

auth.save\_voice(text, dist, \*\*tts\_params)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

存储语音文件到指定目录【dist】，或抛出错误。

auth.tts\_params
~~~~~~~~~~~~~~~~

设置语音文件属性,参考：https://help.aliyun.com/document\_detail/52793.html?spm=5176.doc30422.6.587.Z6Muvv

Test
----

.. code:: shell

    python -m unittest discover -v

.. _Go版本: https://github.com/huyinghuan/aliyun-voice