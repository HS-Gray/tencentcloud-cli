**Example 1: 通过准备好的印章图片创建个人印章**

通过准备好的印章图片创建个人印章

Input: 

```
tccli ess CreatePreparedPersonalEsign --cli-unfold-argument  \
    --Operator.UserId abc \
    --Operator.Channel abc \
    --Operator.OpenId abc \
    --Operator.ClientIp abc \
    --Operator.ProxyIp abc \
    --UserName 印章归属个人姓名 \
    --IdCardType  \
    --IdCardNumber 身份证件号码 \
    --SealImage 印章图片Base64 \
    --SealName 我的印章名称 \
    --Mobile 135*111 \
    --EnableAutoSign True
```

Output: 
```
{
    "Response": {
        "SealId": "sealid-1",
        "RequestId": "abc"
    }
}
```
