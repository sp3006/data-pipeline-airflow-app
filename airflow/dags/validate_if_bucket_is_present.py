import uuid
import boto3
import boto3.session
import time
import airflow
from botocore.exceptions import ClientError
# creating the connection
s3 = boto3.client('s3')
s3_resource = boto3.resource('s3')

def get_s3_keys(bucket):
    """Get a list of keys in an S3 bucket."""
    keys = []
    resp = s3.list_objects_v2(Bucket=bucket)
    for obj in resp['Contents']:
        keys.append(obj['Key'])
    return keys

def create_bucket_name(bucket_prefix):
    # The generated bucket name must be between 3 and 63 chars long
      return ''.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    bucket_response = s3_connection.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'})
    print(bucket_name, current_region)
    return bucket_name, bucket_response

udacity_bucket_name, response =create_bucket( bucket_prefix ='udacity-dend', s3_connection=s3_resource.meta.client)

