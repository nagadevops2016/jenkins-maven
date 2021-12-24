from boto.s3.connection import S3Connection

conn = S3Connection('AKIA6LQSYPWOCJBNHKW6','cWfJjNJRyqDPEU7m8ul+YgISO9eIvBkV2PNPpS2R')
bucket = conn.get_bucket('bucket')
for key in bucket.list():
    print(key.name.encode('utf-8'))
