# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



# Import the necessary packages
import pymongo


#Import scrapy packages
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class CrawlerPipeline(object):
    

#Get the MongoDB values from scrapy settings file and initialize the connection    
    def __init__(self):
            connection = pymongo.MongoClient(
                    settings['MONGODB_SERVER'],
                    settings['MONGODB_PORT']
                    )
            db = connection[settings['MONGODB_DB']]
            self.collection = db[settings['MONGODB_COLLECTION']]
            print (self.collection)
 
#Process the article data returned by the spider:crawler to insert into MongoDB       
    def process_item(self, item, spider):
            valid = True
            for data in item:
                if not data:
                    valid = False
                    raise DropItem("Missing {0}!".format(data))
            #Tag List has values with /n, hence - it needs to be stripped out. 
            if valid:
                for i in range(0,len(item['Tags'])):
                    item['Tags'][i] = item['Tags'][i].strip()
            
            self.collection.insert(dict(item))
                
            log.msg("Document Inserted")
            return item
