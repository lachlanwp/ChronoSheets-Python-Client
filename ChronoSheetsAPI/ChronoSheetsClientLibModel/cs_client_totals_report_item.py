# coding: utf-8

"""
    ChronoSheets API

    ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  # noqa: E501

    OpenAPI spec version: v1
    Contact: lachlan@chronosheets.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CSClientTotalsReportItem(object):
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
        'client_id': 'int',
        'client_name': 'str',
        'span_seconds': 'int'
    }

    attribute_map = {
        'organisation_id': 'OrganisationId',
        'user_id': 'UserId',
        'client_id': 'ClientId',
        'client_name': 'ClientName',
        'span_seconds': 'SpanSeconds'
    }

    def __init__(self, organisation_id=None, user_id=None, client_id=None, client_name=None, span_seconds=None):  # noqa: E501
        """CSClientTotalsReportItem - a model defined in Swagger"""  # noqa: E501

        self._organisation_id = None
        self._user_id = None
        self._client_id = None
        self._client_name = None
        self._span_seconds = None
        self.discriminator = None

        if organisation_id is not None:
            self.organisation_id = organisation_id
        if user_id is not None:
            self.user_id = user_id
        if client_id is not None:
            self.client_id = client_id
        if client_name is not None:
            self.client_name = client_name
        if span_seconds is not None:
            self.span_seconds = span_seconds

    @property
    def organisation_id(self):
        """Gets the organisation_id of this CSClientTotalsReportItem.  # noqa: E501


        :return: The organisation_id of this CSClientTotalsReportItem.  # noqa: E501
        :rtype: int
        """
        return self._organisation_id

    @organisation_id.setter
    def organisation_id(self, organisation_id):
        """Sets the organisation_id of this CSClientTotalsReportItem.


        :param organisation_id: The organisation_id of this CSClientTotalsReportItem.  # noqa: E501
        :type: int
        """

        self._organisation_id = organisation_id

    @property
    def user_id(self):
        """Gets the user_id of this CSClientTotalsReportItem.  # noqa: E501


        :return: The user_id of this CSClientTotalsReportItem.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSClientTotalsReportItem.


        :param user_id: The user_id of this CSClientTotalsReportItem.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def client_id(self):
        """Gets the client_id of this CSClientTotalsReportItem.  # noqa: E501


        :return: The client_id of this CSClientTotalsReportItem.  # noqa: E501
        :rtype: int
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this CSClientTotalsReportItem.


        :param client_id: The client_id of this CSClientTotalsReportItem.  # noqa: E501
        :type: int
        """

        self._client_id = client_id

    @property
    def client_name(self):
        """Gets the client_name of this CSClientTotalsReportItem.  # noqa: E501


        :return: The client_name of this CSClientTotalsReportItem.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this CSClientTotalsReportItem.


        :param client_name: The client_name of this CSClientTotalsReportItem.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def span_seconds(self):
        """Gets the span_seconds of this CSClientTotalsReportItem.  # noqa: E501


        :return: The span_seconds of this CSClientTotalsReportItem.  # noqa: E501
        :rtype: int
        """
        return self._span_seconds

    @span_seconds.setter
    def span_seconds(self, span_seconds):
        """Sets the span_seconds of this CSClientTotalsReportItem.


        :param span_seconds: The span_seconds of this CSClientTotalsReportItem.  # noqa: E501
        :type: int
        """

        self._span_seconds = span_seconds

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CSClientTotalsReportItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
