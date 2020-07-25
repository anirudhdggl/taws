#!/bin/bash

BUCKET=<enter the bucket name>

aws s3 sync s3://$BUCKET/ <path to mount-point>