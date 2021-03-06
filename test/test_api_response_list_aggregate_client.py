# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import ChronoSheetsAPI
from ChronoSheetsAPI.ChronoSheetsClientLibModel.api_response_list_aggregate_client import ApiResponseListAggregateClient  # noqa: E501
from ChronoSheetsAPI.rest import ApiException

class TestApiResponseListAggregateClient(unittest.TestCase):
    """ApiResponseListAggregateClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ApiResponseListAggregateClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = ChronoSheetsAPI.models.api_response_list_aggregate_client.ApiResponseListAggregateClient()  # noqa: E501
        if include_optional :
            return ApiResponseListAggregateClient(
                data = [
                    ChronoSheetsAPI.models.aggregate_client.AggregateClient(
                        client_projects = [
                            ChronoSheetsAPI.models.aggregate_project.AggregateProject(
                                id = 56, 
                                client_id = 56, 
                                organisation_id = 56, 
                                project_name = '0', 
                                cost_estimation = 1.337, 
                                start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                                end_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                            ], 
                        id = 56, 
                        organisation_id = 56, 
                        client_name = '0', 
                        client_address_line1 = '0', 
                        client_address_line2 = '0', 
                        client_suburb = '0', 
                        client_state = '0', 
                        client_post_code = '0', 
                        person_of_contact = '0', 
                        client_phone_number = '0', 
                        client_mobile_number = '0', 
                        client_email_address = '0', 
                        client_web_url = '0', 
                        project_count = 56, )
                    ], 
                status = 'Succeeded', 
                message = '0'
            )
        else :
            return ApiResponseListAggregateClient(
        )

    def testApiResponseListAggregateClient(self):
        """Test ApiResponseListAggregateClient"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
