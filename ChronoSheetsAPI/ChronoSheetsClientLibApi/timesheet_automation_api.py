"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ChronoSheetsAPI.api_client import ApiClient, Endpoint
from ChronoSheetsAPI.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ChronoSheetsAPI.model.api_response_for_paginated_list_timesheet_automation_with_org_and_geofence import ApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from ChronoSheetsAPI.model.create_automation_step_request import CreateAutomationStepRequest


class TimesheetAutomationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __timesheet_automation_create_automation_step(
            self,
            x_chronosheets_auth,
            request,
            **kwargs
        ):
            """Creates an automation step.  Timesheet automation is determined by looking at steps taken by the user.  Create a step to log some automation action, such as entering a geofence or tapping on an NFC badge.  Requires the 'SubmitTimesheets' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.timesheet_automation_create_automation_step(x_chronosheets_auth, request, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token
                request (CreateAutomationStepRequest):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponseInt32
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            kwargs['request'] = \
                request
            return self.call_with_http_info(**kwargs)

        self.timesheet_automation_create_automation_step = Endpoint(
            settings={
                'response_type': (ApiResponseInt32,),
                'auth': [],
                'endpoint_path': '/TimesheetAutomation/CreateAutomationStep',
                'operation_id': 'timesheet_automation_create_automation_step',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_chronosheets_auth',
                    'request',
                ],
                'required': [
                    'x_chronosheets_auth',
                    'request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'x_chronosheets_auth':
                        (str,),
                    'request':
                        (CreateAutomationStepRequest,),
                },
                'attribute_map': {
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'x_chronosheets_auth': 'header',
                    'request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'multipart/form-data'
                ],
                'content_type': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'application/x-www-form-urlencoded',
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__timesheet_automation_create_automation_step
        )

        def __timesheet_automation_get_timesheet_automation_audit_trail(
            self,
            geofence_id,
            nfc_id,
            user_id,
            sort,
            order,
            x_chronosheets_auth,
            **kwargs
        ):
            """Retrieve the timesheet automation / alerts for geofences activities or NFC tap on/off.  Requires the 'ManageGeofencing' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.timesheet_automation_get_timesheet_automation_audit_trail(geofence_id, nfc_id, user_id, sort, order, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                geofence_id (int): The ID of the Geofence
                nfc_id (int):
                user_id (int):
                sort (str):
                order (str):
                x_chronosheets_auth (str): The ChronoSheets Auth Token

            Keyword Args:
                skip (int): Skip this many records. [optional]
                take (int): Take this many records. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                ApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['geofence_id'] = \
                geofence_id
            kwargs['nfc_id'] = \
                nfc_id
            kwargs['user_id'] = \
                user_id
            kwargs['sort'] = \
                sort
            kwargs['order'] = \
                order
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.timesheet_automation_get_timesheet_automation_audit_trail = Endpoint(
            settings={
                'response_type': (ApiResponseForPaginatedListTimesheetAutomationWithOrgAndGeofence,),
                'auth': [],
                'endpoint_path': '/TimesheetAutomation/GetTimesheetAutomationAuditTrail',
                'operation_id': 'timesheet_automation_get_timesheet_automation_audit_trail',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'geofence_id',
                    'nfc_id',
                    'user_id',
                    'sort',
                    'order',
                    'x_chronosheets_auth',
                    'skip',
                    'take',
                ],
                'required': [
                    'geofence_id',
                    'nfc_id',
                    'user_id',
                    'sort',
                    'order',
                    'x_chronosheets_auth',
                ],
                'nullable': [
                ],
                'enum': [
                    'sort',
                    'order',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('sort',): {

                        "USERNAME": "UserName",
                        "AUTOMATIONACTIONTYPE": "AutomationActionType",
                        "CLIENTDATETIME": "ClientDateTime",
                        "ISPROCESSED": "IsProcessed"
                    },
                    ('order',): {

                        "ASCENDING": "Ascending",
                        "DESCENDING": "Descending"
                    },
                },
                'openapi_types': {
                    'geofence_id':
                        (int,),
                    'nfc_id':
                        (int,),
                    'user_id':
                        (int,),
                    'sort':
                        (str,),
                    'order':
                        (str,),
                    'x_chronosheets_auth':
                        (str,),
                    'skip':
                        (int,),
                    'take':
                        (int,),
                },
                'attribute_map': {
                    'geofence_id': 'GeofenceId',
                    'nfc_id': 'NfcId',
                    'user_id': 'UserId',
                    'sort': 'Sort',
                    'order': 'Order',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                    'skip': 'Skip',
                    'take': 'Take',
                },
                'location_map': {
                    'geofence_id': 'query',
                    'nfc_id': 'query',
                    'user_id': 'query',
                    'sort': 'query',
                    'order': 'query',
                    'x_chronosheets_auth': 'header',
                    'skip': 'query',
                    'take': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/json',
                    'application/xml',
                    'text/xml',
                    'multipart/form-data'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__timesheet_automation_get_timesheet_automation_audit_trail
        )
