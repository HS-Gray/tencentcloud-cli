**Example 1: 修改自学习模型状态**



Input: 

```
tccli gme ModifyCustomizationState --cli-unfold-argument  \
    --ToState 0 \
    --BizId 0 \
    --ModelId xx
```

Output: 
```
{
    "Response": {
        "ErrorCode": 0,
        "RequestId": "xx",
        "ModelId": "xx"
    }
}
```
