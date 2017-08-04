# Crawler
Crawl and Extract the data from website and Parse, Process it further to push it to database.


Following is the folder hierarchy:

![ScreenShot](https://github.com/sureshchella/Crawler/blob/master/Snippets/Structure.JPG)

#Crawler.py:

Main Python code that extacts the data from the news website pertaining to specific tags. 

Code needs to be invoked through command line by: scrapy crawl crawler -a tags="science"

If the command line argument is not provided - the scraper considers tag as default (international). 


#pipelilnes.py

captures data from crawler.py and process it further. Once done, data gets inserted into MongoDB

#settings

consists of pipeline and mongodb parameters



Once done, below is the snippet of the document structure in MongoDB:
![ScreenShot](https://github.com/sureshchella/Crawler/blob/master/Snippets/Mongo.JPG)

#Query the stored data

Once everything is done, Lets query the results. 

1. CrawlAPI.py - connects to the mongodb and queries the results using PyMongo. 

2. MongoDB Index Configuration:
   For text searches - "text" index was added to the columns in the document:
   db.articles.createIndex( { "Topic": "text" } )
   db.articles.createIndex( { "Snippet": "text" } )
   
3. Python code is called by:  python crawlAPI (using console)
   Which will prompt for search keyword as shown below:
   ![ScreenShot](https://github.com/sureshchella/Crawler/blob/master/Snippets/Results-2.JPG)
   
   If the search result is none - respective messages are shown (similar to above snippet). 
   
   If there are results found:
   ![ScreenShot](https://github.com/sureshchella/Crawler/blob/master/Snippets/Result-1.JPG)
