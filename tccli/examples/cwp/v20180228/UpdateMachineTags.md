**Example 1: 关联机器标签列表**



Input: 

```
tccli cwp UpdateMachineTags --cli-unfold-argument  \
    --Quuid 2b6e5770-8e4d-11e9-8127-98be94219792 \
    --TagIds 11 12 \
    --MachineRegion ap-guangzhou \
    --MachineArea CVM
```

Output: 
```
{
    "Response": {
        "RequestId": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}
```

