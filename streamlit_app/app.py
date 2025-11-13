import streamlit as st
from s3ops import S3Ops

st.title('AWS S3 Operations App')
st.write('S3 File Uplaod Application')

s3_obj = S3Ops()
bucket_name = 'ms-custom-data-bucket'

uploaded_file = st.file_uploader('Choose a file to upload')

if uploaded_file is not None:
    filename = uploaded_file.name
    if st.button('Upload to S3'):
        try:
            s3_obj.upload_file(bucket_name, filename, uploaded_file)
            print("File uploaded successfully")
            st.write("File uploaded successfully")
        except Exception as e:
            print('Error occured: ', str(e))
            st.write("File upload failed. Check logs")
            