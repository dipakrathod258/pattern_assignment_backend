import logging

from pymongo import MongoClient


mongodb_client = MongoClient(connect=False, host="127.0.0.1")


def insert_doc_to_mongodb(mongodb_name, mongodb_collection_name, mongodb_document):
    """
    :param mongodb_name: Name of the MongoDB Database
    :param mongodb_collection_name: Name of the MongoDB Collection
    :param mongodb_document: The Mongodb Document to be inserted
    :return: This function returns the ID of the last inserted document in the database
    """
    try:
        mongodb = mongodb_client[mongodb_name]
        mongodb_collection = mongodb[mongodb_collection_name]
        mongodb_insert_response = mongodb_collection.insert_one(mongodb_document)
        mongodb_doc_id = str(mongodb_insert_response.inserted_id)
        return mongodb_doc_id
    except Exception as err:
        logging.error(f"#src #connections #mongo_connections insert_doc_to_mongodb #ERROR: {str(err)}")
