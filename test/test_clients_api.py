# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ChronoSheetsAPI
from ChronoSheetsClientLibApi.clients_api import ClientsApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestClientsApi(unittest.TestCase):
    """ClientsApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.clients_api.ClientsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_clients_create_client(self):
        """Test case for clients_create_client

        Create a client.    Requires the 'ManageClientsAndProjects' permission.  # noqa: E501
        """
        pass

    def test_clients_get_client(self):
        """Test case for clients_get_client

        Get a particular client.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.  # noqa: E501
        """
        pass

    def test_clients_get_clients(self):
        """Test case for clients_get_clients

        Get a collection of clients that are under your organisation.    Requires the 'ManageClientsAndProjects' or 'ManageJobsAndTask' permissions.  # noqa: E501
        """
        pass

    def test_clients_update_client(self):
        """Test case for clients_update_client

        Update a client.    Requires the 'ManageClientsAndProjects' permission.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
