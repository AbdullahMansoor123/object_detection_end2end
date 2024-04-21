FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y

RUN apt-get update 
RUN apt-get install ffmpeg libsm6 libxext6 unzip -y
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]