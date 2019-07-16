from bson.regex import Regex
from pymongo import MongoClient

client = MongoClient("mongodb://host:port/")
database = client["whatsapp"]
collection = database["messages"]

query = {}
query["key_remote_jid"] = Regex(u".*@g\\.us.*", "i")
query["media_url"] = {
    u"$type": 2.0
}

cursor = collection.find(query)
