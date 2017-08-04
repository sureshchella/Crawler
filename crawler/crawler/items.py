# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Date = scrapy.Field()
    Headline = scrapy.Field()
    Author = scrapy.Field()
    Topic = scrapy.Field()
    Snippet = scrapy.Field()
    Tags = scrapy.Field()
    DateUpdated = scrapy.Field()
    pass
