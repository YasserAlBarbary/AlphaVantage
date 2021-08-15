class Session:

    def __init__(self):
        self._api_key = "demo"

    def set_api_key(self, api_key):
        self._api_key = api_key

    def get_api_key(self):
        return self._api_key