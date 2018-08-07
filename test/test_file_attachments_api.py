# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import ChronoSheetsAPI
from ChronoSheetsClientLibApi.file_attachments_api import FileAttachmentsApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestFileAttachmentsApi(unittest.TestCase):
    """FileAttachmentsApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.file_attachments_api.FileAttachmentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_file_attachments_get_my_file_attachments(self):
        """Test case for file_attachments_get_my_file_attachments

        Get my file attachments.  Get files you've attached to timesheets.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
