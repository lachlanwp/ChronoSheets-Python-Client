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


class UsersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def users_create_timesheet_user(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Create a user in your organisation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_create_timesheet_user(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSInsertUserRequest request:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseInsertUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.users_create_timesheet_user_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.users_create_timesheet_user_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def users_create_timesheet_user_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Create a user in your organisation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_create_timesheet_user_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSInsertUserRequest request:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseInsertUserResponse
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
                    " to method users_create_timesheet_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `users_create_timesheet_user`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `users_create_timesheet_user`")  # noqa: E501

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
            '/api/Users/CreateTimesheetUser', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseInsertUserResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_get_timesheet_user(self, user_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a particular user in your organisation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_get_timesheet_user(user_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int user_id: (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseUserForManagement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.users_get_timesheet_user_with_http_info(user_id, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.users_get_timesheet_user_with_http_info(user_id, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def users_get_timesheet_user_with_http_info(self, user_id, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get a particular user in your organisation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_get_timesheet_user_with_http_info(user_id, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param int user_id: (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseUserForManagement
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'x_chronosheets_auth']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method users_get_timesheet_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `users_get_timesheet_user`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `users_get_timesheet_user`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('UserId', params['user_id']))  # noqa: E501

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
            '/api/Users/GetTimesheetUser', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseUserForManagement',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_get_timesheet_users(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get users for your organisation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_get_timesheet_users(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListUserForManagement
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.users_get_timesheet_users_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.users_get_timesheet_users_with_http_info(x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def users_get_timesheet_users_with_http_info(self, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Get users for your organisation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_get_timesheet_users_with_http_info(x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseListUserForManagement
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
                    " to method users_get_timesheet_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `users_get_timesheet_users`")  # noqa: E501

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
            '/api/Users/GetTimesheetUsers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseListUserForManagement',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def users_update_timesheet_user(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_update_timesheet_user(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSUpdateUserRequest request:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseUpdateUserResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.users_update_timesheet_user_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
        else:
            (data) = self.users_update_timesheet_user_with_http_info(request, x_chronosheets_auth, **kwargs)  # noqa: E501
            return data

    def users_update_timesheet_user_with_http_info(self, request, x_chronosheets_auth, **kwargs):  # noqa: E501
        """Update a user  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.users_update_timesheet_user_with_http_info(request, x_chronosheets_auth, async=True)
        >>> result = thread.get()

        :param async bool
        :param CSUpdateUserRequest request:  (required)
        :param str x_chronosheets_auth: The ChronoSheets Auth Token (required)
        :return: CSApiResponseUpdateUserResponse
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
                    " to method users_update_timesheet_user" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `users_update_timesheet_user`")  # noqa: E501
        # verify the required parameter 'x_chronosheets_auth' is set
        if ('x_chronosheets_auth' not in params or
                params['x_chronosheets_auth'] is None):
            raise ValueError("Missing the required parameter `x_chronosheets_auth` when calling `users_update_timesheet_user`")  # noqa: E501

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
            '/api/Users/UpdateTimesheetUser', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CSApiResponseUpdateUserResponse',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
