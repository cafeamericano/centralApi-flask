# General imports
from flask import Flask, Blueprint, request, jsonify
import os

# MongoDB specific imports
import pymongo
from bson import json_util, ObjectId
import json

# Define database
myclient = pymongo.MongoClient(os.getenv('DB_URL', "mongodb://localhost:27017"))
database = myclient[(os.getenv('DB_NAME', "local-database-name"))]

# Define collections
appsCollection = database["apps"]
keywordsCollection = database["keywords"]

# Define blueprint
AppGalleryLiteAPI = Blueprint('AppGalleryLiteAPI', __name__)

# Define reusable functions

def bsonToJson(item):
    return json.loads(json_util.dumps(item))

def jsonResponse(dataset):
    arr = []
    for item in dataset:
        arr.append(bsonToJson(item))
    return json.dumps(arr)

# Begin routes

@AppGalleryLiteAPI.route("/AppGalleryLite/api/applications", methods=['GET', 'POST', 'PUT', 'DELETE'])
def sendApplications():

    if request.method == 'GET':
        dataset = appsCollection.find().sort([("isFeatured", pymongo.DESCENDING), ("publishDate", pymongo.DESCENDING) ])
        return jsonResponse(dataset)

    if request.method == 'POST':
        appsCollection.insert_one(request.json)
        return jsonify(
            code=200,
            msg="Success"
        )

    if request.method == 'PUT':
        myquery = {'_id': ObjectId(request.json['_id'])}
        appsCollection.replace_one(myQuery, request.json, upsert=True)
        return jsonify(
            code=200,
            msg="Success"
        )

    if request.method == 'DELETE':
        appsCollection.delete_one({'_id': ObjectId(request.json['_id'])})
        return jsonify(
            code=200,
            msg="Success"
        )

@AppGalleryLiteAPI.route("/AppGalleryLite/api/keywords", methods=['GET', 'POST', 'PUT', 'DELETE'])
def sendKeywords():

    if request.method == 'GET':
        dataset = keywordsCollection.find().sort([("type", pymongo.ASCENDING), ("name", pymongo.ASCENDING)])
        return jsonResponse(dataset)
    
    if request.method == 'POST':
        keywordsCollection.insert_one(request.json)
        return jsonify(
            code=200,
            msg="Success"
        )

    if request.method == 'PUT':
        myquery = {'_id': ObjectId(request.json['_id'])}
        keywordsCollection.replace_one(myQuery, request.json, upsert=True)
        return jsonify(
            code=200,
            msg="Success"
        )

    if request.method == 'DELETE':
        keywordsCollection.delete_one({'_id': ObjectId(request.json['_id'])})
        return jsonify(
            code=200,
            msg="Success"
        )