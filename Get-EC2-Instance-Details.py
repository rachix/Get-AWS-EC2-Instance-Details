import json
import boto3
import re

def lambda_handler(event, context):
    client = boto3.client("ec2")

    # Get the information about all the instances
    status = client.describe_instances()
    print(status)
    print("-" * 30)

    for i in status["Reservations"]:
        instance_details = i["Instances"][0]
        if instance_details["State"]["Name"].lower() in ["shutting-down","stopped","stopping","terminated"]:
            print("Instance ID: ", instance_details["InstanceId"])
            print("Instance Current State: ", instance_details["State"]["Name"].lower())
            print("Instance Launch Time: ", instance_details["LaunchTime"])
            print("Instance Stop Time: ",  re.findall("\((.*?) *\)", instance_details["StateTransitionReason"]),)
            print("Instance State Change Reason: ", instance_details["StateTransitionReason"])
            print("\n")

    return {"statusCode": 200, "body": json.dumps("OK")}
