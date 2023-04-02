from flask import Flask, jsonify
from pymongo import MongoClient
import random

app = Flask(__name__)

MONGO_HOST = 'mongo1,mongo2,mongo3'
MONGO_PORT = 27017
MONGO_DBNAME = 'stajdb'
MONGO_USERNAME = 'stajuser'
MONGO_PASSWORD = 'your-stajuser-password'
MONGO_REPLICA_SET = 'my-replica-set'
MONGO_AUTH_SOURCE = 'admin'

# create MongoClient instance
client = MongoClient(
    f'mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONGO_DBNAME}?replicaSet={MONGO_REPLICA_SET}&authSource={MONGO_AUTH_SOURCE}'
)

# client = MongoClient('mongodb://stajuser:your-stajuser-password@mongo1,mongo2,mongo3/?replicaSet=my-replica-set&authSource=admin')

# # get the stajdb database
# db = client[MONGO_DBNAME]


db = client['stajdb']
iller = db['iller']
ulkeler = db['ulkeler']

@app.route("/")
def hello():
    return "Merhaba Python!"

@app.route("/staj")
def get_random_il():
    # MongoDB'den rastgele bir il verisi çekme
    # il = iller.aggregate([{ '$sample': { 'size': 1 } }]).next()
    # return jsonify(il)
    return "Staj"

@app.route("/pythonapp")
def get_random_il_pythonapp():
    # MongoDB'den rastgele bir il verisi çekme
    # il = iller.aggregate([{ '$sample': { 'size': 1 } }]).next()
    # return jsonify(il)
    return "Staj pythonapp"

@app.route('/iller')
def get_iller():
    data = []
    for doc in iller.find():
        data.append(doc)
    return {'data': data}

if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=4444)
    app.run(host='0.0.0.0', port=4444)