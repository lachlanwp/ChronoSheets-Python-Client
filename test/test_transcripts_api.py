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
from ChronoSheetsClientLibApi.transcripts_api import TranscriptsApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestTranscriptsApi(unittest.TestCase):
    """TranscriptsApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.transcripts_api.TranscriptsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_transcripts_get_my_transcripts(self):
        """Test case for transcripts_get_my_transcripts

        Get my file transcripts.  Get audio to text transcripts that you've created.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
