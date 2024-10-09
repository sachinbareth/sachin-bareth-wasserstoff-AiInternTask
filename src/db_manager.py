from pymongo import MongoClient

def connect_db(uri, db_name, collection_name):
    client = MongoClient(uri)
    db = client[db_name]
    return db[collection_name]

def store_summary_and_keywords(db, filename, summary, keywords):
    db.update_one(
        {'filename': filename},
        {'$set': {'summary': summary, 'keywords': keywords}},
        upsert=True
    )

def get_all_documents(db):
    # Retrieve all documents from the MongoDB collection
    return list(db.find({}, {'_id': 0}))  # Exclude the MongoDB document ID (_id)


