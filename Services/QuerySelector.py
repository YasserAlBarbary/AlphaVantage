import requests

from Api.Models.ApiFunction import Function
from Api.Models.ApiKey import Session
from Api.Models.Interval import Interval
from Api.Models.SeriesType import SeriesType
from Api.Models.Symbol import Symbol
from Api.Models.TimePeriod import TimePeriod


class Query:
    def __init__(self):
        self.function = Function()
        self.session = Session()
        self.interval = Interval()
        self.series_type = SeriesType()
        self.symbol = Symbol()
        self.TimePeriod = TimePeriod()

        self.url = f'https://www.alphavantage.co/query?'

    def get_symbol_data(self):
        self.session.set_api_key(
            input("Enter your API key.\n")
        )
        keyword = input("Enter your search keyword.\n")
        self.symbol.set_symbol(
            input()
        )
        url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={keyword}&apikey={self.session.get_api_key()}'
        r = requests.get(url)
        data = r.json()["bestMatches"]

        print("Enter the number corresponding to the required symbol.\n")
        resultDict = {}
        for i, result in enumerate(data, start=1):
            resultDict[i] = result
            print(i, "  ", result["2. name"])

        symbolId = int(input())
        print(f'{resultDict[symbolId]["2. name"]} is selected.')
        self.symbol.set_symbol(resultDict[symbolId]["2. name"])
        
        return resultDict[symbolId]

    def select_main_function(self,):
        query_id = input("Press:\n"
                         "1 for Historical prices\n"
                         "2 for current quote\n"
                         "3 for technical indicators\n")
        return query_id

    def select_secondary_function(self, query_id):
        if query_id == 1:
            time_frame_query = self.get_timeframe()
            interval = self.get_interval()
        if query_id == 2:
            pass
        if query_id == 3:
            pass

    def get_timeframe(self,):
        time_frame = input("Press:\n"
                         "1 for Intraday\n"
                         "2 for Daily\n"
                         "3 for Weekly\n"
                         "4 for Monthly\n")


    def get_interval(self,):
