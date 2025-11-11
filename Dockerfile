FROM ubuntu

WORKDIR /app

COPY . .
CMD pip install -r requirements.tx
EXPOSE 8080

ENTRYPOINT ["python", "app.py"]