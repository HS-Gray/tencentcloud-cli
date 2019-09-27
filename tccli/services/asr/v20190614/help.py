# -*- coding: utf-8 -*-
DESC = "asr-2019-06-14"
INFO = {
  "CreateRecTask": {
    "params": [
      {
        "name": "EngineModelType",
        "desc": "引擎类型。8k_0：电话 8k 通用模型；16k_0：16k 通用模型；8k_6: 电话场景下单声道话者分离模型。"
      },
      {
        "name": "ChannelNum",
        "desc": "语音声道数。1：单声道；2：双声道（仅在电话 8k 通用模型下支持）。"
      },
      {
        "name": "ResTextFormat",
        "desc": "识别结果文本编码方式。0：UTF-8。"
      },
      {
        "name": "SourceType",
        "desc": "语音数据来源。0：语音 URL；1：语音数据（post body）。"
      },
      {
        "name": "CallbackUrl",
        "desc": "回调 URL，用户自行搭建的用于接收识别结果的服务器地址， 长度小于2048字节。"
      },
      {
        "name": "Url",
        "desc": "语音的URL地址，需要公网可下载。长度小于2048字节，当 source_type 值为 0 时须填写该字段，为 1 时不需要填写。注意：请确保录音文件时长在一个小时之内，否则可能识别失败。请保证文件的下载速度，否则可能下载失败。"
      },
      {
        "name": "Data",
        "desc": "语音数据，当SourceType 值为1时必须填写，为0可不写。要base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于5MB。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，当 SourceType 值为1时必须填写，为0可不写（此数据长度为数据未进行base64编码时的数据长度）。"
      }
    ],
    "desc": "本接口服务对录音时长1小时以内的录音文件进行识别，异步返回识别全部结果。\n<br>• 支持回调或轮询的方式获取结果，轮询方式请参考“录音文件识别结果查询”。\n<br>• 支持语音 URL 和本地语音文件两种请求方式。\n<br>• 接口是 HTTP RESTful 形式\n\n在使用该接口前，需要在 [语音识别控制台](https://console.cloud.tencent.com/asr) 开通服务，并进入 [API 密钥管理页面](https://console.cloud.tencent.com/cam/capi) 新建密钥，<br>生成 AppID、SecretID 和 SecretKey ，用于 API 调用时生成签名，签名将用来进行接口鉴权。"
  },
  "SentenceRecognition": {
    "params": [
      {
        "name": "ProjectId",
        "desc": "腾讯云项目 ID，可填 0，总长度不超过 1024 字节。"
      },
      {
        "name": "SubServiceType",
        "desc": "子服务类型。2： 一句话识别。"
      },
      {
        "name": "EngSerViceType",
        "desc": "引擎类型。8k：电话 8k 中文普通话通用；16k：16k 中文普通话通用；16k_en：16k 英语；16k_ca：16k 粤语。"
      },
      {
        "name": "SourceType",
        "desc": "语音数据来源。0：语音 URL；1：语音数据（post body）。"
      },
      {
        "name": "VoiceFormat",
        "desc": "识别音频的音频格式。mp3、wav。"
      },
      {
        "name": "UsrAudioKey",
        "desc": "用户端对此任务的唯一标识，用户自助生成，用于用户查找识别结果。"
      },
      {
        "name": "Url",
        "desc": "语音 URL，公网可下载。当 SourceType 值为 0（语音 URL上传） 时须填写该字段，为 1 时不填；URL 的长度大于 0，小于 2048，需进行urlencode编码。音频时间长度要小于60s。"
      },
      {
        "name": "Data",
        "desc": "语音数据，当SourceType 值为1（本地语音数据上传）时必须填写，当SourceType 值为0（语音 URL上传）可不写。要使用base64编码(采用python语言时注意读取文件应该为string而不是byte，以byte格式读取后要decode()。编码后的数据不可带有回车换行符)。音频数据要小于600KB。"
      },
      {
        "name": "DataLen",
        "desc": "数据长度，单位为字节。当 SourceType 值为1（本地语音数据上传）时必须填写，当 SourceType 值为0（语音 URL上传）可不写（此数据长度为数据未进行base64编码时的数据长度）。"
      }
    ],
    "desc": "本接口用于对60秒之内的短音频文件进行识别。\n<br>•   支持中文普通话、英语、粤语和带有一定方言口音的中文普通话识别。\n<br>•   支持本地语音文件上传和语音URL上传两种请求方式。\n<br>•   音频格式支持wav、mp3；采样率支持8000Hz或者16000Hz；采样精度支持16bits；声道支持单声道。\n<br>•   当音频文件通过请求中body内容上传时，请求大小不能超过600KB；当音频以URL方式传输时，音频时长不可超过60s。\n<br>•   所有请求参数放在POST请求的body中，编码类型采用x-www-form-urlencoded，参数进行urlencode编码后传输。"
  },
  "DescribeTaskStatus": {
    "params": [
      {
        "name": "TaskId",
        "desc": "从CreateRecTask接口获取的TaskId，用于获取任务状态与结果。"
      }
    ],
    "desc": "本接口需要配合录音文件识别请求接口使用，单独使用无效。在调用录音文件识别接口后，可以在本接口传入TaskID来轮询识别结果。"
  }
}