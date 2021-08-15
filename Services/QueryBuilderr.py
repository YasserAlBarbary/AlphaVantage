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

    def build_query(self):
        self.retrieve_symbol_data()
        self.select_main_function()
        self.url += f'&apikey={self.session.get_api_key()}'

    def retrieve_symbol_data(self):
        self.session.set_api_key(
            input("Enter your API key.\n")
        )
        keyword = input("Enter your search keyword.\n")

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

        print(resultDict[symbolId])

    def select_main_function(self, ):
        query_id = int(input("Press:\n"
                             "1 for Historical prices\n"
                             "2 for current quote\n"
                             "3 for technical indicators\n"))
        if query_id == 1:
            self.retrieve_historical_prices()
        if query_id == 2:
            self.retrieve_current_quote()
        if query_id == 3:
            self.retrieve_technical_indicators()

    def retrieve_interval(self):
        # 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
        intraday_interval = int(input("Select intraday interval\nPress:\n"
                                      "1 for 1min\n"
                                      "2 for 5min\n"
                                      "3 for 15min\n"
                                      "4 for 30min\n"
                                      "5 for 60min\n"
                                      "6 for daily\n"
                                      "7 for weekly\n"
                                      "8 for monthly\n"))
        if intraday_interval == 1:
            self.interval.set_interval("1min")
        if intraday_interval == 2:
            self.interval.set_interval("5min")
        if intraday_interval == 3:
            self.interval.set_interval("15min")
        if intraday_interval == 4:
            self.interval.set_interval("30min")
        if intraday_interval == 5:
            self.interval.set_interval("60min")
        if intraday_interval == 6:
            self.interval.set_interval("daily")
        if intraday_interval == 7:
            self.interval.set_interval("weekly")
        if intraday_interval == 8:
            self.interval.set_interval("monthly")
        else:
            raise ValueError("Wrong value for interval, please restart")

        self.url += f'&interval={self.interval.get_interval()}'

    def retrieve_intraday_interval(self):
        # 1min, 5min, 15min, 30min, 60min
        intraday_interval = int(input("Select intraday interval\nPress:\n"
                                      "1 for 1min\n"
                                      "2 for 5min\n"
                                      "3 for 15min\n"
                                      "4 for 30min\n"
                                      "5 for 60min\n"))
        if intraday_interval == 1:
            self.interval.set_interval("1min")
        if intraday_interval == 2:
            self.interval.set_interval("5min")
        if intraday_interval == 3:
            self.interval.set_interval("15min")
        if intraday_interval == 4:
            self.interval.set_interval("30min")
        if intraday_interval == 5:
            self.interval.set_interval("60min")
        else:
            raise ValueError("Wrong value for intraday interval, please restart")
        self.url += f'&interval={self.interval.get_interval()}'

    def retrieve_historical_prices(self):
        time_frame = int(input("Select Time Frame\nPress:\n"
                               "1 for Intraday\n"
                               "2 for Daily\n"
                               "3 for Weekly\n"
                               "4 for Monthly\n"))
        if time_frame == 1:
            self.function.set_function("TIME_SERIES_INTRADAY")
        if time_frame == 2:
            self.function.set_function("TIME_SERIES_DAILY")
        if time_frame == 3:
            self.function.set_function("TIME_SERIES_WEEKLY")
        if time_frame == 4:
            self.function.set_function("TIME_SERIES_MONTHLY")
        else:
            raise ValueError("Wrong value for time frame, please restart")
        self.url += f'function={self.function.get_function()}&symbol={self.symbol.get_symbol()}'

        # if time frame is intraday, we need to add interval too
        if time_frame == 1:
            self.retrieve_intraday_interval()

    def retrieve_current_quote(self):
        self.function.set_function("GLOBAL_QUOTE")
        self.url += f'function={self.function.get_function()}&symbol={self.symbol.get_symbol()}'

    def retrieve_technical_indicators(self):
        self.function.set_function("SMA")
        self.url += f'function={self.function.get_function()}&symbol={self.symbol.get_symbol()}'
        self.retrieve_interval()
        self.retrieve_period()
        self.retrieve_series_type()

    def retrieve_period(self):
        time_period = int(input("Select time period\nChoose any positive integer:\n"))
        self.TimePeriod.set_time_period(time_period)
        self.url += f'&time_period={self.TimePeriod.get_time_period()}'

    def retrieve_series_type(self):
        # close, open, high, low
        series_type = int(input("Select series type\nPress:\n"
                                      "1 for close\n"
                                      "2 for open\n"
                                      "3 for high\n"
                                      "4 for low\n"
                                      ))
        if series_type == 1:
            self.series_type.set_series_type("close")
        if series_type == 2:
            self.series_type.set_series_type("open")
        if series_type == 3:
            self.series_type.set_series_type("high")
        if series_type == 4:
            self.series_type.set_series_type("low")

        else:
            raise ValueError("Wrong value for intraday interval, please restart")
        self.url += f'&interval={self.interval.get_interval()}'