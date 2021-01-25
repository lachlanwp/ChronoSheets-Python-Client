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
from ChronoSheetsAPI.model.api_response_organisation import ApiResponseOrganisation
from ChronoSheetsAPI.model.api_response_update_organisation_response import ApiResponseUpdateOrganisationResponse
from ChronoSheetsAPI.model.update_organisation_request import UpdateOrganisationRequest


class OrganisationApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __organisation_get_organisation(
            self,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get your organisation.    Requires 'OrganisationAdmin' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.organisation_get_organisation(x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token

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
                ApiResponseOrganisation
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
            return self.call_with_http_info(**kwargs)

        self.organisation_get_organisation = Endpoint(
            settings={
                'response_type': (ApiResponseOrganisation,),
                'auth': [],
                'endpoint_path': '/Organisation/GetOrganisation',
                'operation_id': 'organisation_get_organisation',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'x_chronosheets_auth',
                ],
                'required': [
                    'x_chronosheets_auth',
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
                },
                'attribute_map': {
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'x_chronosheets_auth': 'header',
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
            callable=__organisation_get_organisation
        )

        def __organisation_update_organisation(
            self,
            x_chronosheets_auth,
            request,
            **kwargs
        ):
            """Update an organisation.    Requires 'OrganisationAdmin' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.organisation_update_organisation(x_chronosheets_auth, request, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token
                request (UpdateOrganisationRequest): An Update Organsation Request object containing updated fields.  Make sure to specify the Organsation Id in the request object so that ChronoSheets knows which Organsation to update

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
                ApiResponseUpdateOrganisationResponse
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

        self.organisation_update_organisation = Endpoint(
            settings={
                'response_type': (ApiResponseUpdateOrganisationResponse,),
                'auth': [],
                'endpoint_path': '/Organisation/UpdateOrganisation',
                'operation_id': 'organisation_update_organisation',
                'http_method': 'PUT',
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
                        (UpdateOrganisationRequest,),
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
            callable=__organisation_update_organisation
        )
