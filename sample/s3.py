import boto3

session = boto3.Session( 
         aws_access_key_id='AKIAZIJX3N3NP62RM2FK', 
         aws_secret_access_key='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')


#Then use the session to get the resource
s3 = session.resource('s3')

my_bucket = s3.Bucket('ramesh123-openhift')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
