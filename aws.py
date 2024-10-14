import boto3
from botocore.exceptions import NoCredentialsError

# AWS profile
session = boto3.Session(profile_name='rioprofile')

# Create S3 client
s3 = session.client('s3')

bucket_name = 'riotintos3-enriched-data'
file_name = 'enriched.csv'
s3_file_name = 'enriched-from-boto3.csv'

try:
    s3.create_bucket(Bucket=bucket_name)
    s3.upload_file(file_name, bucket_name, s3_file_name)
    print(f"File {file_name} uploaded successfully to {bucket_name}")
except FileNotFoundError:
    print("The file was not found")
except NoCredentialsError:
    print("Credentials not available")
