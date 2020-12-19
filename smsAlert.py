#############################################
## NOTE:- SMS may be charged by AWS. Please
## Review the pricing for your desired region
#############################################

import logging
import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#############################################
## VARIABLES
#############################################

#Enter the region name here
aws_region = "us-east-1"

#Enter the phone number you want to send message to
phone_number = "+911234567890"

message_text = "Enter the text that you want to send in the SMS"

#Code to send the SMS
session = boto3.Session(
    region_name = aws_region
)

sns_client = session.client('sns')


def lambda_handler(event, context):

# The message type has been set to transactional
# as promotional messages can be lost and are not
# guaranteed delivery.
    response = sns_client.publish(
        PhoneNumber = phone_number,
        Message = message_text,
        MessageAttributes={
            'AWS.SNS.SMS.SenderID': {
                'DataType': 'String',
                'StringValue': 'SENDERID'
            },
            'AWS.SNS.SMS.SMSType': {
                'DataType': 'String',
                'StringValue': 'Transactional'
            }
        }
    )

    logger.info(response)
    return 'Message Sent'