#!/bin/bash

#make sure that the database is empty in this RDS

BUCKET_NAME=<enter the bucket name of sql dump here>

sudo su
snap install aws-cli
pip install awscli

aws configure

mkdir ~/dump/

aws s3 sync s3://$BUCKET_NAME/sql-dump ~/dump/

mysql -h <hostname> -u <username> -p <database> < ~/dump/dump.sql

#optional steps if you want to change domain name too
#e.g. from abc.com to xy.abc.com or xy.com
#Uncomment the below code to run it

# cd path/to/your/wordpress/ > /dev/null && wp search-replace --allow-root "https://abc.com" "https://xyc.com"

#you may add other values like www.abc.com to www.xyc.com