from utils.s3ops import S3Ops
from flask import Flask
from flask import render_template, request
import config

s3_obj = S3Ops()

app = Flask(__name__)

@app.route('/')
def home():
    return "AWS Operation application"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file_obj = request.files['uploaded_file']
        # request_json = request.json
        s3_obj.upload__file(file_obj, config.bucket_name, )
