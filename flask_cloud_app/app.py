from utils.s3ops import S3Ops
from flask import Flask
from flask import render_template, request
import config
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename

s3_obj = S3Ops()

app = Flask(__name__)
app.secret_key = b'your_high_key'

@app.route('/')
def home():
    return "AWS Operation application"


## Use of flash and secure_filename 
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file uploaded")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "" or not file.filename.endswith(".txt"):
            flash("No selected file, Invalid txt file")
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            try:
                s3_obj.upload_file(config.bucket_name, filename, file)
                flash(f"File '{filename}' uploaded successfully to S3.")
            except Exception as e:
                flash(f"Upload failed: {str(e)}")
            return redirect(request.url)
    return render_template("upload.html")

if __name__ == '__main__':
    app.run(debug=True)