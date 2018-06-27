# coding: utf-8

"""
    ChronoSheets API

    ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  # noqa: E501

    OpenAPI spec version: v1
    Contact: lachlan@chronosheets.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ChronoSheetsAPI.api_client import ApiClient


class TasksApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def tasks_create_task(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Create a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_create_task(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSInsertTaskRequest request:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseInt32
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tasks_create_task_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_create_task_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def tasks_create_task_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Create a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_create_task_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSInsertTaskRequest request:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseInt32
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_create_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `tasks_create_task`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `tasks_create_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Tasks/CreateTask', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseInt32',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_delete_task(self, task_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Delete a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_delete_task(task_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int task_id:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tasks_delete_task_with_http_info(task_id, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_delete_task_with_http_info(task_id, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def tasks_delete_task_with_http_info(self, task_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Delete a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_delete_task_with_http_info(task_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int task_id:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_delete_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `tasks_delete_task`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `tasks_delete_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in params:
            query_params.append(('TaskId', params['task_id']))  # noqa: E501

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Tasks/DeleteTask', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_get_task_by_id(self, task_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a particular task by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_get_task_by_id(task_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int task_id: (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseTimesheetTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tasks_get_task_by_id_with_http_info(task_id, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_get_task_by_id_with_http_info(task_id, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def tasks_get_task_by_id_with_http_info(self, task_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a particular task by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_get_task_by_id_with_http_info(task_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int task_id: (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseTimesheetTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['task_id', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_get_task_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'task_id' is set
        if ('task_id' not in params or
                params['task_id'] is None):
            raise ValueError("Missing the required parameter `task_id` when calling `tasks_get_task_by_id`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `tasks_get_task_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'task_id' in params:
            query_params.append(('TaskId', params['task_id']))  # noqa: E501

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Tasks/GetTaskById', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseTimesheetTask',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_get_tasks(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get tasks in your organisation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_get_tasks(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListTimesheetTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tasks_get_tasks_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_get_tasks_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def tasks_get_tasks_with_http_info(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get tasks in your organisation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_get_tasks_with_http_info(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListTimesheetTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_get_tasks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `tasks_get_tasks`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Tasks/GetTasks', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseListTimesheetTask',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_get_tasks_for_job(self, job_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get tasks for a particular job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_get_tasks_for_job(job_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int job_id: The ID of the job (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListTimesheetTask
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tasks_get_tasks_for_job_with_http_info(job_id, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_get_tasks_for_job_with_http_info(job_id, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def tasks_get_tasks_for_job_with_http_info(self, job_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get tasks for a particular job  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_get_tasks_for_job_with_http_info(job_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int job_id: The ID of the job (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListTimesheetTask
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['job_id', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_get_tasks_for_job" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'job_id' is set
        if ('job_id' not in params or
                params['job_id'] is None):
            raise ValueError("Missing the required parameter `job_id` when calling `tasks_get_tasks_for_job`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `tasks_get_tasks_for_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'job_id' in params:
            query_params.append(('JobId', params['job_id']))  # noqa: E501

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Tasks/GetTasksForJob', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseListTimesheetTask',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def tasks_update_task(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_update_task(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSUpdateTaskRequest request:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.tasks_update_task_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.tasks_update_task_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def tasks_update_task_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update a task  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.tasks_update_task_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSUpdateTaskRequest request:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseBoolean
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tasks_update_task" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `tasks_update_task`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `tasks_update_task`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_chronosheets_auth' in params:
            header_params['x-chronosheets-auth'] = params['x_chronosheets_auth']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'multipart/form-data'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded', 'multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Tasks/UpdateTask', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseBoolean',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
