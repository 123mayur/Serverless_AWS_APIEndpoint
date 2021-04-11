import boto3
import json

def lambda_handler_start(event, context):
    inputParams = json.loads(json.dumps(event))
    sevice_Id =inputParams['id']
    instances = [sevice_Id]
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=instances)
    ec2.delete_tags(Resources=instances, Tags=[{'Key':'Schedule', 'Value':'True'}])

def lambda_handler_stop(event, context):
    inputParams = json.loads(json.dumps(event))
    sevice_Id =inputParams['id']
    instances = [sevice_Id]
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=instances)
    ec2.delete_tags(Resources=instances, Tags=[{'Key':'Schedule', 'Value':'True'}])
