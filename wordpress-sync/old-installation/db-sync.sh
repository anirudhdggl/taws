#!/bin/bash

sudo su

snap install aws-cli
pip install awscli

aws configure

mkdir ~/sql-dump

mysqldump -h <hostname of rds> -u <user> -p <dbname> > ~/sql-dump/dump.sql

#next it will prompt for DB password

RANDOM=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

aws s3api create-bucket --bucket db-sync-wordpress-$RANDOM

aws s3 sync ~/sql-dump s3://db-sync-wordpress-RANDOM/sql-dump

echo "Your SQL dump has been successfully uploaded to the bucket s3://db-sync-wordpress-$RANDOM"