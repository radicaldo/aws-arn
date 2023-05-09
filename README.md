# aws-arn
A complete list of all AWS ARNs

Isn't anyoning trying to guess the ARN for a specific AWS resource? This is a complete list of all AWS ARNs. The list is sorted alphabetically by service and resource.  This is the only complete list of AWS ARNs available anywhere.

> :warning: **Work in progress**: This is a work in progress.  Not all services and resources are included yet.  Please open an issue or pull request if you find any errors or omissions.

- Total number of services:  153
- Total number of resources:  468

# Features

- Generate ARNs for any AWS resource by passing in the resource ID and other parameters
- Get the ASFF Resource Name for any AWS resource (e.g. `AwsCertificateManagerCertificate`)
- Get the Cloudformation Resource Name for any AWS resource (e.g. `AWS::CertificateManager::Certificate`)
- Get the Terraform Resource Name for any AWS resource (e.g. `aws_acm_certificate`)

# Contributing to this list

ARNs are defined under [aws_arn/data.py](aws_arn/data.py). 

Format:

```
    "acm": { --> The Service Name (we follow boto3 naming conventions)
        "certificate": {  --> The Resource Name (we follow boto3 naming conventions)
            "arn_format": "arn:{partition}:acm:{region}:{account}:certificate/{resource_id}",
            "id_name": "CertificateId",  --> The Resource Id name
            "id_regexp": "([a-z0-9-]+)", --> The Resource Id regexp
            "asff_name": "AwsCertificateManagerCertificate",   --> The ASFF Resource Name
            "cloudformation": "AWS::CertificateManager::Certificate",  --> The CloudFormation Resource Name
            "terraform": "aws_acm_certificate",  --> The Terraform Resource Name
        }
    },
```

# To Do:

- CloudFormation and Terraform resources for all ARNs


# Use it as a module

```
import aws_arn

arn = aws_arn.generate_arn('i-1234568901', 'ec2', 'instance', 'us-east-1', '012345789012', 'aws')

print (arn)

arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

arn = aws_arn.generate_arn_from_terraform('i-1234568901', 'aws_instance', 'us-east-1', '012345789012', 'aws')

print (arn)

arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

arn = aws_arn.generate_arn_from_cloudformation('i-1234568901', 'AWS::EC2::Instance', 'us-east-1', '012345789012', 'aws')

print (arn)

arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901

```

# Use it as CLI

```
./aws-arn --generate-arn --id test --service ec2 --sub-service instance --region us-east-1 --account 012345789012 --partition aws

arn:aws:ec2:us-east-1:012345789012:instance/test


./aws-arn --get-service-from-terraform --terraform aws_instance

('ec2', 'instance')

./aws-arn --generate-arn-from-terraform --id test --terraform aws_instance --region us-east-1 --account 012345789012 --partition aws

arn:aws:ec2:us-east-1:012345789012:instance/test

./aws-arn --generate-arn-from-cloudformation --id test --cloudformation AWS::EC2::Instance --region us-east-1 --account 012345789012 --partition aws

arn:aws:ec2:us-east-1:012345789012:instance/test

```

## Full List of ARNs

