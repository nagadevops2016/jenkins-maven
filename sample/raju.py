

import logging
import boto3


# Retrieve the list of existing buckets
s3 = boto3.resource('s3', aws_access_key_id='AKIA6LQSYPWOAZDZTOMC',
 aws_secret_access_key='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')


for bucket in s3.buckets.all():
    print (bucket.name)
    
allbuckets = s3resource.list_buckets()

# Header Line for the output going to standard out
print('Bucket'.ljust(45) + 'Size in Bytes'.rjust(25))
for bucket in conn.get_all_buckets():
	total_bytes = 0
	name = bucket.name
	for key in bucket:
		total_bytes += key.size
	total_bytes = total_bytes/1024/1024/1024
	print ("Bucket Name:" ,name, "Size: ",total_bytes ,"GB")
