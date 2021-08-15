class Interval:
    _intervalList = [
        "1min",
        "5min",
        "15min",
        "30min",
        "60min",
        "daily",
        "weekly",
        "monthly"
    ]

    def __init__(self):
        self._interval = ""

    def get_interval(self):
        return self._interval

    def set_interval(self, interval_value):
        if interval_value in self._intervalList:
            self._interval = interval_value
        else:
            raise ValueError("Interval invalid.")


