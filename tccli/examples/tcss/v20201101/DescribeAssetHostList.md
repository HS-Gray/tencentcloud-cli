**Example 1: 查询主机列表**



Input: 

```
tccli tcss DescribeAssetHostList --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "List": [
            {
                "Status": "xx",
                "PublicIp": "xx",
                "HostID": "xx",
                "Group": "xx",
                "DockerVersion": "xx",
                "IsContainerd": true,
                "InstanceID": "xx",
                "HostName": "xx",
                "ImageCnt": 1,
                "DockerFileSystemDriver": "xx",
                "HostIP": "xx",
                "RegionID": 0,
                "MachineType": "xx",
                "ContainerCnt": 1,
                "Uuid": "xx"
            },
            {
                "Status": "xx",
                "ImageCnt": 1,
                "HostID": "xx",
                "Group": "xx",
                "DockerVersion": "xx",
                "IsContainerd": true,
                "InstanceID": "xx",
                "HostName": "xx",
                "PublicIp": "xx",
                "DockerFileSystemDriver": "xx",
                "HostIP": "xx",
                "RegionID": 0,
                "MachineType": "xx",
                "ContainerCnt": 1,
                "Uuid": "xx"
            }
        ],
        "RequestId": "xx"
    }
}
```

