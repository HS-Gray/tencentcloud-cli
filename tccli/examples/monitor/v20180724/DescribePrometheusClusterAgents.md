**Example 1: 拉取agent信息**

拉取agent信息

Input: 

```
tccli monitor DescribePrometheusClusterAgents --cli-unfold-argument  \
    --InstanceId xx \
    --Limit 1 \
    --Offset 1
```

Output: 
```
{
    "Response": {
        "Total": 1,
        "Agents": [
            {
                "Status": "xx",
                "ClusterName": "xx",
                "ExternalLabels": [
                    {}
                ],
                "ClusterId": "xx",
                "ClusterType": "xx",
                "Region": "xx",
                "VpcId": "xx",
                "FailedReason": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```
