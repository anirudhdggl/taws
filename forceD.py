import json
import urllib.parse
import boto3
s3 = boto3.client('s3')
def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    
    if len(key.split('/')) > 1:
        objectUploadedInFolder = True

    i = 0

    source = ""
    while i < len(key):
        if key[i] == '+':
            source += " "
        else:
            source += key[i]
        
        i = i + 1

    destination = "uploads/"

    if objectUploadedInFolder:
        i = 0
        ReadingMainDir = True
        while ReadingMainDir:
            if key[i] == '/':
                ReadingMainDir = False
                i = i + 1
            else:
                i = i + 1
        
        while i < len(key):
            destination += key[i]
            i = i + 1

    
    else:
        destination += key
    

    i = 0
    path = ""
    while i < len(destination):
        if destination[i] == '+':
            path += " "
        
        else:
            path += destination[i]
        
        i = i + 1
    
    try:
        response = s3.copy_object(
            ACL='public-read',
            Bucket=bucket,
            ContentDisposition='attachment',
            CopySource={
                'Bucket': bucket,
                'Key': source,
            },
            MetadataDirective='REPLACE',
            Key=destination
        )
        
    except Exception as e:
        print(e)