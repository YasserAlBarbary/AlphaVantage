class SeriesType:
    _series_typeList = [
        "close",
        "open",
        "high",
        "low"
    ]

    def __init__(self):
        self._series_type = "close"

    def get_series_type(self):
        return self._series_type

    def set_series_type(self, series_type_value):
        if series_type_value in self._series_typeList:
            self._series_type = series_type_value
        else:
            raise ValueError("Series type invalid.")


