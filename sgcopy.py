#!/usr/bin/env python

import boto3
import argparse
import textwrap

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
  description=textwrap.dedent('''\
    sgcopy copies the rules of one of your security group to another security group.
    Please take care of the following points:

    1. You must have your aws credentials configured
    2. You cannot copy a rule if it involves another security group as it's source/description and that SG is already present in the destination security group

    You can ignore the 2nd point if you do not have a SG added in your destination SG as source/destination. If it's still unclear, simply run. It'll give you a clear error so you know what you're doing wrong.
    ''')
)

parser.add_argument("--id", help="Set this flag if using security group ID instead of name. You can't set outbound rules without using ID", action="store_true")
parser.add_argument("source", help="Source security group name/ID")
parser.add_argument("destination", help="destination security group name/ID")

args = parser.parse_args()

ec2 = boto3.client('ec2')

if args.id:
  if (args.source[0:3] != 'sg-') or (args.destination[0:3] != 'sg-'):
    exit("Enter a security Group ID when using --id flag")
  sg = ec2.describe_security_groups(
    GroupIds = [
      args.source
    ]
  )

else:
  sg = ec2.describe_security_groups(
    GroupNames = [
      args.source
    ]
  )

inboundRules = sg['SecurityGroups'][0]['IpPermissions']
outboundRules = sg['SecurityGroups'][0]['IpPermissionsEgress']

if args.id:
  response_ingress = ec2.authorize_security_group_ingress(
    GroupId = args.destination,
    IpPermissions = inboundRules
  )
  response_egress = ec2.authorize_security_group_egress(
    GroupId = args.destination,
    IpPermissions = outboundRules
  )
else:
  response_ingress = ec2.authorize_security_group_ingress(
    GroupName = args.destination,
    IpPermissions = inboundRules
  )