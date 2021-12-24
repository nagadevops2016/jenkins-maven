

import logging
import boto3
from botocore.exceptions import ClientError

# Retrieve the list of existing buckets
s3 = boto3.client('s3', aws_access_key_id='AKIA6LQSYPWOAZDZTOMC',
 aws_secret_access_key='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')


for bucket in s3.buckets.all():
    print (bucket.name)
