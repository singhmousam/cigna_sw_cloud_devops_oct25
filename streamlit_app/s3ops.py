"""Perform all S3 related operations"""
import os
from dotenv import load_dotenv
from boto3 import Session
import boto3

# Load environment variables from .env file
load_dotenv('../.env')

class S3Ops:
    def __init__(self):
        access_key = os.getenv('AWS_ACCESS_KEY', 
                                    '')
        secret_key = os.getenv('AWS_SECRET_KEY', 
                                    '')
        self.session = Session(aws_access_key_id=access_key,
                               aws_secret_access_key=secret_key)
        # print('Access Key:', self.access_key)
        self.client = self.session.client('s3')

    def upload_file(self, bucket_name, file_path, file_object):
        """
        """
        try:
            print(f'Upload file {file_path.split('/')[-1]} on {bucket_name}')
            self.client.upload_fileobj(file_object, bucket_name, file_path)
        except Exception as e:
            print('Error occured: ' + str(e))

        