**Example 1: 查看实例列表**

查看在广州一区或广州二区的实例信息，限制返回结果最多为一项

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-1 ap-guangzhou-2 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RenewFlag": "xx",
                "Uuid": "xx",
                "InstanceState": "xx",
                "LatestOperationState": "xx",
                "LoginSettings": {
                    "Password": "xx",
                    "KeepImageLogin": "xx",
                    "KeyIds": [
                        "xx"
                    ]
                },
                "IPv6Addresses": [
                    "xx"
                ],
                "RestrictState": "xx",
                "ExpiredTime": "2020-09-22T00:00:00+00:00",
                "DisasterRecoverGroupId": "xx",
                "Memory": 1,
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "CPU": 1,
                "RdmaIpAddresses": [
                    "xx"
                ],
                "CamRoleName": "xx",
                "PublicIpAddresses": [
                    "123.207.11.190"
                ],
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "InstanceId": "xx",
                "ImageId": "xx",
                "StopChargingMode": "xx",
                "InstanceChargeType": "xx",
                "InstanceType": "xx",
                "SystemDisk": {
                    "DiskSize": 50,
                    "CdcId": "xx",
                    "DiskId": "xx",
                    "DiskType": "xx"
                },
                "Placement": {
                    "HostId": "xx",
                    "ProjectId": 1174660,
                    "HostIds": [
                        "xx"
                    ],
                    "Zone": "xx",
                    "HostIps": [
                        "xx"
                    ]
                },
                "PrivateIpAddresses": [
                    "172.16.32.78"
                ],
                "OsName": "xx",
                "SecurityGroupIds": [
                    "sg-p1ezv4wz"
                ],
                "InstanceName": "xx",
                "DataDisks": [
                    {
                        "DeleteWithInstance": true,
                        "Encrypt": true,
                        "CdcId": "xx",
                        "DiskType": "xx",
                        "ThroughputPerformance": 0,
                        "KmsKeyId": "xx",
                        "DiskSize": 0,
                        "SnapshotId": "xx",
                        "DiskId": "xx"
                    }
                ],
                "IsolatedSource": "xx",
                "VirtualPrivateCloud": {
                    "SubnetId": "xx",
                    "AsVpcGateway": false,
                    "Ipv6AddressCount": 1,
                    "VpcId": "xx",
                    "PrivateIpAddresses": [
                        "xx"
                    ]
                },
                "LatestOperationRequestId": "xx",
                "InternetAccessible": {
                    "PublicIpAssigned": true,
                    "InternetChargeType": "xx",
                    "BandwidthPackageId": "xx",
                    "InternetMaxBandwidthOut": 1
                },
                "HpcClusterId": "xx",
                "LatestOperation": "xx"
            }
        ],
        "TotalCount": 2,
        "RequestId": "xx"
    }
}
```

**Example 2: 查询绑定了标签的实例**

查询绑定了标签键值对（city:shenzhen）的实例。

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Filters.0.Name tag:city \
    --Filters.0.Values shenzhen \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RenewFlag": "NOTIFY_AND_MANUAL_RENEW",
                "Uuid": "68b510db-b4c1-4630-a62b-73d0c7c970f9",
                "InstanceState": "RUNNING",
                "LatestOperationState": "SUCCESS",
                "OsName": "CentOS 7.6 64bit",
                "CreatedTime": "2020-03-10T02:43:51Z",
                "RestrictState": "NORMAL",
                "ExpiredTime": "2020-04-10T02:47:36Z",
                "DisasterRecoverGroupId": "",
                "Memory": 1,
                "IPv6Addresses": null,
                "CPU": 1,
                "CamRoleName": "",
                "PublicIpAddresses": [
                    "123.207.11.190"
                ],
                "Tags": [
                    {
                        "Value": "shenzhen",
                        "Key": "city"
                    }
                ],
                "InstanceId": "ins-9bxebleo",
                "ImageId": "img-9qabwvbn",
                "StopChargingMode": "NOT_APPLICABLE",
                "InstanceChargeType": "PREPAID",
                "InstanceType": "S1.SMALL1",
                "SystemDisk": {
                    "DiskSize": 50,
                    "DiskId": "disk-nucurerk",
                    "DiskType": "CLOUD_PREMIUM"
                },
                "IsolatedSource": "xx",
                "Placement": {
                    "ProjectId": 1174660,
                    "HostId": null,
                    "Zone": "ap-guangzhou-2"
                },
                "PrivateIpAddresses": [
                    "172.16.32.78"
                ],
                "LoginSettings": {
                    "KeyIds": null
                },
                "SecurityGroupIds": [
                    "sg-p1ezv4wz"
                ],
                "InstanceName": "测试实例",
                "DataDisks": [],
                "VirtualPrivateCloud": {
                    "SubnetId": "subnet-a2676p0e",
                    "AsVpcGateway": false,
                    "VpcId": "vpc-g7wzcv7n"
                },
                "LatestOperationRequestId": "3554eb5b-1cfa-471a-ae76-dc436c9d43e8",
                "InternetAccessible": {
                    "InternetMaxBandwidthOut": 1,
                    "InternetChargeType": "BANDWIDTH_PREPAID"
                },
                "RdmaIpAddresses": [],
                "HpcClusterId": "",
                "LatestOperation": "RenewInstances"
            }
        ],
        "TotalCount": 1,
        "RequestId": "62DDFFC6-FDB5-44F7-20A6-59152E3D129A"
    }
}
```

