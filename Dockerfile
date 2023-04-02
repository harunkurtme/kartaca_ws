FROM ubuntu:20.04
LABEL Name=kartaca_ws Version=0.0.1

# RUN echo "rs.initiate({_id: 'rs0', members: [{_id: 0, host: 'mongo-master:27017'}, {_id: 1, host: 'mongo-slave1:27018'}, {_id: 2, host: 'mongo-slave3:27019'}]})" >> /docker-entrypoint-initdb.d/mongo-init.js
