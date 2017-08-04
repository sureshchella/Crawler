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

