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
from ChronoSheetsAPI.model.api_response_for_paginated_list_org_report_transcript import ApiResponseForPaginatedListOrgReportTranscript
from ChronoSheetsAPI.model.api_response_transcription import ApiResponseTranscription


class TranscriptsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __transcripts_get_my_transcript(
            self,
            file_attachment_id,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get an audio to text transcript for a particular audio file attachment  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.transcripts_get_my_transcript(file_attachment_id, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                file_attachment_id (int): The ID of the file attachment that has a transcript.  It should be an audio file attachment.
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
                ApiResponseTranscription
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
            kwargs['file_attachment_id'] = \
                file_attachment_id
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.transcripts_get_my_transcript = Endpoint(
            settings={
                'response_type': (ApiResponseTranscription,),
                'auth': [],
                'endpoint_path': '/Transcripts/GetMyTranscript',
                'operation_id': 'transcripts_get_my_transcript',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_attachment_id',
                    'x_chronosheets_auth',
                ],
                'required': [
                    'file_attachment_id',
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
                    'file_attachment_id':
                        (int,),
                    'x_chronosheets_auth':
                        (str,),
                },
                'attribute_map': {
                    'file_attachment_id': 'FileAttachmentId',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'file_attachment_id': 'query',
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
            callable=__transcripts_get_my_transcript
        )

        def __transcripts_get_my_transcripts(
            self,
            start_date,
            end_date,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get my file transcripts.  Get audio to text transcripts that you've created.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.transcripts_get_my_transcripts(start_date, end_date, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                start_date (datetime): The Start date of the date range.  Transcripts after this date will be obtained.
                end_date (datetime): The End date of the date range.  Transcripts before this date will be obtained.
                x_chronosheets_auth (str): The ChronoSheets Auth Token

            Keyword Args:
                skip (int): Skip this many transcripts. [optional]
                take (int): Take this many transcripts. [optional]
                keyword (str): Search the text content of the transcript keywords. [optional]
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
                ApiResponseForPaginatedListOrgReportTranscript
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
            kwargs['start_date'] = \
                start_date
            kwargs['end_date'] = \
                end_date
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.transcripts_get_my_transcripts = Endpoint(
            settings={
                'response_type': (ApiResponseForPaginatedListOrgReportTranscript,),
                'auth': [],
                'endpoint_path': '/Transcripts/GetMyTranscripts',
                'operation_id': 'transcripts_get_my_transcripts',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'start_date',
                    'end_date',
                    'x_chronosheets_auth',
                    'skip',
                    'take',
                    'keyword',
                ],
                'required': [
                    'start_date',
                    'end_date',
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
                    'start_date':
                        (datetime,),
                    'end_date':
                        (datetime,),
                    'x_chronosheets_auth':
                        (str,),
                    'skip':
                        (int,),
                    'take':
                        (int,),
                    'keyword':
                        (str,),
                },
                'attribute_map': {
                    'start_date': 'StartDate',
                    'end_date': 'EndDate',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                    'skip': 'Skip',
                    'take': 'Take',
                    'keyword': 'Keyword',
                },
                'location_map': {
                    'start_date': 'query',
                    'end_date': 'query',
                    'x_chronosheets_auth': 'header',
                    'skip': 'query',
                    'take': 'query',
                    'keyword': 'query',
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
            callable=__transcripts_get_my_transcripts
        )
