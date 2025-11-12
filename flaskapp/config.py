import configparser
from configparser import ConfigParser

## SOILD Principles
config = configparser.ConfigParser()
config = ConfigParser('./config.ini')

import boto3

se_client = boto3.client('s3')
se_client.put_object()
bucket_name = config['aws']['bucket_name']

import PyYaml
config = PyYaml('./config.yaml')

bucket_name = config['aws']['bucket_name']

import json
json.load('config.json')

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
database_url = os.getenv("DATABASE_URL")
api_key = os.getenv("API_KEY")