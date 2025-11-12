"""Perform all S3 related operations"""
import os
from dotenv import load_dotenv
from boto3 import Session
import boto3

# Load environment variables from .env file
load_dotenv()

class S3Ops:
    def __init__(self):
        self.access_key = os.getenv('AWS_ACCESS_KEY', 
                                    'Pass expected access key id')
        self.secret_key = os.getenv('AWS_SECRET_KEY', 
                                    'Pass expected access key id')
        self.session = Session(aws_access_key_id=self.access_key,
                               aws_secret_access_key=self.secret_key)
        self.client = self.session.client('s3')
        self.client = boto3.client('s3')

    def upload__file(self, bucket_name, file_path, file_object):
        """
        """
        try:
            print(f'Upload file {file_path.split('/')[-1]} on {bucket_name}')
            self.client.upload_fileobj(file_object, bucket_name, file_path)
        except Exception as e:
            print('Error occured: ' + str(e))

        