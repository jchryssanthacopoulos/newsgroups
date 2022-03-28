#!/bin/bash


# copy to S3
aws s3 mv emails.tar.gz s3://funnel-share/emails.tar.gz

# update permissions
aws s3api put-object-acl --bucket funnel-share --key emails.tar.gz --acl public-read
