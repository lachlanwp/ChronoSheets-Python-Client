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
from ChronoSheetsClientLibApi.projects_api import ProjectsApi  # noqa: E501
from ChronoSheetsAPI.rest import ApiException


class TestProjectsApi(unittest.TestCase):
    """ProjectsApi unit test stubs"""

    def setUp(self):
        self.api = ChronoSheetsClientLibApi.projects_api.ProjectsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_projects_create_project(self):
        """Test case for projects_create_project

        Create a project  # noqa: E501
        """
        pass

    def test_projects_get_project_by_id(self):
        """Test case for projects_get_project_by_id

        Get project by Id  # noqa: E501
        """
        pass

    def test_projects_get_projects_for_client(self):
        """Test case for projects_get_projects_for_client

        Get projects for a particular client  # noqa: E501
        """
        pass

    def test_projects_update_project(self):
        """Test case for projects_update_project

        Update a project  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
