import unittest
import sys
from io import StringIO
from unittest.mock import patch

from Services.QueryBuilder import Query


class test_Query(unittest.TestCase):

    def setUp(self) -> None:
        self.query = Query()

    def tearDown(self) -> None:
        pass

    def test_run(self) -> None:
        pass

    def test_build_query(self) -> None:
        pass

    def test_retrieve_symbol_data(self) -> None:
        pass

    def test_select_main_function(self) -> None:
        pass

    def test_retrieve_interval(self) -> None:
        pass

    def test_retrieve_intraday_interval(self) -> None:
        pass

    def test_retrieve_historical_prices(self) -> None:
        pass

    def test_retrieve_current_quote(self) -> None:
        pass

    def test_retrieve_technical_indicators(self) -> None:
        pass

    def test_retrieve_period(self) -> None:
        pass

    def test_retrieve_series_type(self) -> None:
        pass