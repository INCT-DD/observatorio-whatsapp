from pymongo import MongoClient

client = MongoClient("mongodb://host:port/")
database = client["whatsapp"]
collection = database["group_participants"]

query = {}
query["gjid"] = {
    u"$type": 2.0
}

query["jid"] = {
    u"$type": 2.0
}

cursor = collection.find(query)