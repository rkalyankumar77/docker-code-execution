FROM python:3.12-slim
COPY requirements_docker_image.txt requirements.txt
RUN pip install -r requirements.txt