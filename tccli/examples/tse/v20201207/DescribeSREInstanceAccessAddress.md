**Example 1: 查询引擎实例访问地址**



Input: 

```
tccli tse DescribeSREInstanceAccessAddress --cli-unfold-argument  \
    --InstanceId sre-12345678
```

Output: 
```
{
    "Response": {
        "EnvAddressInfos": [
            {
                "EnableConfigInternet": true,
                "EnvName": "xx",
                "ConfigInternetServiceIp": "xx"
            }
        ],
        "IntranetAddress": "xx",
        "InternetAddress": "xx",
        "ConsoleIntranetAddress": "xx",
        "RequestId": "xx",
        "ConsoleInternetAddress": "xx"
    }
}
```