| Service | ARN Format |
| --- | --- |
| acm | certificate: `arn:{partition}:acm:{region}:{account}:certificate/{resource_id}`<br> |
| acm-pca | certificate_authority: `arn:{partition}:acm-pca:{region}:{account}:certificate-authority/{resource_id}`<br> |
| alexaforbusiness | skill: `arn:{partition}:aplb:{region}:{account}:skill/{resource_id}`<br> |
| apigateway | api: `arn:{partition}:apigateway:{region}::/restapis/{resource_id}`<br>api_key: `arn:{partition}:apigateway:{region}::/apikeys/{resource_id}`<br>authorizer: `arn:{partition}:apigateway:{region}::/restapis/{api_id}/authorizers/{resource_id}`<br>base_path_mapping: `arn:{partition}:apigateway:{region}::/restapis/{api_id}/basepathmappings/{resource_id}`<br>client_certificate: `arn:{partition}:apigateway:{region}::/clientcertificates/{resource_id}`<br>deployment: `arn:{partition}:apigateway:{region}::/restapis/{api_id}/deployments/{resource_id}`<br>documentation_part: `arn:{partition}:apigateway:{region}::/restapis/{api_id}/documentation/parts/{resource_id}`<br>documentation_version: `arn:{partition}:apigateway:{region}::/restapis/{api_id}/documentation/versions/{resource_id}`<br>domain_name: `arn:{partition}:apigateway:{region}::/domainnames/{resource_id}`<br>gateway_response: `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/gatewayresponses/{resource_id}`<br>integration: `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{ResourceId}/methods/{HttpMethod}/integrations/{resource_id}`<br>method: `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{ResourceId}/methods/{resource_id}`<br>model: `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/models/{resource_id}`<br>request_validator: `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/requestvalidators/{resource_id}`<br>resource: `arn:{partition}:apigateway:{region}::/restapis/{ApiId}/resources/{resource_id}`<br>rest_api: `arn:{partition}:apigateway:{region}::/restapis/{resource_id}`<br>stage: `arn:{partition}:apigateway:{region}::/restapis/{rest_api_id}/stages/{resource_id}`<br>usage_plan: `arn:{partition}:apigateway:{region}::/usageplans/{resource_id}`<br>usage_plan_key: `arn:{partition}:apigateway:{region}::/usageplans/{usage_plan_id}/keys/{resource_id}`<br>vpc_link: `arn:{partition}:apigateway:{region}::/vpclinks/{resource_id}`<br> |
| appflow | connector_profile: `arn:{partition}:appflow:{region}:{account}:connectorprofile/{resource_id}`<br>flow: `arn:{partition}:appflow:{region}:{account}:flow/{resource_id}`<br> |
| appstream | directory_config: `arn:{partition}:appstream:{region}:{account}:directoryconfig/{resource_id}`<br>fleet: `arn:{partition}:appstream:{region}:{account}:fleet/{resource_id}`<br>image: `arn:{partition}:appstream:{region}:{account}:image/{resource_id}`<br>image_builder: `arn:{partition}:appstream:{region}:{account}:imagebuilder/{resource_id}`<br>stack: `arn:{partition}:appstream:{region}:{account}:stack/{resource_id}`<br> |
| athena | workgroup: `arn:{partition}:athena:{region}:{account}:workgroup/{resource_id}`<br> |
| augmentedairuntime | human_loop: `arn:{partition}:sagemaker:{region}:{account}:human-loop/{resource_id}`<br> |
| autoscaling | auto_scaling_group: `arn:{partition}:autoscaling:{region}:{account}:autoScalingGroup:{resource_id}`<br>launch_configuration: `arn:{partition}:autoscaling:{region}:{account}:launchConfiguration:{resource_id}`<br> |
| backup | backup_plan: `arn:{partition}:backup:{region}:{account}:backup-plan/{resource_id}`<br>backup_vault: `arn:{partition}:backup:{region}:{account}:backup-vault/{resource_id}`<br>recovery_plan: `arn:{partition}:backup:{region}:{account}:recoveryplan/{resource_id}`<br> |
| batch | compute_environment: `arn:{partition}:batch:{region}:{account}:compute-environment/{resource_id}`<br>job_definition: `arn:{partition}:batch:{region}:{account}:job-definition/{resource_id}:{version}`<br>job_queue: `arn:{partition}:batch:{region}:{account}:job-queue/{resource_id}`<br> |
| budgets | budget: `arn:{partition}:budgets:{region}:{account}:budget/{resource_id}`<br> |
| cloud9 | environment: `arn:{partition}:cloud9:{region}:{account}:environment:{resource_id}`<br> |
| cloudformation | change_set: `arn:{partition}:cloudformation:{region}:{account}:changeSet/{resource_id}`<br>stack: `arn:{partition}:cloudformation:{region}:{account}:stack/{stack_name}/{stack_id}`<br> |
| cloudfront | distribution: `arn:{partition}:cloudfront::{account}:distribution/{resource_id}`<br>field_level_encryption_config: `arn:{partition}:cloudfront::{account}:field-level-encryption-config/{resource_id}`<br>field_level_encryption_profile: `arn:{partition}:cloudfront::{account}:field-level-encryption-profile/{resource_id}`<br>realtime_log_config: `arn:{partition}:cloudfront::{account}:realtime-log-config/{resource_id}`<br> |
| cloudhsmv2 | cluster: `arn:{partition}:cloudhsmv2:{region}:{account}:cluster/{resource_id}`<br>backup: `arn:{partition}:cloudhsmv2:{region}:{account}:backup/{resource_id}`<br>hsm: `arn:{partition}:cloudhsmv2:{region}:{account}:cluster/{resource_id}/hsm/{hsm_id}`<br> |
| cloudtrail | trail: `arn:{partition}:cloudtrail:{region}:{account}:trail/{resource_id}`<br> |
| cloudwatch | alarm: `arn:{partition}:cloudwatch:{region}:{account}:alarm:{resource_id}`<br>dashboard: `arn:{partition}:cloudwatch::{account}:dashboard/{resource_id}`<br> |
| codeartifact | domain: `arn:{partition}:codeartifact:{region}:{account}:domain/{resource_id}`<br>repository: `arn:{partition}:codeartifact:{region}:{account}:repository/{domain_name}/{resource_id}`<br>package: `arn:{partition}:codeartifact:{region}:{account}:repository/{domain_name}/{repository_name}/package/{package_format}/{package_name}@{package_version}`<br> |
| codebuild | project: `arn:{partition}:codebuild:{region}:{account}:project/{resource_id}`<br> |
| codecommit | repository: `arn:{partition}:codecommit:{region}:{account}:{resource_id}`<br> |
| codedeploy | application: `arn:{partition}:codedeploy:{region}:{account}:application:{resource_id}`<br>deployment_config: `arn:{partition}:codedeploy:{region}:{account}:deploymentconfig:{resource_id}`<br>deployment_group: `arn:{partition}:codedeploy:{region}:{account}:deploymentgroup:{resource_id}`<br> |
| codepipeline | pipeline: `arn:{partition}:codepipeline:{region}:{account}:{resource_type}/{resource_id}`<br> |
| codestar-connections | connection: `arn:{partition}:codestar-connections:{region}:{account}:connection/{resource_id}`<br> |
| codestar-notifications | rule: `arn:{partition}:codestar-notifications:{region}:{account}:notificationrule/{resource_id}`<br> |
| cognito-idp | identity_provider: `arn:{partition}:cognito-idp:{region}:{account}:userpool/{user_pool_id}:identityprovider/{identity_provider_name}`<br>resource_server: `arn:{partition}:cognito-idp:{region}:{account}:userpool/{user_pool_id}/resource-server/{resource_server_id}`<br>user_pool: `arn:{partition}:cognito-idp:{region}:{account}:userpool/{user_pool_id}`<br> |
| comprehend | document_classifier: `arn:{partition}:comprehend:{region}:{account}:document-classifier/{resource_id}`<br>entity_recognizer: `arn:{partition}:comprehend:{region}:{account}:entity-recognizer/{resource_id}`<br>key_phrases_detection_job: `arn:{partition}:comprehend:{region}:{account}:key-phrases-detection-job/{resource_id}`<br>sentiment_detection_job: `arn:{partition}:comprehend:{region}:{account}:sentiment-detection-job/{resource_id}`<br>topic_detection_job: `arn:{partition}:comprehend:{region}:{account}:topic-detection-job/{resource_id}`<br> |
| compute-optimizer | recommendation_export_job: `arn:{partition}:compute-optimizer:{region}:{account}:recommendation-export-job/{resource_id}`<br> |
| config | aggregator: `arn:{partition}:config:{region}:{account}:config-aggregator/{resource_id}`<br>conformance_pack: `arn:{partition}:config:{region}:{account}:conformance-pack/{resource_id}`<br>config_rule: `arn:{partition}:config:{region}:{account}:config-rule/{resource_id}`<br>organization_config_rule: `arn:{partition}:config:{region}:{account}:organization-config-rule/{resource_id}`<br>remediation_configuration: `arn:{partition}:config:{region}:{account}:remediation-configuration/{resource_id}`<br> |
| cur | report_definition: `arn:{partition}:cur:${ReportName}-${YYYYMM}-${AdditionalArtifact}-{region}-{account}`<br> |
| dataexchange | asset: `arn:{partition}:dataexchange:{region}:{account}:asset/{resource_id}`<br>data_set: `arn:{partition}:dataexchange:{region}:{account}:data-sets/{resource_id}`<br>job: `arn:{partition}:dataexchange:{region}:{account}:job/{resource_id}`<br>revision: `arn:{partition}:dataexchange:{region}:{account}:revision/{resource_id}`<br> |
| datapipeline | pipeline: `arn:{partition}:datapipeline:{region}:{account}:{resource_type}/{resource_id}`<br> |
| dax | cluster: `arn:{partition}:dax:{region}:{account}:cluster:{resource_id}`<br> |
| devicefarm | project: `arn:{partition}:devicefarm:{region}:{account}:project:${resource_id}`<br>device_instance: `arn:{partition}:devicefarm:{region}:{account}:device-instance:${resource_id}`<br>device_pool: `arn:{partition}:devicefarm:{region}:{account}:devicepool:${resource_id}`<br>run: `arn:{partition}:devicefarm:{region}:{account}:run:${resource_id}`<br>job: `arn:{partition}:devicefarm:{region}:{account}:job:${resource_id}`<br>suite: `arn:{partition}:devicefarm:{region}:{account}:suite:${resource_id}`<br>test: `arn:{partition}:devicefarm:{region}:{account}:test:${resource_id}`<br> |
| directconnect | connection: `arn:{partition}:directconnect:{region}:{account}:dxcon:{resource_id}`<br>link_aggregation_group: `arn:{partition}:directconnect:{region}:{account}:linkaggregations:{resource_id}`<br>private_virtual_interface: `arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id}`<br>public_virtual_interface: `arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id}`<br>transit_virtual_interface: `arn:{partition}:directconnect:{region}:{account}:dxvif:{resource_id}`<br> |
| dynamodb | table: `arn:{partition}:dynamodb:{region}:{account}:table/{resource_id}`<br> |
| ec2 | customer_gateway: `arn:{partition}:ec2:{region}:{account}:customer-gateway/{resource_id}`<br>dedicated_host: `arn:{partition}:ec2:{region}:{account}:host/{resource_id}`<br>dhcp_options: `arn:{partition}:ec2:{region}:{account}:dhcp-options/{resource_id}`<br>egress_only_internet_gateway: `arn:{partition}:ec2:{region}:{account}:egress-only-internet-gateway/{resource_id}`<br>elastic_gpu: `arn:{partition}:ec2:{region}:{account}:elastic-gpu/{resource_id}`<br>elastic_inference_accelerator: `arn:{partition}:elastic-inference:{region}:{account}:accelerator/{resource_id}`<br>elastic_ip: `arn:{partition}:ec2:{region}:{account}:elastic-ip/{resource_id}`<br>flow_log: `arn:{partition}:ec2:{region}:{account}:flow-log/{resource_id}`<br>image: `arn:{partition}:ec2:{region}:{account}:image/{resource_id}`<br>instance: `arn:{partition}:ec2:{region}:{account}:instance/{resource_id}`<br>internet_gateway: `arn:{partition}:ec2:{region}:{account}:internet-gateway/{resource_id}`<br>key_pair: `arn:{partition}:ec2:{region}:{account}:key-pair/{resource_id}`<br>launch_template: `arn:{partition}:ec2:{region}:{account}:launch-template/{resource_id}`<br>natgateway: `arn:{partition}:ec2:{region}:{account}:natgateway/{resource_id}`<br>network_acl: `arn:{partition}:ec2:{region}:{account}:network-acl/{resource_id}`<br>network_interface: `arn:{partition}:ec2:{region}:{account}:network-interface/{resource_id}`<br>placement_group: `arn:{partition}:ec2:{region}:{account}:placement-group/{resource_id}`<br>reserved_instances: `arn:{partition}:ec2:{region}:{account}:reserved-instances/{resource_id}`<br>route_table: `arn:{partition}:ec2:{region}:{account}:route-table/{resource_id}`<br>security_group: `arn:{partition}:ec2:{region}:{account}:security-group/{resource_id}`<br>snapshot: `arn:{partition}:ec2:{region}:{account}:snapshot/{resource_id}`<br>spot_fleet_request: `arn:{partition}:ec2:{region}:{account}:spot-fleet-request/{resource_id}`<br>spot_instance_request: `arn:{partition}:ec2:{region}:{account}:spot-instances-request/{resource_id}`<br>subnet: `arn:{partition}:ec2:{region}:{account}:subnet/{resource_id}`<br>traffic_mirror_filter: `arn:{partition}:ec2:{region}:{account}:traffic-mirror-filter/{resource_id}`<br>traffic_mirror_session: `arn:{partition}:ec2:{region}:{account}:traffic-mirror-session/{resource_id}`<br>traffic_mirror_target: `arn:{partition}:ec2:{region}:{account}:traffic-mirror-target/{resource_id}`<br>transit_gateway: `arn:{partition}:ec2:{region}:{account}:transit-gateway/{resource_id}`<br>transit_gateway_attachment: `arn:{partition}:ec2:{region}:{account}:transit-gateway-attachment/{resource_id}`<br>transit_gateway_multicast_domain: `arn:{partition}:ec2:{region}:{account}:transit-gateway-multicast-domain/{resource_id}`<br>transit_gateway_route_table: `arn:{partition}:ec2:{region}:{account}:transit-gateway-route-table/{resource_id}`<br>volume: `arn:{partition}:ec2:{region}:{account}:volume/{resource_id}`<br>vpc: `arn:{partition}:ec2:{region}:{account}:vpc/{resource_id}`<br>vpc_endpoint: `arn:{partition}:ec2:{region}:{account}:vpc-endpoint/{resource_id}`<br>vpc_endpoint_service: `arn:{partition}:ec2:{region}:{account}:vpc-endpoint-service/{resource_id}`<br>vpc_peering_connection: `arn:{partition}:ec2:{region}:{account}:vpc-peering-connection/{resource_id}`<br>vpn_connection: `arn:{partition}:ec2:{region}:{account}:vpn-connection/{resource_id}`<br>vpn_gateway: `arn:{partition}:ec2:{region}:{account}:vpn-gateway/{resource_id}`<br> |
| ec2-instance-connect | connect: `arn:{partition}:ec2-instance-connect:{region}:{account}:connect/${InstanceId}`<br> |
| ecr | repository: `arn:{partition}:ecr:{region}:{account}:repository/{resource_id}`<br>image: `arn:{partition}:ecr:{region}:{account}:image/{resource_id}`<br> |
| ecs | cluster: `arn:{partition}:ecs:{region}:{account}:cluster/{resource_id}`<br>task_definition: `arn:{partition}:ecs:{region}:{account}:task-definition/{resource_id}`<br>task: `arn:{partition}:ecs:{region}:{account}:task/{resource_id}`<br>service: `arn:{partition}:ecs:{region}:{account}:service/{cluster_name}/{service_name}`<br>container_instance: `arn:{partition}:ecs:{region}:{account}:container-instance/{resource_id}`<br> |
| efs | file_system: `arn:{partition}:elasticfilesystem:{region}:{account}:file-system/{resource_id}`<br>access_point: `arn:{partition}:elasticfilesystem:{region}:{account}:access-point/{resource_id}`<br> |
| eks | cluster: `arn:{partition}:eks:{region}:{account}:cluster/{resource_id}`<br> |
| elastic-inference | accelerator_type: `arn:{partition}:elastic-inference:{region}:{account}:accelerator-type/{resource_id}`<br> |
| elasticache | cache_cluster: `arn:{partition}:elasticache:{region}:{account}:cluster:{resource_id}`<br>cache_parameter_group: `arn:{partition}:elasticache:{region}:{account}:parameter-group:{resource_id}`<br>cache_security_group: `arn:{partition}:elasticache:{region}:{account}:security-group:{resource_id}`<br>cache_subnet_group: `arn:{partition}:elasticache:{region}:{account}:subnet-group:{resource_id}`<br>global_replication_group: `arn:{partition}:elasticache:{region}:{account}:global-replication-group:{resource_id}`<br>replication_group: `arn:{partition}:elasticache:{region}:{account}:cluster:{resource_id}`<br>user_group: `arn:{partition}:elasticache:{region}:{account}:user-group:{resource_id}`<br> |
| elasticbeanstalk | application: `arn:{partition}:elasticbeanstalk:{region}:{account}:application/{resource_id}`<br>application_version: `arn:{partition}:elasticbeanstalk:{region}:{account}:applicationversion/{resource_id}`<br>environment: `arn:{partition}:elasticbeanstalk:{region}:{account}:environment/{resource_id}`<br> |
| elb | loadbalancer: `arn:{partition}:elasticloadbalancing:{region}:{account}:loadbalancer/{resource_id}`<br> |
| elbv2 | loadbalancer: `arn:{partition}:elasticloadbalancing:{region}:{account}:loadbalancer/{resource_id}`<br>targetgroup: `arn:{partition}:elasticloadbalancing:{region}:{account}:targetgroup/{resource_id}/{tagergroup_id}}`<br>listener: `arn:{partition}:elasticloadbalancing:{region}:{account}:listener/{resource_id}/{load_balancer_id}/{listener_id}`<br>listener_rule: `arn:{partition}:elasticloadbalancing:{region}:{account}:listener-rule/{resource_id}`<br> |
| elasticmapreduce | cluster: `arn:{partition}:elasticmapreduce:{region}:{account}:cluster/{resource_id}`<br>security_configuration: `arn:{partition}:elasticmapreduce:{region}:{account}:security-configuration/{resource_id}`<br>step: `arn:{partition}:elasticmapreduce:{region}:{account}:cluster/{resource_id}/step/{step_id}`<br> |
| elastictranscoder | pipeline: `arn:{partition}:elastictranscoder:{region}:{account}:pipeline/{resource_id}`<br>preset: `arn:{partition}:elastictranscoder:{region}:{account}:preset/{resource_id}`<br> |
| es | domain: `arn:{partition}:es:{region}:{account}:domain/{resource_id}`<br> |
| events | archive: `arn:{partition}:events:{region}:{account}:archive/{resource_id}`<br>bus: `arn:{partition}:events:{region}:{account}:event-bus/{resource_id}`<br>rule: `arn:{partition}:events:{region}:{account}:rule/{resource_id}`<br> |
| firehose | delivery_stream: `arn:{partition}:firehose:{region}:{account}:deliverystream/{resource_id}`<br> |
| fms | policy: `arn:{partition}:fms:{region}:{account}:policy/{resource_id}`<br> |
| fsx | backup: `arn:{partition}:fsx:{region}:{account}:backup/{resource_id}`<br>file_system: `arn:{partition}:fsx:{region}:{account}:file-system/{resource_id}`<br> |
| gamelift | alias: `arn:{partition}:gamelift:{region}:{account}:alias/{resource_id}`<br>build: `arn:{partition}:gamelift:{region}:{account}:build/{resource_id}`<br>fleet: `arn:{partition}:gamelift:{region}:{account}:fleet/{resource_id}`<br> |
| glacier | vault: `arn:{partition}:glacier:{region}:{account}:vaults/{resource_id}`<br> |
| globalaccelerator | accelerator: `arn:{partition}:globalaccelerator::{account}:accelerator/{resource_id}`<br>listener: `arn:{partition}:globalaccelerator::{account}:listener/{resource_id}`<br>endpoint_group: `arn:{partition}:globalaccelerator::{account}:endpoint-group/{resource_id}`<br> |
| glue | catalog: `arn:{partition}:glue:{region}:{account}:catalog`<br>crawler: `arn:{partition}:glue:{region}:{account}:crawler:{resource_name}`<br>database: `arn:{partition}:glue:{region}:{account}:database/{resource_id}`<br>dev_endpoint: `arn:{partition}:glue:{region}:{account}:devEndpoint/{resource_name}`<br>job: `arn:{partition}:glue:{region}:{account}:job/{resource_name}`<br>partition: `arn:{partition}:glue:{region}:{account}:table/{DatabaseName}/{TableName}/partition/{PartitionValues}`<br>trigger: `arn:{partition}:glue:{region}:{account}:trigger/{resource_name}`<br>workflow: `arn:{partition}:glue:{region}:{account}:workflow/{resource_name}`<br> |
| greengrass | group: `arn:{partition}:greengrass:{region}:{account}:/greengrass/groups/{resource_id}`<br> |
| guardduty | detector: `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}`<br>filter: `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/filter/{subresource_id}`<br>ipset: `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/ipset/{subresource_id}`<br>member: `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/member/{subresource_id}`<br>threatintelset: `arn:{partition}:guardduty:{region}:{account}:detector/{resource_id}/threatintelset/{subresource_id}`<br> |
| health | event: `arn:{partition}:health:{region}:{account}:event/{resource_id}`<br>health_check: `arn:{partition}:health:{region}:{account}:healthcheck/{resource_id}`<br>organization_event_detail: `arn:{partition}:health:{region}:{account}:event-organization/{event_type_code}/{service}/{event_type_version}/{event_id}`<br>service: `arn:{partition}:health:{region}:{account}:service/{resource_id}`<br> |
| iam | access_key: `arn:{partition}:iam::{account}:accesskey/{resource_id}`<br>account_alias: `arn:{partition}:iam::{account}:alias/{resource_id}`<br>group: `arn:{partition}:iam::{account}:group/{resource_id}`<br>instance_profile: `arn:{partition}:iam::{account}:instance-profile/{resource_id}`<br>policy: `arn:{partition}:iam::{account}:policy/{resource_id}`<br>role: `arn:{partition}:iam::{account}:role/{resource_id}`<br>server_certificate: `arn:{partition}:iam::{account}:server-certificate/{resource_id}`<br>user: `arn:{partition}:iam::{account}:user/{resource_id}`<br>virtual_mfa_device: `arn:{partition}:iam::{account}:mfa/{resource_id}`<br>group_policy: `arn:{partition}:iam::{account}:group/{group_id}/policy/{policy_id}`<br>role_policy: `arn:{partition}:iam::{account}:role/{role_id}/policy/{policy_id}`<br>user_policy: `arn:{partition}:iam::{account}:user/{user_id}/policy/{policy_id}`<br> |
| imagebuilder | component: `arn:{partition}:imagebuilder:{region}:{account}:component/{resource_id}`<br>distribution_configuration: `arn:{partition}:imagebuilder:{region}:{account}:distribution-configuration/{resource_id}`<br>image: `arn:{partition}:imagebuilder:{region}:{account}:image/{resource_id}`<br>image_pipeline: `arn:{partition}:imagebuilder:{region}:{account}:image-pipeline/{resource_id}`<br>infrastructure_configuration: `arn:{partition}:imagebuilder:{region}:{account}:infrastructure-configuration/{resource_id}`<br> |
| inspector | assessment_target: `arn:{partition}:inspector:{region}:{account}:target/{resource_id}`<br>assessment_template: `arn:{partition}:inspector:{region}:{account}:template/{resource_id}`<br>assessment_run: `arn:{partition}:inspector:{region}:{account}:run/{resource_id}`<br> |
| iot | authorizer: `arn:{partition}:iot:{region}:{account}:authorizer/${AuthorizerName}`<br>billing_group: `arn:{partition}:iot:{region}:{account}:billinggroup/${BillingGroupName}`<br>certificate: `arn:{partition}:iot:{region}:{account}:cert/${CertificateId}`<br>dimension: `arn:{partition}:iot:{region}:{account}:dimension/${DimensionName}`<br>policy: `arn:{partition}:iot:{region}:{account}:policy/${PolicyName}`<br>provisioning_template: `arn:{partition}:iot:{region}:{account}:provisioningtemplate/${TemplateName}`<br>rule: `arn:{partition}:iot:{region}:{account}:rule/${RuleName}`<br>scheduled_audit: `arn:{partition}:iot:{region}:{account}:scheduledaudit/${ScheduledAuditName}`<br>thing: `arn:{partition}:iot:{region}:{account}:thing/{resource_id}`<br>thing_group: `arn:{partition}:iot:{region}:{account}:thinggroup/{resource_id}`<br>thing_type: `arn:{partition}:iot:{region}:{account}:thingtype/{resource_id}`<br>topic_rule_destination: `arn:{partition}:iot:{region}:{account}:topic-rule-destination/{resource_id}`<br>topic_rule: `arn:{partition}:iot:{region}:{account}:rule/{resource_id}`<br>domain_configuration: `arn:{partition}:iot:{region}:{account}:domainconfiguration/{resource_id}`<br>fleet_indexing_configuration: `arn:{partition}:iot:{region}:{account}:fleet-indexing-configuration/{resource_id}`<br>job: `arn:{partition}:iot:{region}:{account}:job/{resource_id}`<br> |
| iot-device-tester | test_suite_run: `arn:{partition}:iot-device-tester:{region}:{account}:test-suite-run:${SuiteDefinitionId}/{resource_id}`<br> |
| iot1click-projects | device: `arn:{partition}:iot1click:{region}:{account}:device/{resource_id}`<br>placement: `arn:{partition}:iot1click:{region}:{account}:placement/{resource_id}`<br>project: `arn:{partition}:iot1click:{region}:{account}:project/{resource_id}`<br> |
| iotanalytics | channel: `arn:{partition}:iotanalytics:{region}:{account}:channel/{resource_id}`<br>dataset: `arn:{partition}:iotanalytics:{region}:{account}:dataset/{resource_id}`<br>datastore: `arn:{partition}:iotanalytics:{region}:{account}:datastore/{resource_id}`<br>pipeline: `arn:{partition}:iotanalytics:{region}:{account}:pipeline/{resource_id}`<br> |
| iotevents | input: `arn:{partition}:iotevents:{region}:{account}:input/{resource_id}`<br>detector_model: `arn:{partition}:iotevents:{region}:{account}:detector-model/{resource_id}`<br> |
| iotsitewise | asset_model: `arn:{partition}:iotsitewise:{region}:{account}:asset-model/{resource_id}`<br>gateway: `arn:{partition}:iotsitewise:{region}:{account}:gateway/{resource_id}`<br> |
| kafka | cluster: `arn:{partition}:kafka:{region}:{account}:cluster/{resource_id}`<br> |
| kinesis | stream: `arn:{partition}:kinesis:{region}:{account}:stream/{resource_id}`<br>firehose_delivery_stream: `arn:{partition}:firehose:{region}:{account}:deliverystream/{resource_id}`<br> |
| kinesis-video-archived-media | archive: `arn:{partition}:kinesisvideo:{region}:{account}:archive/{stream_id}/{archive_id}`<br>stream: `arn:{partition}:kinesisvideo:{region}:{account}:stream/{stream_id}/{stream_arn}`<br> |
| kinesis-video-media | stream: `arn:{partition}:kinesisvideo:{region}:{account}:stream/{stream_id}/{stream_arn}`<br> |
| kinesis-video-signaling | channel: `arn:{partition}:kinesisvideo:{region}:{account}:channel/{channel_name}/{channel_arn}`<br> |
| kms | key: `arn:{partition}:kms:{region}:{account}:key/{resource_id}`<br>alias: `arn:{partition}:kms:{region}:{account}:alias/{resource_id}`<br> |
| lakeformation | data_lake_settings: `arn:{partition}:lakeformation:{region}:{account}:datalake/{resource_id}/settings`<br>permissions: `arn:{partition}:lakeformation:{region}:{account}:permissions/{resource_id}`<br> |
| lambda | function: `arn:{partition}:lambda:{region}:{account}:function:{resource_id}`<br>layer: `arn:{partition}:lambda:{region}:{account}:layer:{resource_id}`<br>event_source_mapping: `arn:{partition}:lambda:{region}:{account}:event-source-mapping:{resource_id}`<br>event_invoke_config: `arn:{partition}:lambda:{region}:{account}:event-invoke-config:{resource_id}`<br> |
| lex | bot: `arn:{partition}:lex:{region}:{account}:bot:{resource_id}`<br>bot_alias: `arn:{partition}:lex:{region}:{account}:bot:{BotName}:alias:{resource_id}`<br>bot_channel: `arn:{partition}:lex:{region}:{account}:bot-channel:{BotName}:{BotAlias}:{ChannelName}`<br> |
| license-manager | license_configuration: `arn:{partition}:license-manager:{region}:{account}:license-configuration/{resource_id}`<br> |
| lightsail | instance: `arn:{partition}:lightsail:{region}:{account}:instance/{resource_id}`<br>key_pair: `arn:{partition}:lightsail:{region}:{account}:key-pair/{resource_id}`<br>static_ip: `arn:{partition}:lightsail:{region}:{account}:static-ip/{resource_id}`<br>load_balancer: `arn:{partition}:lightsail:{region}:{account}:loadbalancer/{resource_id}`<br>bucket: `arn:{partition}:lightsail:{region}:{account}:bucket/{resource_id}`<br> |
| logs | log_group: `arn:{partition}:logs:{region}:{account}:log-group:{resource_id}`<br>log_stream: `arn:{partition}:logs:{region}:{account}:log-group:{LogGroupName}:log-stream:{resource_id}`<br>metric_filter: `arn:{partition}:logs:{region}:{account}:metric-filter:{resource_id}`<br>destination: `arn:{partition}:logs:{region}:{account}:destination:{resource_id}`<br>query_definition: `arn:{partition}:logs:{region}:{account}:query-definition:{resource_id}`<br> |
| machinelearning | batch_prediction: `arn:{partition}:machinelearning:{region}:{account}:batchprediction/{resource_id}`<br>data_source: `arn:{partition}:machinelearning:{region}:{account}:datasource/{resource_id}`<br>evaluation: `arn:{partition}:machinelearning:{region}:{account}:evaluation/{resource_id}`<br>ml_model: `arn:{partition}:machinelearning:{region}:{account}:mlmodel/{resource_id}`<br> |
| macie | classification_job: `arn:{partition}:macie:{region}:{account}:classification-job/{resource_id}`<br>custom_data_identifier: `arn:{partition}:macie:{region}:{account}:custom-data-identifier/{resource_id}`<br>findings_filter: `arn:{partition}:macie:{region}:{account}:findings-filter/{resource_id}`<br>member_account: `arn:{partition}:macie:{region}:{account}:member-account/{resource_id}`<br>s3_object: `arn:{partition}:macie:{region}:{account}:s3-object/{resource_id}`<br> |
| managedblockchain | network: `arn:{partition}:managedblockchain:{region}:{account}:network/${NetworkId}`<br>node: `arn:{partition}:managedblockchain:{region}:{account}:node/${NetworkId}/${MemberId}/${NodeId}`<br>proposal: `arn:{partition}:managedblockchain:{region}:{account}:proposal/${NetworkId}/${ProposalId}`<br> |
| mediaconnect | flow: `arn:{partition}:mediaconnect:{region}:{account}:flow/{resource_id}`<br> |
| mediaconvert | queue: `arn:{partition}:mediaconvert:{region}:{account}:queue/{resource_id}`<br>preset: `arn:{partition}:mediaconvert:{region}:{account}:preset/{resource_id}`<br>job_template: `arn:{partition}:mediaconvert:{region}:{account}:jobTemplate/{resource_id}`<br> |
| medialive | channel: `arn:{partition}:medialive:{region}:{account}:channel:{resource_id}`<br> |
| mediapackage | channel: `arn:{partition}:mediapackage:{region}:{account}:channel/{resource_id}`<br>origin_endpoint: `arn:{partition}:mediapackage:{region}:{account}:origin_endpoint/{resource_id}`<br> |
| mediastore | container: `arn:{partition}:mediastore:{region}:{account}:container/{resource_id}`<br> |
| mediastore-data | object: `arn:{partition}:mediastore-data:{region}:{account}:object/{resource_id}`<br> |
| meteringmarketplace | product: `arn:{partition}:meteringmarketplace:{region}:{account}:product/{resource_id}`<br>usage_record: `arn:{partition}:meteringmarketplace:{region}:{account}:usage-record:{resource_id}`<br> |
| mgh | home_region_control: `arn:{partition}:mgh:{region}:{account}:homeRegionControl/{resource_id}`<br>migration_task: `arn:{partition}:mgh:{region}:{account}:migrationTask/{resource_id}`<br>progress_update_stream: `arn:{partition}:mgh:{region}:{account}:progressUpdateStream/{resource_id}`<br> |
| mobilehub | project: `arn:{partition}:mobilehub:{region}:{account}:project/{resource_id}`<br> |
| mq | broker: `arn:{partition}:mq:{region}:{account}:broker:{resource_id}`<br>configuration: `arn:{partition}:mq:{region}:{account}:configuration:{resource_id}`<br> |
| mturk | hit_type: `arn:{partition}:mturk:{region}:{account}:hittype/{resource_id}`<br>hit: `arn:{partition}:mturk:{region}:{account}:hit/{resource_id}`<br>qualification_type: `arn:{partition}:mturk:{region}:{account}:qualificationtype/{resource_id}`<br> |
| neptune-db | cluster: `arn:{partition}:neptune-db:{region}:{account}:cluster:{resource_id}`<br> |
| network-firewall | firewall_policy: `arn:{partition}:network-firewall:{region}:{account}:policy/{resource_id}`<br>firewall: `arn:{partition}:network-firewall:{region}:{account}:firewall/{resource_id}`<br>rule_group: `arn:{partition}:network-firewall:{region}:{account}:rulegroup/{resource_id}`<br> |
| networkmanager | global_network: `arn:{partition}:networkmanager:{region}:{account}:global-network/{resource_id}`<br>device: `arn:{partition}:networkmanager:{region}:{account}:device/{resource_id}`<br>link: `arn:{partition}:networkmanager:{region}:{account}:link/{resource_id}`<br>site: `arn:{partition}:networkmanager:{region}:{account}:site/{resource_id}`<br> |
| opensearch | domain: `arn:{partition}:opensearch:{region}:{account}:domain/{resource_id}`<br> |
| opsworks | stack: `arn:{partition}:opsworks:{region}:{account}:stack/{resource_id}`<br>layer: `arn:{partition}:opsworks:{region}:{account}:layer/{resource_id}`<br>app: `arn:{partition}:opsworks:{region}:{account}:app/{resource_id}`<br>instance: `arn:{partition}:opsworks:{region}:{account}:instance/{resource_id}`<br>user_profile: `arn:{partition}:opsworks:{region}:{account}:user-profile/{resource_id}`<br>permission: `arn:{partition}:opsworks:{region}:{account}:permission/{resource_id}`<br>deployment: `arn:{partition}:opsworks:{region}:{account}:deployment/{resource_id}`<br> |
| organizations | organization: `arn:{partition}:organizations::{account}:organization/{resource_id}`<br>account: `arn:{partition}:organizations::{account}:account/{resource_id}`<br>organizational_unit: `arn:{partition}:organizations::{account}:ou/{resource_id}`<br> |
| outposts | outpost: `arn:{partition}:outposts:{region}:{account}:outpost/{resource_id}`<br> |
| personalize | dataset_group: `arn:{partition}:personalize:{region}:{account}:dataset-group/{resource_id}`<br>dataset: `arn:{partition}:personalize:{region}:{account}:dataset/{dataset_group_arn}/dataset/{resource_id}`<br>solution: `arn:{partition}:personalize:{region}:{account}:solution/{resource_id}`<br>campaign: `arn:{partition}:personalize:{region}:{account}:campaign/{resource_id}`<br>event_tracker: `arn:{partition}:personalize:{region}:{account}:event-tracker/{resource_id}`<br> |
| pi | dimension: `arn:{partition}:pi:{region}:{account}:dimension:${resource_id}`<br> |
| pinpoint | app: `arn:{partition}:mobiletargeting:{region}:{account}:apps/${resource_id}`<br>adm_channel: `arn:{partition}:mobiletargeting:{region}:{account}:apps/${ApplicationId}/channels/adm`<br>apns_channel: `arn:{partition}:mobiletargeting:{region}:{account}:apps/${ApplicationId}/channels/apns`<br>apns_sandbox_channel: `arn:{partition}:mobiletargeting:{region}:{account}:apps/${ApplicationId}/channels/apns_sandbox`<br>baidu_channel: `arn:{partition}:mobiletargeting:{region}:{account}:apps/${ApplicationId}/channels/baidu`<br>email_channel: `arn:{partition}:mobiletargeting:{region}:{account}:apps/${ApplicationId}/channels/email`<br>gcm_channel: `arn:{partition}:mobiletargeting:{region}:{account}:apps/${ApplicationId}/channels/gcm`<br>sms_channel: `arn:{partition}:mobiletargeting:{region}:{account}:apps/${ApplicationId}/channels/sms}`<br> |
| polly | lexicon: `arn:{partition}:polly:{region}:{account}:lexicon/{resource_id}`<br> |
| qldb | ledger: `arn:{partition}:qldb:{region}:{account}:ledger/${resource_id}`<br> |
| quickSight | group: `arn:{partition}:quicksight:{region}:{account}:group/{resource_id}`<br>user: `arn:{partition}:quicksight:{region}:{account}:user/{resource_id}`<br> |
| ram | resource_share: `arn:{partition}:ram:{region}:{account}:resource-share/${resource_id}`<br>resource_share_invitation: `arn:{partition}:ram:{region}:{account}:resource-share-invitation/${resource_id}`<br> |
| rds | db_instance: `arn:{partition}:rds:{region}:{account}:db:{resource_id}`<br>db_snapshot: `arn:{partition}:rds:{region}:{account}:snapshot:{resource_id}`<br>db_cluster: `arn:{partition}:rds:{region}:{account}:cluster:{resource_id}`<br>db_cluster_snapshot: `arn:{partition}:rds:{region}:{account}:cluster-snapshot:{resource_id}`<br>option_group: `arn:{partition}:rds:{region}:{account}:og:{resource_id}`<br>parameter_group: `arn:{partition}:rds:{region}:{account}:pg:{resource_id}`<br>security_group: `arn:{partition}:rds:{region}:{account}:secgrp:{resource_id}`<br>subgroup: `arn:{partition}:rds:{region}:{account}:sub-group:{resource_id}`<br>event_subscription: `arn:{partition}:rds:{region}:{account}:es:{resource_id}`<br>global_cluster: `arn:{partition}:rds:{region}:{account}:global-cluster:${resource_id}`<br> |
| rds-data | secret: `arn:{partition}:secretsmanager:{region}:{account}:secret:{resource_id}`<br> |
| redshift | cluster: `arn:{partition}:redshift:{region}:{account}:cluster:${resource_id}`<br>snapshot: `arn:{partition}:redshift:{region}:{account}:snapshot:${resource_id}`<br> |
| rekognition | collection: `arn:{partition}:rekognition:{region}:{account}:collection/${resource_id}`<br>stream_processor: `arn:{partition}:rekognition:{region}:{account}:stream-processor/${resource_id}`<br> |
| resource-groups | group: `arn:{partition}:resource-groups:{region}:{account}:group/${resource_id}`<br> |
| robomaker | robot_application: `arn:{partition}:robomaker:{region}:{account}:robot-application/${ApplicationName}/${ApplicationVersion}`<br>simulation_application: `arn:{partition}:robomaker:{region}:{account}:simulation-application/${ApplicationName}/${ApplicationVersion}`<br>robot: `arn:{partition}:robomaker:{region}:{account}:robot/${RobotName}`<br>simulation_job: `arn:{partition}:robomaker:{region}:{account}:simulation-job/${SimulationJobArn}`<br>fleet: `arn:{partition}:robomaker:{region}:{account}:fleet/${FleetName}`<br> |
| route53 | health_check: `arn:{partition}:route53:::healthcheck/{resource_id}`<br>hosted_zone: `arn:{partition}:route53:::hostedzone/{resource_id}`<br>vpc_association_authorization: `arn:{partition}:route53:::vpc/{region}:{account}:authorizevpcassociation/{resource_id}/{vpc_id}`<br>resolver_endpoint: `arn:{partition}:route53resolver:{region}:{account}:resolver-endpoint/{resource_id}`<br>resolver_rule: `arn:{partition}:route53resolver:{region}:{account}:resolver-rule/{resource_id}`<br>resolver_rule_association: `arn:{partition}:route53resolver:{region}:{account}:resolver-rule-association/{resource_id}`<br> |
| s3 | bucket: `arn:{partition}:s3:::{resource_id}`<br>object: `arn:{partition}:s3:::{bucket}/{resource_id}`<br> |
| s3-object-lambda | access_point: `arn:{partition}:s3-object-lambda:{region}:{account}:accesspoint/${resource_id}`<br>access_point_policy: `arn:{partition}:s3-object-lambda:{region}:{account}:accesspoint-policy/${resource_id}`<br>access_point_configuration: `arn:{partition}:s3-object-lambda:{region}:{account}:accesspoint/${resource_id}/configuration`<br> |
| sagemaker | notebook_instance: `arn:{partition}:sagemaker:{region}:{account}:notebook-instance/${resource_id}`<br>notebook_instance_lifecycle_configuration: `arn:{partition}:sagemaker:{region}:{account}:notebook-instance-lifecycle-config/${resource_id}`<br>training_job: `arn:{partition}:sagemaker:{region}:{account}:training-job/${resource_id}`<br>processing_job: `arn:{partition}:sagemaker:{region}:{account}:processing-job/${resource_id}`<br>transform_job: `arn:{partition}:sagemaker:{region}:{account}:transform-job/${resource_id}`<br>model: `arn:{partition}:sagemaker:{region}:{account}:model/${resource_id}`<br>endpoint_config: `arn:{partition}:sagemaker:{region}:{account}:endpoint-config/${resource_id}`<br>endpoint: `arn:{partition}:sagemaker:{region}:{account}:endpoint/${resource_id}`<br>feature_group: `arn:{partition}:sagemaker:{region}:{account}:feature-group/${resource_id}`<br> |
| sdb | domain: `arn:{partition}:sdb:{region}:{account}:domain/${resource_id}`<br> |
| secretsmanager | secret: `arn:{partition}:secretsmanager:{region}:{account}:secret:${resource_id}`<br> |
| securityhub | hub: `arn:{partition}:securityhub:{region}:{account}:hub/default`<br>product_subscription: `arn:{partition}:securityhub:{region}:{account}:subscription/${resource_id}`<br> |
| serverlessrepo | application: `arn:{partition}:serverlessrepo:{region}:{account}:applications/${resource_id}`<br> |
| servicecatalog | product: `arn:{partition}:catalog:{region}:{account}:product/${resource_id}`<br>portfolio: `arn:{partition}:catalog:{region}:{account}:portfolio/${resource_id}`<br>portfolio_share: `arn:{partition}:catalog:{region}:{account}:share/${resource_id}`<br>cloudformation_stack_set_constraint: `arn:{partition}:cloudformation:{region}:{account}:stack-set/${StackSetName}:constraint/${resource_id}`<br> |
| servicediscovery | namespace: `arn:{partition}:servicediscovery:{region}:{account}:namespace/${resource_id}`<br>service: `arn:{partition}:servicediscovery:{region}:{account}:service/${resource_id}`<br> |
| ses | configuration_set: `arn:{partition}:ses:{region}:{account}:configuration-set/${resource_id}`<br> |
| shield | protection: `arn:{partition}:shield::{account}:protection/${resource_id}`<br> |
| signer | signing_profile: `arn:{partition}:signer:{region}:{account}:signing-profiles/${resource_id}`<br> |
| sms | app: `arn:{partition}:sms:{region}:{account}:app/${resource_id}`<br>server: `arn:{partition}:sms:{region}:{account}:server/${resource_id}`<br>replication_job: `arn:{partition}:sms:{region}:{account}:replication-job/${resource_id}`<br> |
| snowball | job: `arn:{partition}:snowball:{region}:{account}:job/${JobId}`<br> |
| sns | topic: `arn:{partition}:sns:{region}:{account}:${TopicName}`<br>subscription: `arn:{partition}:sns:{region}:{account}:${TopicName}:${SubscriptionId}`<br>platform_application_endpoint: `arn:{partition}:sns:{region}:{account}:app/${PlatformApplicationArn}/${EndpointId}`<br> |
| sqs | queue: `arn:{partition}:sqs:{region}:{account}:${QueueName}`<br> |
| ssm | document: `arn:{partition}:ssm:{region}:{account}:document/${DocumentName}`<br>parameter: `arn:{partition}:ssm:{region}:{account}:parameter/${ParameterName}`<br>maintenance_window: `arn:{partition}:ssm:{region}:{account}:maintenancewindow/${WindowId}`<br>maintenance_window_task: `arn:{partition}:ssm:{region}:{account}:maintenancewindow/${WindowId}/task/${WindowTaskId}`<br>patch_baseline: `arn:{partition}:ssm:{region}:{account}:patchbaseline/${BaselineId}`<br> |
| sso | instance: `arn:{partition}:sso:{region}:{account}:instance/${resource_id}`<br>permission_set: `arn:{partition}:sso:{region}:{account}:permissionSet/${resource_id}`<br> |
| sso-directory | directory: `arn:{partition}:sso-directory:{region}:{account}:directory/${resource_id}`<br> |
| stepfunctions | state_machine: `arn:{partition}:states:{region}:{account}:stateMachine:${resource_id}`<br> |
| storagegateway | gateway: `arn:{partition}:storagegateway:{region}:{account}:gateway/${resource_id}`<br>share: `arn:{partition}:storagegateway:{region}:{account}:share/${resource_id}`<br>tape: `arn:{partition}:storagegateway:{region}:{account}:tape/${resource_id}`<br>volume: `arn:{partition}:storagegateway:{region}:{account}:gateway/${gateway_id}/volume/${volume_id}`<br> |
| sts | assumed_role: `arn:{partition}:sts::{account}:assumed-role/${resource_name}/${resource_id}`<br>federated_user: `arn:{partition}:sts::{account}:federated-user/${resource_id}`<br>oidc_provider: `arn:{partition}:iam::{account}:oidc-provider/${resource_id}`<br>saml_provider: `arn:{partition}:iam::{account}:saml-provider/${resource_id}`<br> |
| swf | domain: `arn:{partition}:swf:{region}:{account}:domain/${resource_id}`<br>workflow_type: `arn:{partition}:swf:{region}:{account}:workflowType/${DomainName}/${resource_id}`<br>activity_type: `arn:{partition}:swf:{region}:{account}:activityType/${DomainName}/${resource_id}`<br>workflow_execution: `arn:{partition}:swf:{region}:{account}:workflow/${DomainName}/${WorkflowType}:${resource_id}`<br>activity_execution: `arn:{partition}:swf:{region}:{account}:activity/${DomainName}/${ActivityType}:${resource_id}`<br> |
| synthetics | canary: `arn:{partition}:synthetics:{region}:{account}:canary:${resource_id}`<br>canary_run: `arn:{partition}:synthetics:{region}:{account}:canary:${CanaryName}:run:${resource_id}`<br> |
| textract | document: `arn:{partition}:textract:{region}:{account}:document/${resource_id}`<br> |
| transcribe | vocabulary: `arn:{partition}:transcribe:{region}:{account}:vocabulary/${resource_id}`<br> |
| transfer | server: `arn:{partition}:transfer:{region}:{account}:server/${resource_id}`<br>user: `arn:{partition}:transfer:{region}:{account}:user/${ServerId}/${resource_id}`<br> |
| translate | terminology: `arn:{partition}:translate:{region}:{account}:terminology/${resource_id}`<br> |
| waf | ipset: `arn:{partition}:waf:{region}:{account}:ipset/${resource_id}`<br>rule: `arn:{partition}:waf:{region}:{account}:rule/${resource_id}`<br>rule_group: `arn:{partition}:waf::{account}:rulegroup/${resource_name}/${resource_id}`<br>web_acl: `arn:{partition}:waf:{region}:{account}:webacl/${resource_id}`<br>global_web_acl: `arn:{partition}:waf::{account}:global-webacl/${resource_name}/${resource_id}`<br>rate_based_rule: `arn:{partition}:waf::{account}:ratebasedrule/${resource_name}/${resource_id}`<br> |
| waf-regional | ipset: `arn:{partition}:waf-regional:{region}:{account}:ipset/${resource_id}`<br>regional_rule: `arn:{partition}:waf-regional:{region}:{account}:rule/${resource_id}`<br>regional_web_acl: `arn:{partition}:waf-regional:{region}:{account}:webacl/${resource_id}`<br>regional_rule_group: `arn:{partition}:waf-regional:{region}:{account}:rulegroup/${RuleGroupName}/${resource_id}`<br>regional_rate_based_rule: `arn:{partition}:waf-regional:{region}:{account}:rule/${resource_id}`<br> |
| wafv2 | ip_set: `arn:{partition}:wafv2:{region}:{account}:/ipset/${resource_scope}/${resource_id}`<br>rule_group: `arn:{partition}:wafv2:{region}:{account}:/rulegroup/${resource_scope}/${resource_id}`<br>web_acl: `arn:{partition}:wafv2:{region}:{account}:/webacl/${resource_scope}/${resource_id}`<br> |
| wellarchitected | workload: `arn:{partition}:wellarchitected:{region}:{account}:workload/${resource_id}`<br> |
| workdocs | document: `arn:{partition}:workdocs:{region}:{account}:${FolderHierarchy}/${resource_id}`<br>folder: `arn:{partition}:workdocs:{region}:{account}:${FolderHierarchy}/${resource_id}`<br>user: `arn:{partition}:workdocs:{region}:{account}:user/${resource_id}`<br> |
| worklink | fleet: `arn:{partition}:worklink:{region}:{account}:fleet/${resource_id}`<br>website_certificate_authority_association: `arn:{partition}:worklink:{region}:{account}:website-certificate-authority-association/${resource_id}`<br> |
| workmail | organization: `arn:{partition}:workmail:{region}:{account}:organization/${resource_id}`<br>resource: `arn:{partition}:workmail:{region}:{account}:resource/${resource_id}`<br>user: `arn:{partition}:workmail:{region}:{account}:user/${resource_id}`<br> |
| workspaces | directory: `arn:{partition}:workspaces:{region}:{account}:directory/${resource_id}`<br>workspace: `arn:{partition}:workspaces:{region}:{account}:workspace/${resource_id}`<br> |
