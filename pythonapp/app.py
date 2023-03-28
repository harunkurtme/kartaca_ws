from flask import Flask, jsonify
from pymongo import MongoClient
import random

app = Flask(__name__)

client = MongoClient('mongodb://stajuser:your-stajuser-password@mongo1,mongo2,mongo3/?replicaSet=my-replica-set&authSource=admin')
db = client['stajdb']
iller = db['iller']
ulkeler = db['ulkeler']

@app.route("/")
def hello():
    return "Merhaba Python"

@app.route("/staj")
def get_random_il():
    # MongoDB'den rastgele bir il verisi çekme
    # il = iller.aggregate([{ '$sample': { 'size': 1 } }]).next()
    # return jsonify(il)
    return "Staj"

if __name__ == '__main__':
    #from waitress import serve
    #serve(app, host="0.0.0.0", port=4444)
    app.run(host='0.0.0.0', port=4444)