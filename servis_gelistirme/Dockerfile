FROM python:3.8-slim-buster
LABEL Name=flask_app Version=0.0.1

RUN pip install websockets

COPY ./servis_gelistirme.py /app/
# Change the working directory
WORKDIR /app/
# Set "python" as the entry point
ENTRYPOINT ["python"]
# Set the command as the script name
CMD [ "servis_gelistirme.py" ]