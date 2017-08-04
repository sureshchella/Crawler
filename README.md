# Crawler
Crawl and Extract the data from website and Parse, Process it further to push it to database.


Following is the folder hierarchy:

![Alt text](F:/Suresh/Isentia/Structure.JPG?raw=true "Optional Title")

#Crawler.py:

Main Python code that extacts the data from the news website pertaining to specific tags. 

Code needs to be invoked through command line by: scrapy crawl crawler -a tags="science"

If the command line argument is not provided - the scraper considers tag as default (international). 


#pipelilnes.py

captures data from crawler.py and process it further. Once done, data gets inserted into MongoDB

#settings

consists of pipeline and mongodb parameters

