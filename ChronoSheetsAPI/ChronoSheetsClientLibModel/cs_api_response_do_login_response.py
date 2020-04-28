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


class CSApiResponseDoLoginResponse(object):
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
        'data': 'CSDoLoginResponse',
        'status': 'str',
        'message': 'str'
    }

    attribute_map = {
        'data': 'Data',
        'status': 'Status',
        'message': 'Message'
    }

    def __init__(self, data=None, status=None, message=None):  # noqa: E501
        """CSApiResponseDoLoginResponse - a model defined in Swagger"""  # noqa: E501

        self._data = None
        self._status = None
        self._message = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if status is not None:
            self.status = status
        if message is not None:
            self.message = message

    @property
    def data(self):
        """Gets the data of this CSApiResponseDoLoginResponse.  # noqa: E501


        :return: The data of this CSApiResponseDoLoginResponse.  # noqa: E501
        :rtype: CSDoLoginResponse
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CSApiResponseDoLoginResponse.


        :param data: The data of this CSApiResponseDoLoginResponse.  # noqa: E501
        :type: CSDoLoginResponse
        """

        self._data = data

    @property
    def status(self):
        """Gets the status of this CSApiResponseDoLoginResponse.  # noqa: E501


        :return: The status of this CSApiResponseDoLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CSApiResponseDoLoginResponse.


        :param status: The status of this CSApiResponseDoLoginResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Succeeded", "FatalException", "GeneralError", "ValidationError", "UnAuthorized", "SessionExpired"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def message(self):
        """Gets the message of this CSApiResponseDoLoginResponse.  # noqa: E501


        :return: The message of this CSApiResponseDoLoginResponse.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CSApiResponseDoLoginResponse.


        :param message: The message of this CSApiResponseDoLoginResponse.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(CSApiResponseDoLoginResponse, dict):
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
        if not isinstance(other, CSApiResponseDoLoginResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
