
import imp
import json
from unittest.mock import call
from urllib import request
import scrapy
import requests
import time

url = "https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm"


class NSEIndia(scrapy.Spider):
    name = 'nseindia'
    start_urls = [url]
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en;q=0.9",
        "Host": "www1.nseindia.com",
        "Referer": "https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm",
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }


    def parse(self, response):
        dataUrl = "https://www1.nseindia.com/live_market/dynaContent/live_watch/stock_watch/niftyStockWatch.json"
        request = scrapy.Request(dataUrl, callback=self.parse_api, headers=self.headers,)
        yield request

    def parse_api(self, response):
        server_url = "http://localhost:8000/api/v1/equitystockwatch/"
        # Get the data
        raw_data = response.body
        data = json.loads(raw_data)

        for company in data["data"]:
            # Make api call to django server
            dicter1 = {
                "symbol": company["symbol"],
                "open": float(company["open"].replace(",", "")),
                "high": float(company["high"].replace(",", "")),
                "low": float(company["low"].replace(",", "")),
                "ltp": float(company["ltP"].replace(",", "")),
                "change": float(company["ptsC"].replace(",", "")),
                "change_percent": float(company["per"].replace(",", "")),
                "volume": float(company["trdVol"].replace(",", "")),
                "turnover": float(company["ntP"].replace(",", "")),
                "high_52": float(company["wkhi"].replace(",", "")),
                "low_52": float(company["wklo"].replace(",", "")),
                "chang_percent_365": float(company["yPC"].replace(",", "")),
                "chang_percent_30": float(company["mPC"].replace(",", ""))
            }
            r = requests.post(server_url, data=dicter1, )
            if not r.status_code == 201:
                print(r.json(), "//////////////////////////")
                raise Exception("Issue in dumping Data to the server.")

            time.sleep(0.5)

        yield data
