

## **Introduction**

  

NSE Scraper can be used to get the equity data from the page.
Please check this [file](https://github.com/chetankalewar1/PrivateCircleTest/blob/main/NSEScrapper/NSEScrapper/spiders/nse_spider.py) for scraping info.
You need a Django server running on the local , since this scrapper dumps the data to database via API.  
Clone the Django server for this project from this  [link1](https://github.com/chetankalewar1/PrivateCircleServer)  or [link2](https://github.com/chetankalewar1/PrivateCircleServer) for Mongo based server.

## **Setup**

  

-   **Libraries used:**
    1.  Scrapy
	2.  Requests
    

-   **Install Dependencies**
    
    1.  IDE Pycharm
        
    2.  Run ‘`pip install -r requirements.txt’` to install the remaining necessary packages.
        

## **Data Obtained**

symbol, open, high, low, ltp, etc..
    

## **Usage Module Examples**

1.  class _**NSEIndia**_
    
    1.  This class scrapes equity related data from [nse india.](https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm)
    2. Dumps the data to Django via API(Do check the server_url in parse_api function of this class.)
        


## **Points to Remember**

-   You need to clone the Django server for this project from this  [link1](https://github.com/chetankalewar1/PrivateCircleServer)  or [link2](https://github.com/chetankalewar1/PrivateCircleServer) for Mongo based server.
    

## **Run**

-   Refer / Run  `scrapy runspider NSEScrapper/NSEScrapper/spiders/nse_spider.py`.
