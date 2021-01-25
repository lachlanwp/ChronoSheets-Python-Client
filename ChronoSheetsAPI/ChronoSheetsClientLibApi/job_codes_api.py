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
from ChronoSheetsAPI.model.api_response_boolean import ApiResponseBoolean
from ChronoSheetsAPI.model.api_response_int32 import ApiResponseInt32
from ChronoSheetsAPI.model.api_response_job_code import ApiResponseJobCode
from ChronoSheetsAPI.model.api_response_list_job_code import ApiResponseListJobCode
from ChronoSheetsAPI.model.insert_job_code_request import InsertJobCodeRequest
from ChronoSheetsAPI.model.update_job_code_request import UpdateJobCodeRequest


class JobCodesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __job_codes_create_job_code(
            self,
            x_chronosheets_auth,
            request,
            **kwargs
        ):
            """Create a job code.    Requires the 'ManageJobsAndTask' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.job_codes_create_job_code(x_chronosheets_auth, request, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token
                request (InsertJobCodeRequest): An Insert JobCode Request object containing values for the new JobCode to create

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

        self.job_codes_create_job_code = Endpoint(
            settings={
                'response_type': (ApiResponseInt32,),
                'auth': [],
                'endpoint_path': '/JobCodes/CreateJobCode',
                'operation_id': 'job_codes_create_job_code',
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
                        (InsertJobCodeRequest,),
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
            callable=__job_codes_create_job_code
        )

        def __job_codes_delete_job_code(
            self,
            job_code_id,
            x_chronosheets_auth,
            **kwargs
        ):
            """Delete a job code.    Requires the 'ManageJobsAndTask' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.job_codes_delete_job_code(job_code_id, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                job_code_id (int): The ID of the job code you want to delete
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
                ApiResponseBoolean
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
            kwargs['job_code_id'] = \
                job_code_id
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.job_codes_delete_job_code = Endpoint(
            settings={
                'response_type': (ApiResponseBoolean,),
                'auth': [],
                'endpoint_path': '/JobCodes/DeleteJobCode',
                'operation_id': 'job_codes_delete_job_code',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'job_code_id',
                    'x_chronosheets_auth',
                ],
                'required': [
                    'job_code_id',
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
                    'job_code_id':
                        (int,),
                    'x_chronosheets_auth':
                        (str,),
                },
                'attribute_map': {
                    'job_code_id': 'JobCodeId',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'job_code_id': 'query',
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
            callable=__job_codes_delete_job_code
        )

        def __job_codes_get_job_code_by_id(
            self,
            job_code_id,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get a particular job code by job code id.    Requires 'SubmitTimesheets' or 'ManageJobsAndTasks' permissions.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.job_codes_get_job_code_by_id(job_code_id, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                job_code_id (int): The ID of the JobCode you want to get
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
                ApiResponseJobCode
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
            kwargs['job_code_id'] = \
                job_code_id
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.job_codes_get_job_code_by_id = Endpoint(
            settings={
                'response_type': (ApiResponseJobCode,),
                'auth': [],
                'endpoint_path': '/JobCodes/GetJobCodeById',
                'operation_id': 'job_codes_get_job_code_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'job_code_id',
                    'x_chronosheets_auth',
                ],
                'required': [
                    'job_code_id',
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
                    'job_code_id':
                        (int,),
                    'x_chronosheets_auth':
                        (str,),
                },
                'attribute_map': {
                    'job_code_id': 'JobCodeId',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'job_code_id': 'query',
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
            callable=__job_codes_get_job_code_by_id
        )

        def __job_codes_get_job_codes(
            self,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get job codes for your organisation.    Requires 'SubmitTimesheets' or 'ManageJobsAndTasks' permissions.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.job_codes_get_job_codes(x_chronosheets_auth, async_req=True)
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
                ApiResponseListJobCode
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

        self.job_codes_get_job_codes = Endpoint(
            settings={
                'response_type': (ApiResponseListJobCode,),
                'auth': [],
                'endpoint_path': '/JobCodes/GetJobCodes',
                'operation_id': 'job_codes_get_job_codes',
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
            callable=__job_codes_get_job_codes
        )

        def __job_codes_update_job_code(
            self,
            x_chronosheets_auth,
            request,
            **kwargs
        ):
            """Update a job code.    Requires the 'ManageJobsAndTask' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.job_codes_update_job_code(x_chronosheets_auth, request, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token
                request (UpdateJobCodeRequest): A Update JobCode Request object containing updated fields.  Make sure to specify the JobCode Id in the request object so that ChronoSheets knows which JobCode to update

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
                ApiResponseBoolean
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

        self.job_codes_update_job_code = Endpoint(
            settings={
                'response_type': (ApiResponseBoolean,),
                'auth': [],
                'endpoint_path': '/JobCodes/UpdateJobCode',
                'operation_id': 'job_codes_update_job_code',
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
                        (UpdateJobCodeRequest,),
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
            callable=__job_codes_update_job_code
        )
