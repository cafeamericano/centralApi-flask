# General imports
from flask import Blueprint
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

@AppGalleryLiteAPI.route("/AppGalleryLite/api/applications")
def sendApplications():
    dataset = appsCollection.find()
    return jsonResponse(dataset)

@AppGalleryLiteAPI.route("/AppGalleryLite/api/keywords")
def sendKeywords():
    dataset = keywordsCollection.find()
    return jsonResponse(dataset)