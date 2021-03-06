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
from ChronoSheetsAPI.model.api_response_list_timesheet_task import ApiResponseListTimesheetTask
from ChronoSheetsAPI.model.api_response_timesheet_task import ApiResponseTimesheetTask
from ChronoSheetsAPI.model.insert_task_request import InsertTaskRequest
from ChronoSheetsAPI.model.update_task_request import UpdateTaskRequest


class TasksApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __tasks_create_task(
            self,
            x_chronosheets_auth,
            request,
            **kwargs
        ):
            """Create a task.    Requires the 'ManageJobsAndTask' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tasks_create_task(x_chronosheets_auth, request, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token
                request (InsertTaskRequest): An Insert Task Request object containing values for the new Task to create

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

        self.tasks_create_task = Endpoint(
            settings={
                'response_type': (ApiResponseInt32,),
                'auth': [],
                'endpoint_path': '/Tasks/CreateTask',
                'operation_id': 'tasks_create_task',
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
                        (InsertTaskRequest,),
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
            callable=__tasks_create_task
        )

        def __tasks_delete_task(
            self,
            task_id,
            x_chronosheets_auth,
            **kwargs
        ):
            """Delete a task.    Requires the 'ManageJobsAndTask' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tasks_delete_task(task_id, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                task_id (int): The ID of the Task you want to delete
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
            kwargs['task_id'] = \
                task_id
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.tasks_delete_task = Endpoint(
            settings={
                'response_type': (ApiResponseBoolean,),
                'auth': [],
                'endpoint_path': '/Tasks/DeleteTask',
                'operation_id': 'tasks_delete_task',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_id',
                    'x_chronosheets_auth',
                ],
                'required': [
                    'task_id',
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
                    'task_id':
                        (int,),
                    'x_chronosheets_auth':
                        (str,),
                },
                'attribute_map': {
                    'task_id': 'TaskId',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'task_id': 'query',
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
            callable=__tasks_delete_task
        )

        def __tasks_get_task_by_id(
            self,
            task_id,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get a particular task by Id.   Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tasks_get_task_by_id(task_id, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                task_id (int): The ID of the TimesheetTask you want to get
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
                ApiResponseTimesheetTask
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
            kwargs['task_id'] = \
                task_id
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.tasks_get_task_by_id = Endpoint(
            settings={
                'response_type': (ApiResponseTimesheetTask,),
                'auth': [],
                'endpoint_path': '/Tasks/GetTaskById',
                'operation_id': 'tasks_get_task_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_id',
                    'x_chronosheets_auth',
                ],
                'required': [
                    'task_id',
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
                    'task_id':
                        (int,),
                    'x_chronosheets_auth':
                        (str,),
                },
                'attribute_map': {
                    'task_id': 'TaskId',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'task_id': 'query',
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
            callable=__tasks_get_task_by_id
        )

        def __tasks_get_tasks(
            self,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get tasks in your organisation.   Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tasks_get_tasks(x_chronosheets_auth, async_req=True)
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
                ApiResponseListTimesheetTask
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

        self.tasks_get_tasks = Endpoint(
            settings={
                'response_type': (ApiResponseListTimesheetTask,),
                'auth': [],
                'endpoint_path': '/Tasks/GetTasks',
                'operation_id': 'tasks_get_tasks',
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
            callable=__tasks_get_tasks
        )

        def __tasks_get_tasks_for_job(
            self,
            job_id,
            x_chronosheets_auth,
            **kwargs
        ):
            """Get a collection of tasks for a particular Job, specified by JobId.    Requires the 'SubmitTimesheets' or 'ManageJobsAndTask' permissions.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tasks_get_tasks_for_job(job_id, x_chronosheets_auth, async_req=True)
            >>> result = thread.get()

            Args:
                job_id (int): The ID of the job
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
                ApiResponseListTimesheetTask
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
            kwargs['job_id'] = \
                job_id
            kwargs['x_chronosheets_auth'] = \
                x_chronosheets_auth
            return self.call_with_http_info(**kwargs)

        self.tasks_get_tasks_for_job = Endpoint(
            settings={
                'response_type': (ApiResponseListTimesheetTask,),
                'auth': [],
                'endpoint_path': '/Tasks/GetTasksForJob',
                'operation_id': 'tasks_get_tasks_for_job',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'job_id',
                    'x_chronosheets_auth',
                ],
                'required': [
                    'job_id',
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
                    'job_id':
                        (int,),
                    'x_chronosheets_auth':
                        (str,),
                },
                'attribute_map': {
                    'job_id': 'JobId',
                    'x_chronosheets_auth': 'x-chronosheets-auth',
                },
                'location_map': {
                    'job_id': 'query',
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
            callable=__tasks_get_tasks_for_job
        )

        def __tasks_update_task(
            self,
            x_chronosheets_auth,
            request,
            **kwargs
        ):
            """Update a task.    Requires the 'ManageJobsAndTask' permission.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.tasks_update_task(x_chronosheets_auth, request, async_req=True)
            >>> result = thread.get()

            Args:
                x_chronosheets_auth (str): The ChronoSheets Auth Token
                request (UpdateTaskRequest): An Update Task Request object containing updated fields.  Make sure to specify the Task Id in the request object so that ChronoSheets knows which Task to update

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

        self.tasks_update_task = Endpoint(
            settings={
                'response_type': (ApiResponseBoolean,),
                'auth': [],
                'endpoint_path': '/Tasks/UpdateTask',
                'operation_id': 'tasks_update_task',
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
                        (UpdateTaskRequest,),
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
            callable=__tasks_update_task
        )
