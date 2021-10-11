**Example 1: 查询线索列表接口**



Input: 

```
tccli wav QueryClueInfoList --cli-unfold-argument  \
    --Cursor sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU \
    --Limit 1
```

Output: 
```
{
    "Response": {
        "NextCursor": "sHmJbhJZhCwwMYmSot50dl2Hs9qQvbP+pCUVxlm/oLU=",
        "HasMore": 1,
        "PageData": [
            {
                "DealerId": "1,3,5",
                "ClueId": "1348080105398452226",
                "EnquireTime": 1618556502,
                "UnionId": "wmpqy2CAAATGwpQTxuU1IUfoiOFH2cXA",
                "Name": "微信昵称",
                "Phone": "134xxxx1234",
                "SeriesCode": "车系编号",
                "ModelCode": "车型编号",
                "ProvinceCode": "省份编号",
                "CityCode": "城市编号",
                "SalesName": "顾问名称",
                "SalesPhone": "134xxxx6789",
                "Remark": "备注",
                "TagList": [
                    "标签1",
                    "标签2"
                ]
            }
        ],
        "RequestId": "b1a024bf-4d74-4b5d-a5bd-bbec330520e8"
    }
}
```
