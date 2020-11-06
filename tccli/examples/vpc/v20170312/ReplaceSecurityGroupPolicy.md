**Example 1: 替换单条安全组路由规则**



Input: 

```
tccli vpc ReplaceSecurityGroupPolicy --cli-unfold-argument  \
    --Version 2017-03-12 \
    --SecurityGroupId sg-ohuuioma \
    --SecurityGroupPolicySet.Version 20 \
    --SecurityGroupPolicySet.Egress.0.PolicyIndex 2 \
    --SecurityGroupPolicySet.Egress.0.ServiceTemplate.ServiceId ppm-f5n1f8da \
    --SecurityGroupPolicySet.Egress.0.AddressTemplate.AddressId ipm-2uw6ujo6 \
    --SecurityGroupPolicySet.Egress.0.Action accept \
    --SecurityGroupPolicySet.Egress.0.PolicyDescription TestPolicy
```

Output: 
```
{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```
