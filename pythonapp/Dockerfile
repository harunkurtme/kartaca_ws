FROM python:3.8-slim-buster
LABEL Name=pythonapp Version=0.0.1

RUN pip install flask
RUN pip install pymongo
#RUN pip install waitress
# Copy the source code to app folder
COPY ./app.py /app/
# Change the working directory
WORKDIR /app/
# Set "python" as the entry point
ENTRYPOINT ["python"]
# Set the command as the script name
CMD [ "app.py" ]