**Example 3: 查询实例的最新操作情况**

当对实例发起 StopInstances 后，通过 DescribeInstances 可以查询到实例的 LatestOperation 为 StopInstances，LatestOperationState 为 OPERATING。

Input: 

```
tccli cvm DescribeInstances --cli-unfold-argument  \
    --Filters.0.Name zone \
    --Filters.0.Values ap-guangzhou-1 ap-guangzhou-2 \
    --Offset 0 \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "InstanceSet": [
            {
                "RenewFlag": "xx",
                "Uuid": "xx",
                "InstanceState": "xx",
                "LatestOperationState": "xx",
                "LoginSettings": {
                    "Password": "xx",
                    "KeepImageLogin": "xx",
                    "KeyIds": [
                        "xx"
                    ]
                },
                "IPv6Addresses": [
                    "xx"
                ],
                "RestrictState": "xx",
                "ExpiredTime": "2020-09-22T00:00:00+00:00",
                "DisasterRecoverGroupId": "xx",
                "Memory": 1,
                "CreatedTime": "2020-09-22T00:00:00+00:00",
                "CPU": 1,
                "RdmaIpAddresses": [
                    "xx"
                ],
                "CamRoleName": "xx",
                "PublicIpAddresses": [
                    "123.207.11.190"
                ],
                "Tags": [
                    {
                        "Value": "xx",
                        "Key": "xx"
                    }
                ],
                "InstanceId": "xx",
                "ImageId": "xx",
                "StopChargingMode": "xx",
                "InstanceChargeType": "xx",
                "InstanceType": "xx",
                "SystemDisk": {
                    "DiskSize": 50,
                    "CdcId": "xx",
                    "DiskId": "xx",
                    "DiskType": "xx"
                },
                "Placement": {
                    "HostId": "xx",
                    "ProjectId": 1174660,
                    "HostIds": [
                        "xx"
                    ],
                    "Zone": "xx",
                    "HostIps": [
                        "xx"
                    ]
                },
                "PrivateIpAddresses": [
                    "172.16.32.78"
                ],
                "OsName": "xx",
                "SecurityGroupIds": [
                    "sg-p1ezv4wz"
                ],
                "InstanceName": "xx",
                "DataDisks": [
                    {
                        "DeleteWithInstance": true,
                        "Encrypt": true,
                        "CdcId": "xx",
                        "DiskType": "xx",
                        "ThroughputPerformance": 0,
                        "KmsKeyId": "xx",
                        "DiskSize": 0,
                        "SnapshotId": "xx",
                        "DiskId": "xx"
                    }
                ],
                "IsolatedSource": "xx",
                "VirtualPrivateCloud": {
                    "SubnetId": "xx",
                    "AsVpcGateway": false,
                    "Ipv6AddressCount": 1,
                    "VpcId": "xx",
                    "PrivateIpAddresses": [
                        "xx"
                    ]
                },
                "LatestOperationRequestId": "xx",
                "InternetAccessible": {
                    "PublicIpAssigned": true,
                    "InternetChargeType": "xx",
                    "BandwidthPackageId": "xx",
                    "InternetMaxBandwidthOut": 1
                },
                "HpcClusterId": "xx",
                "LatestOperation": "xx"
            }
        ],
        "TotalCount": 2,
        "RequestId": "xx"
    }
}
```

