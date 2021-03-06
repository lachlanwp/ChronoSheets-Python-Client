# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CSRawReportItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'organisation_id': 'int',
        'user_id': 'int',
        'username': 'str',
        'email_address': 'str',
        'job_code': 'str',
        'task_name': 'str',
        'client_name': 'str',
        'project_name': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'span_seconds': 'int',
        'description': 'str',
        'pay_amount': 'float',
        'pay_overtime_amount': 'float',
        'trip_cost': 'float',
        'trip_distance_meters': 'float',
        'span_seconds_normal_time': 'int',
        'span_seconds_overtime': 'int'
    }

    attribute_map = {
        'organisation_id': 'OrganisationId',
        'user_id': 'UserId',
        'username': 'Username',
        'email_address': 'EmailAddress',
        'job_code': 'JobCode',
        'task_name': 'TaskName',
        'client_name': 'ClientName',
        'project_name': 'ProjectName',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'span_seconds': 'SpanSeconds',
        'description': 'Description',
        'pay_amount': 'PayAmount',
        'pay_overtime_amount': 'PayOvertimeAmount',
        'trip_cost': 'TripCost',
        'trip_distance_meters': 'TripDistanceMeters',
        'span_seconds_normal_time': 'SpanSecondsNormalTime',
        'span_seconds_overtime': 'SpanSecondsOvertime'
    }

    def __init__(self, organisation_id=None, user_id=None, username=None, email_address=None, job_code=None, task_name=None, client_name=None, project_name=None, start_date=None, end_date=None, span_seconds=None, description=None, pay_amount=None, pay_overtime_amount=None, trip_cost=None, trip_distance_meters=None, span_seconds_normal_time=None, span_seconds_overtime=None):  # noqa: E501
        """CSRawReportItem - a model defined in Swagger"""  # noqa: E501

        self._organisation_id = None
        self._user_id = None
        self._username = None
        self._email_address = None
        self._job_code = None
        self._task_name = None
        self._client_name = None
        self._project_name = None
        self._start_date = None
        self._end_date = None
        self._span_seconds = None
        self._description = None
        self._pay_amount = None
        self._pay_overtime_amount = None
        self._trip_cost = None
        self._trip_distance_meters = None
        self._span_seconds_normal_time = None
        self._span_seconds_overtime = None
        self.discriminator = None

        if organisation_id is not None:
            self.organisation_id = organisation_id
        if user_id is not None:
            self.user_id = user_id
        if username is not None:
            self.username = username
        if email_address is not None:
            self.email_address = email_address
        if job_code is not None:
            self.job_code = job_code
        if task_name is not None:
            self.task_name = task_name
        if client_name is not None:
            self.client_name = client_name
        if project_name is not None:
            self.project_name = project_name
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if span_seconds is not None:
            self.span_seconds = span_seconds
        if description is not None:
            self.description = description
        if pay_amount is not None:
            self.pay_amount = pay_amount
        if pay_overtime_amount is not None:
            self.pay_overtime_amount = pay_overtime_amount
        if trip_cost is not None:
            self.trip_cost = trip_cost
        if trip_distance_meters is not None:
            self.trip_distance_meters = trip_distance_meters
        if span_seconds_normal_time is not None:
            self.span_seconds_normal_time = span_seconds_normal_time
        if span_seconds_overtime is not None:
            self.span_seconds_overtime = span_seconds_overtime

    @property
    def organisation_id(self):
        """Gets the organisation_id of this CSRawReportItem.  # noqa: E501


        :return: The organisation_id of this CSRawReportItem.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this CSRawReportItem.


        :param organisation_id: The organisation_id of this CSRawReportItem.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def user_id(self):
        """Gets the user_id of this CSRawReportItem.  # noqa: E501


        :return: The user_id of this CSRawReportItem.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSRawReportItem.


        :param user_id: The user_id of this CSRawReportItem.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def username(self):
        """Gets the username of this CSRawReportItem.  # noqa: E501


        :return: The username of this CSRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CSRawReportItem.


        :param username: The username of this CSRawReportItem.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email_address(self):
        """Gets the email_address of this CSRawReportItem.  # noqa: E501


        :return: The email_address of this CSRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CSRawReportItem.


        :param email_address: The email_address of this CSRawReportItem.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def job_code(self):
        """Gets the job_code of this CSRawReportItem.  # noqa: E501


        :return: The job_code of this CSRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._job_code

    @job_code.setter
    def job_code(self, job_code):
        """Sets the job_code of this CSRawReportItem.


        :param job_code: The job_code of this CSRawReportItem.  # noqa: E501
        :type: str
        """

        self._job_code = job_code

    @property
    def task_name(self):
        """Gets the task_name of this CSRawReportItem.  # noqa: E501


        :return: The task_name of this CSRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CSRawReportItem.


        :param task_name: The task_name of this CSRawReportItem.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    @property
    def client_name(self):
        """Gets the client_name of this CSRawReportItem.  # noqa: E501


        :return: The client_name of this CSRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this CSRawReportItem.


        :param client_name: The client_name of this CSRawReportItem.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def project_name(self):
        """Gets the project_name of this CSRawReportItem.  # noqa: E501


        :return: The project_name of this CSRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this CSRawReportItem.


        :param project_name: The project_name of this CSRawReportItem.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def start_date(self):
        """Gets the start_date of this CSRawReportItem.  # noqa: E501


        :return: The start_date of this CSRawReportItem.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CSRawReportItem.


        :param start_date: The start_date of this CSRawReportItem.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CSRawReportItem.  # noqa: E501


        :return: The end_date of this CSRawReportItem.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CSRawReportItem.


        :param end_date: The end_date of this CSRawReportItem.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def span_seconds(self):
        """Gets the span_seconds of this CSRawReportItem.  # noqa: E501


        :return: The span_seconds of this CSRawReportItem.  # noqa: E501
        :rtype: int
        """
        return self._span_seconds

    @span_seconds.setter
    def span_seconds(self, span_seconds):
        """Sets the span_seconds of this CSRawReportItem.


        :param span_seconds: The span_seconds of this CSRawReportItem.  # noqa: E501
        :type: int
        """

        self._span_seconds = span_seconds

    @property
    def description(self):
        """Gets the description of this CSRawReportItem.  # noqa: E501


        :return: The description of this CSRawReportItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CSRawReportItem.


        :param description: The description of this CSRawReportItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def pay_amount(self):
        """Gets the pay_amount of this CSRawReportItem.  # noqa: E501


        :return: The pay_amount of this CSRawReportItem.  # noqa: E501
        :rtype: float
        """
        return self._pay_amount

    @pay_amount.setter
    def pay_amount(self, pay_amount):
        """Sets the pay_amount of this CSRawReportItem.


        :param pay_amount: The pay_amount of this CSRawReportItem.  # noqa: E501
        :type: float
        """

        self._pay_amount = pay_amount

    @property
    def pay_overtime_amount(self):
        """Gets the pay_overtime_amount of this CSRawReportItem.  # noqa: E501


        :return: The pay_overtime_amount of this CSRawReportItem.  # noqa: E501
        :rtype: float
        """
        return self._pay_overtime_amount

    @pay_overtime_amount.setter
    def pay_overtime_amount(self, pay_overtime_amount):
        """Sets the pay_overtime_amount of this CSRawReportItem.


        :param pay_overtime_amount: The pay_overtime_amount of this CSRawReportItem.  # noqa: E501
        :type: float
        """

        self._pay_overtime_amount = pay_overtime_amount

    @property
    def trip_cost(self):
        """Gets the trip_cost of this CSRawReportItem.  # noqa: E501


        :return: The trip_cost of this CSRawReportItem.  # noqa: E501
        :rtype: float
        """
        return self._trip_cost

    @trip_cost.setter
    def trip_cost(self, trip_cost):
        """Sets the trip_cost of this CSRawReportItem.


        :param trip_cost: The trip_cost of this CSRawReportItem.  # noqa: E501
        :type: float
        """

        self._trip_cost = trip_cost

    @property
    def trip_distance_meters(self):
        """Gets the trip_distance_meters of this CSRawReportItem.  # noqa: E501


        :return: The trip_distance_meters of this CSRawReportItem.  # noqa: E501
        :rtype: float
        """
        return self._trip_distance_meters

    @trip_distance_meters.setter
    def trip_distance_meters(self, trip_distance_meters):
        """Sets the trip_distance_meters of this CSRawReportItem.


        :param trip_distance_meters: The trip_distance_meters of this CSRawReportItem.  # noqa: E501
        :type: float
        """

        self._trip_distance_meters = trip_distance_meters

    @property
    def span_seconds_normal_time(self):
        """Gets the span_seconds_normal_time of this CSRawReportItem.  # noqa: E501


        :return: The span_seconds_normal_time of this CSRawReportItem.  # noqa: E501
        :rtype: int
        """
        return self._span_seconds_normal_time

    @span_seconds_normal_time.setter
    def span_seconds_normal_time(self, span_seconds_normal_time):
        """Sets the span_seconds_normal_time of this CSRawReportItem.


        :param span_seconds_normal_time: The span_seconds_normal_time of this CSRawReportItem.  # noqa: E501
        :type: int
        """

        self._span_seconds_normal_time = span_seconds_normal_time

    @property
    def span_seconds_overtime(self):
        """Gets the span_seconds_overtime of this CSRawReportItem.  # noqa: E501


        :return: The span_seconds_overtime of this CSRawReportItem.  # noqa: E501
        :rtype: int
        """
        return self._span_seconds_overtime

    @span_seconds_overtime.setter
    def span_seconds_overtime(self, span_seconds_overtime):
        """Sets the span_seconds_overtime of this CSRawReportItem.


        :param span_seconds_overtime: The span_seconds_overtime of this CSRawReportItem.  # noqa: E501
        :type: int
        """

        self._span_seconds_overtime = span_seconds_overtime

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CSRawReportItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CSRawReportItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
