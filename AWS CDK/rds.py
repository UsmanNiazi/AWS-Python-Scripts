from aws_cdk import (
    # Duration,
    Stack,aws_rds as rds, aws_ec2 as ec2, aws_iam as iam ,Environment, aws_s3 as s3, aws_quicksight, aws_s3_deployment,
    RemovalPolicy , aws_glue as glue, aws_lambda as lambda_, Duration,
    # aws_sqs as sqs,
)

from constructs import Construct
import os
class DemoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "My-VPC",
        cidr="10.8.0.0/16")
        #https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html bootstraping 

       

        securitygroup1=ec2.SecurityGroup(self,"My SG",
        vpc=vpc,allow_all_outbound=True,
        security_group_name="SecurityGroup")


        #https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_rds/README.html
        MyDB = rds.DatabaseInstance(self, "cluster",
        allocated_storage=30, 
        security_groups=[securitygroup1],
        engine=rds.DatabaseInstanceEngine.postgres(version=rds.PostgresEngineVersion.VER_13_4),
        instance_type=ec2.InstanceType.of(ec2.InstanceClass.M6I, ec2.InstanceSize.XLARGE),       
        database_name="myDB",
        credentials=rds.Credentials.from_generated_secret("admin"),  # Optional - will default to 'admin' username and generated password
        vpc=vpc, max_allocated_storage=1000,
        vpc_subnets=ec2.SubnetSelection(
        subnet_type=ec2.SubnetType.PUBLIC))

        MyDB.connections.allow_from_any_ipv4(ec2.Port.all_traffic(),"Allow to Postgres")
        MyDB.connections.allow_default_port_internally(description="Allow Default")

        MyDB.add_rotation_single_user(
        automatically_after=Duration.days(7),  # defaults to 30 days
        )
        
        

     