# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 17:39:18 2017

@author: Suresh Chellappan

"""

#Import the encessary packages
from pymongo import MongoClient
import pprint


#Function to query the mongoDB
def queryMongo(collection, query):
    results = collection.find({'$text':{'$search': query}})
    for result in results:
        pprint.pprint(result)

#Main function that initialises the connection for DB and calls the queryMongo()
if __name__ == "__main__":
    query = input("Kindly Enter the Search keyword: ")
    client = MongoClient('mongodb://localhost:27017/')
    db = client.guardian
    collection = db.articles
    queryMongo(collection, "trump")
