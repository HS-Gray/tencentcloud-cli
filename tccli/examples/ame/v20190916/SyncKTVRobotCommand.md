**Example 1: 播放列表添加歌曲**



Input: 

```
tccli ame SyncKTVRobotCommand --cli-unfold-argument  \
    --RobotId xxxxx \
    --Command SetPlaylist \
    --SetPlaylistCommandInput.Type Add \
    --SetPlaylistCommandInput.MusicIds xxxxxxx \
    --SetPlaylistCommandInput.Index -1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 2: 播放指定音乐**

播放第2首歌曲

Input: 

```
tccli ame SyncKTVRobotCommand --cli-unfold-argument  \
    --RobotId xxxxx \
    --Command Play \
    --PlayCommandInput.Index 1
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 3: 变更歌曲音频参数**

变更歌曲音频参数

Input: 

```
tccli ame SyncKTVRobotCommand --cli-unfold-argument  \
    --RobotId xxxxx \
    --Command SetAudioParam \
    --SetAudioParamCommandInput.Definition audio/hi \
    --SetAudioParamCommandInput.Type Accompaniment
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 4: 切换下一首歌曲**



Input: 

```
tccli ame SyncKTVRobotCommand --cli-unfold-argument  \
    --RobotId xxxxx \
    --Command SwitchNext
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 5: 发送自定义消息**



Input: 

```
tccli ame SyncKTVRobotCommand --cli-unfold-argument  \
    --RobotId xxxxx \
    --Command SendMessage \
    --SendMessageCommandInput.Message {"Field1":"Value1"} \
    --SendMessageCommandInput.Repeat 2
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

**Example 6: 设置播放模式**

设置播放模式为随机播放。

Input: 

```
tccli ame SyncKTVRobotCommand --cli-unfold-argument  \
    --RobotId xxxxx \
    --Command SetPlayMode \
    --SetPlayModeCommandInput.PlayMode Shuffle
```

Output: 
```
{
    "Response": {
        "RequestId": "xx"
    }
}
```

