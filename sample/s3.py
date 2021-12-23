import boto3

session = boto3.Session( 
         aws_access_key_id='AKIA6LQSYPWOAZDZTOMC', 
         aws_secret_access_key='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')


#Then use the session to get the resource
s3 = session.resource('s3')

my_bucket = s3.Bucket('ramesh123-openhift')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
