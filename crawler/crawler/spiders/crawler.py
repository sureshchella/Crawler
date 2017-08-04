# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:05:41 2017

@author: Suresh Chellappan
"""

################################################################################################
########### Packages management ################################################################

#Packages installed
#1. Scrapy
#2. Readability

#Load the necessary paakcages
import scrapy
from scrapy import Spider
from crawler.items import CrawlerItem

import datetime as dt


#Class Definition for the Scrapy crawler
class ArticleExtracter(Spider):
    name = "articleExtracter"
    
#Intialise the start request function 
    def start_requests(self):
        url = 'https://www.theguardian.com'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + '/' + tag
        else:
            url = url + '/international'
        yield scrapy.Request(url, self.parse)

#Get all the links present with in the page and pass it to Parse_article for extracting data
    def parse(self, response):
       for href in response.xpath("//a[@class='u-faux-block-link__overlay js-headline-text']/@href").extract():
           yield response.follow(href, self.parse_article)
    
    try:
        def parse_article(self, response):
            def extract_with_css(query):
                return response.css(query).extract_first(default='Not-Found').strip()
            
            if response.xpath("//span[@itemprop='name']/text()").extract_first() is None:
                author = response.xpath("//p[@class='byline']/text()").extract_first().strip()
            else:
                author = response.xpath("//span[@itemprop='name']/text()").extract_first().strip()
            
            item = CrawlerItem()
            item['Date'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            item['Headline'] = extract_with_css('h1.content__headline::text')
            item['Author'] = author
            item['Topic'] = extract_with_css('div.content__section-label a::text')
            item['Snippet'] = extract_with_css('p::text')
            item['Tags'] = response.css('li.submeta__link-item a::text').extract()
            item['DateUpdated'] = extract_with_css('p.content__dateline time::text')
            yield item
        
    except Exception as e:
        pass
