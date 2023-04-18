FROM python:3.10-alpine

WORKDIR /app
COPY app /app
RUN pip3 install -r requirements.txt

EXPOSE 8090
ENTRYPOINT ["python3","hello_world.py"]
