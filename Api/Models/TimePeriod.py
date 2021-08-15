class TimePeriod:
    def __init__(self):
        self._time_period = "0"

    def get_time_period(self):
        return self._time_period

    def set_time_period(self, time_period_value):
        if time_period_value > 0:
            self._time_period = str(time_period_value)
        else:
            raise ValueError("Time period invalid.")


