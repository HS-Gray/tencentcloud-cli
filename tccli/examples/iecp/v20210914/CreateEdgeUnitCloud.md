**Example 1: 创建集群**



Input: 

```
tccli iecp CreateEdgeUnitCloud --cli-unfold-argument  \
    --Name console-api-2 \
    --K8sVersion 1.18.2 \
    --VpcId vpc-aib5u94x \
    --Description from console api
```

Output: 
```
{
    "Response": {
        "RequestId": "5ebf13a2-f925-4ba7-adff-ddbc21d355e3",
        "ClusterId": "cls-1dc9nu0m",
        "EdgeUnitId": 100003
    }
}
```

**Example 2: 示例**



Input: 

```
tccli iecp CreateEdgeUnitCloud --cli-unfold-argument  \
    --VpcId  \
    --ServiceCIDR  \
    --Name test \
    --K8sVersion 1.16.7 \
    --PodCIDR  \
    --Description 测试字符串
```

Output: 
```
{
    "Response": {
        "RequestId": "c9db252c-5dd2-448c-a440-86310ca3df22",
        "ClusterId": "cls-f3cj2nxz",
        "EdgeUnitId": 3
    }
}
```

