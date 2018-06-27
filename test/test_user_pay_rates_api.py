# coding: utf-8

"""
    ChronoSheets API

    ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  # noqa: E501

    OpenAPI spec version: v1
    Contact: lachlan@chronosheets.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ChronoSheetsAPI
from ChronoSheetsClientLibApi.user_pay_rates_api import UserPayRatesApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestUserPayRatesApi(unittest.TestCase):
    """UserPayRatesApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.user_pay_rates_api.UserPayRatesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_user_pay_rates_create_pay_rate(self):
        """Test case for user_pay_rates_create_pay_rate

        Create a new pay rate for a particular user, archiving the previous pay rate  # noqa: E501
        """
        pass

    def test_user_pay_rates_get_pay_rates(self):
        """Test case for user_pay_rates_get_pay_rates

        Get a collection of pay rates for a particular user, specified by user id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
