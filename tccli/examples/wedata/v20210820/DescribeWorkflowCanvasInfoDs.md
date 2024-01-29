**Example 1: 示例1**

demo

Input: 

```
tccli wedata DescribeWorkflowCanvasInfoDs --cli-unfold-argument  \
    --ProjectId 1460947878944567296 \
    --WorkflowId f5d1b42f-ed67-11ed-8909-bc97e105ba60
```

Output: 
```
{
    "Response": {
        "Data": {
            "FolderId": "37db1991-ed4d-11ed-8909-bc97e105ba60",
            "Links": [
                {
                    "Id": "acbe9811-f076-11ed-8909-bc97e105ba60",
                    "InCharge": "jaydenjhu",
                    "LinkDependencyType": "normal_all",
                    "LinkKey": "20230508144306162_20230512113952456",
                    "LinkType": "real_real",
                    "Offset": 1,
                    "RealFromTaskId": null,
                    "RealFromTaskName": null,
                    "RealFromWorkflowId": null,
                    "RealFromWorkflowName": null,
                    "RealProjectId": null,
                    "RealProjectIdent": null,
                    "RealProjectName": null,
                    "TaskFrom": "20230508144306162",
                    "TaskTo": "20230512113952456",
                    "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60"
                }
            ],
            "Owner": "amiizhang",
            "OwnerId": "100028664112",
            "Params": null,
            "ProjectId": "1460947878944567296",
            "ProjectIdent": "us_dev",
            "ProjectName": "调度dev验证项目",
            "SparkParams": "spark.driver.cores=1;\nspark.driver.memory=1g;\nspark.executor.memory=1g;\nspark.executor.instances=1;\nspark.executor.cores=1;\n",
            "Tasks": [
                {
                    "Alarm": null,
                    "Alarms": null,
                    "BrokerIp": "any",
                    "ClusterId": null,
                    "ContentType": null,
                    "CreateTime": "2023-05-08 14:43:06",
                    "Creater": "jaydenjhu",
                    "CrontabExpression": null,
                    "CycleStep": 1,
                    "CycleType": "DAY_CYCLE",
                    "DelayTime": 0,
                    "DependencyConfigList": null,
                    "DependencyRel": "and",
                    "DependencyWorkflow": "no",
                    "EndTime": "2099-12-31 23:59:59",
                    "EventListenerConfig": null,
                    "EventPublisherConfig": null,
                    "ExecutionEndTime": null,
                    "ExecutionStartTime": null,
                    "ExecutionTTL": -1,
                    "FolderId": null,
                    "FolderName": null,
                    "ImportErrMsg": null,
                    "ImportResult": null,
                    "InCharge": "jaydenjhu",
                    "InChargeId": "100028578851",
                    "InstanceInitStrategy": "T_PLUS_0",
                    "LastSchedulerCommitTime": null,
                    "LastUpdate": "2023-05-12 11:41:02",
                    "LeftCoordinate": 346,
                    "LinkId": null,
                    "MaxDateTime": null,
                    "MinDateTime": null,
                    "NewOrUpdate": null,
                    "NormalizedJobStartTime": null,
                    "Notes": null,
                    "OwnId": "100028448903",
                    "Params": null,
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": null,
                    "ProjectName": "调度dev验证项目",
                    "Properties": null,
                    "RealWorkflowId": null,
                    "RecoverFreezeStartTime": null,
                    "RecycleTips": null,
                    "RecycleUser": null,
                    "ResourceGroup": null,
                    "Retriable": 1,
                    "RetryWait": 5,
                    "RunPriority": 6,
                    "SchedulerDesc": "每天00:00执行一次",
                    "ScriptChange": false,
                    "SelfDepend": 2,
                    "SourceServer": null,
                    "StartTime": "2023-05-08 14:43:06",
                    "StartupTime": 0,
                    "Status": "NS",
                    "Submit": false,
                    "TargetServer": null,
                    "TaskAction": "",
                    "TaskAutoSubmit": null,
                    "TaskExt": null,
                    "TaskId": "20230508144306162",
                    "TaskLinkInfo": null,
                    "TaskName": "hive_task_jayden_1",
                    "TaskType": {
                        "BrokerParallelism": 10,
                        "CreateTime": "2022-02-12 11:13:41",
                        "DefaultAliveWait": 720,
                        "DoRedoParallelism": 10000,
                        "DowngradePriorityTries": 2,
                        "ExcludeCommonLib": false,
                        "FileType": null,
                        "InCharge": "admin",
                        "KillAble": 0,
                        "ParamList": "<parameters><parameter><name>hive</name><value>/usr/bin/beeline</value></parameter></parameters>",
                        "PollingSeconds": 2,
                        "PostHooks": "DC",
                        "RetryLimit": 5,
                        "RetryWait": 5,
                        "RunJarName": "IdexHiveSql.jar",
                        "SelectFilePath": null,
                        "SourceServerType": "hive",
                        "TargetServerType": null,
                        "TaskParallelism": 10,
                        "TypeDesc": "Hive SQL",
                        "TypeId": 34,
                        "TypeSort": "数据计算"
                    },
                    "Tasks": null,
                    "TenantId": "1315051789",
                    "TopCoordinate": 277,
                    "TryLimit": 5,
                    "UpdateTime": "2023-05-08 14:43:11",
                    "UpdateUser": "jaydenjhu",
                    "UpdateUserId": "100028578851",
                    "UserFileId": "3692be0a-26e4-4d0b-be70-b3e4759cefed",
                    "UserId": "100028578851",
                    "VersionDesc": null,
                    "VirtualFlag": false,
                    "VirtualTaskId": null,
                    "VirtualTaskStatus": null,
                    "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60",
                    "WorkflowName": "workflow_1",
                    "YarnQueue": null
                },
                {
                    "Alarm": null,
                    "Alarms": null,
                    "BrokerIp": "any",
                    "ClusterId": null,
                    "ContentType": null,
                    "CreateTime": "2023-05-12 11:39:52",
                    "Creater": "jaydenjhu",
                    "CrontabExpression": null,
                    "CycleStep": 1,
                    "CycleType": "DAY_CYCLE",
                    "DelayTime": 0,
                    "DependencyConfigList": null,
                    "DependencyRel": "and",
                    "DependencyWorkflow": "no",
                    "EndTime": "2099-12-31 23:59:59",
                    "EventListenerConfig": null,
                    "EventPublisherConfig": null,
                    "ExecutionEndTime": "23:59",
                    "ExecutionStartTime": "00:00",
                    "ExecutionTTL": -1,
                    "FolderId": null,
                    "FolderName": null,
                    "ImportErrMsg": null,
                    "ImportResult": null,
                    "InCharge": "jaydenjhu",
                    "InChargeId": "100028578851",
                    "InstanceInitStrategy": "T_PLUS_0",
                    "LastSchedulerCommitTime": null,
                    "LastUpdate": "2023-05-12 11:41:02",
                    "LeftCoordinate": 323,
                    "LinkId": null,
                    "MaxDateTime": null,
                    "MinDateTime": null,
                    "NewOrUpdate": null,
                    "NormalizedJobStartTime": null,
                    "Notes": null,
                    "OwnId": "100028448903",
                    "Params": null,
                    "ProductName": "DATA_DEV",
                    "ProjectId": "1460947878944567296",
                    "ProjectIdent": null,
                    "ProjectName": "调度dev验证项目",
                    "Properties": null,
                    "RealWorkflowId": null,
                    "RecoverFreezeStartTime": null,
                    "RecycleTips": null,
                    "RecycleUser": null,
                    "ResourceGroup": "default",
                    "Retriable": 1,
                    "RetryWait": 5,
                    "RunPriority": 6,
                    "SchedulerDesc": "每天00:00执行一次",
                    "ScriptChange": false,
                    "SelfDepend": 2,
                    "SourceServer": null,
                    "StartTime": "2023-05-08 14:43:06",
                    "StartupTime": 0,
                    "Status": "N",
                    "Submit": false,
                    "TargetServer": null,
                    "TaskAction": "",
                    "TaskAutoSubmit": null,
                    "TaskExt": null,
                    "TaskId": "20230512113952456",
                    "TaskLinkInfo": null,
                    "TaskName": "hive_task_jayden_1_copy",
                    "TaskType": {
                        "BrokerParallelism": 10,
                        "CreateTime": "2022-02-12 11:13:41",
                        "DefaultAliveWait": 720,
                        "DoRedoParallelism": 10000,
                        "DowngradePriorityTries": 2,
                        "ExcludeCommonLib": false,
                        "FileType": null,
                        "InCharge": "admin",
                        "KillAble": 0,
                        "ParamList": "<parameters><parameter><name>hive</name><value>/usr/bin/beeline</value></parameter></parameters>",
                        "PollingSeconds": 2,
                        "PostHooks": "DC",
                        "RetryLimit": 5,
                        "RetryWait": 5,
                        "RunJarName": "IdexHiveSql.jar",
                        "SelectFilePath": null,
                        "SourceServerType": "hive",
                        "TargetServerType": null,
                        "TaskParallelism": 10,
                        "TypeDesc": "Hive SQL",
                        "TypeId": 34,
                        "TypeSort": "数据计算"
                    },
                    "Tasks": null,
                    "TenantId": "1315051789",
                    "TopCoordinate": 411,
                    "TryLimit": 5,
                    "UpdateTime": "2023-05-11 20:47:55",
                    "UpdateUser": "jaydenjhu",
                    "UpdateUserId": "100028578851",
                    "UserFileId": null,
                    "UserId": "100028578851",
                    "VersionDesc": null,
                    "VirtualFlag": false,
                    "VirtualTaskId": null,
                    "VirtualTaskStatus": null,
                    "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60",
                    "WorkflowName": "workflow_1",
                    "YarnQueue": null
                }
            ],
            "WorkflowDesc": "",
            "WorkflowId": "f5d1b42f-ed67-11ed-8909-bc97e105ba60",
            "WorkflowName": "workflow_1"
        },
        "RequestId": "7cb0ab03-ea5a-47cc-9dc3-626b46e95698"
    }
}
```
