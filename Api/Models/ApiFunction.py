class Function:
    _functionList = [
        #
        "SYMBOL_SEARCH",

        #
        "TIME_SERIES_INTRADAY",
        "TIME_SERIES_DAILY",
        "TIME_SERIES_WEEKLY",
        "TIME_SERIES_MONTHLY",

        # latest price
        "GLOBAL_QUOTE",

        # Technical Indicators
        "SMA",
        "EMA",
    ]

    def __init__(self):
        self._function = "SYMBOL_SEARCH"

    def get_function(self):
        return self._function

    def set_function(self, function_name):
        if function_name in self._functionList:
            self._function = function_name
        else:
            raise ValueError("Function not found.")


