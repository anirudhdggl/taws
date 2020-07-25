#!/bin/bash

RANDOM=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

aws s3api create-bucket efs-sync-$RANDOM

aws s3 sync <path to mount-point> s3://efs-sync-$RANDOM

echo "s3://efs-sync-$RANDOM"