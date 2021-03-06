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


class CSUsualHoursDay(object):
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
        'day_type': 'str',
        'time_slots': 'list[CSTimeSlot]',
        'delete_usual_hours': 'list[int]'
    }

    attribute_map = {
        'day_type': 'DayType',
        'time_slots': 'TimeSlots',
        'delete_usual_hours': 'DeleteUsualHours'
    }

    def __init__(self, day_type=None, time_slots=None, delete_usual_hours=None):  # noqa: E501
        """CSUsualHoursDay - a model defined in Swagger"""  # noqa: E501

        self._day_type = None
        self._time_slots = None
        self._delete_usual_hours = None
        self.discriminator = None

        if day_type is not None:
            self.day_type = day_type
        if time_slots is not None:
            self.time_slots = time_slots
        if delete_usual_hours is not None:
            self.delete_usual_hours = delete_usual_hours

    @property
    def day_type(self):
        """Gets the day_type of this CSUsualHoursDay.  # noqa: E501

        Specify which day this collection of Roster timeslots is for (Monday-Sunday)  # noqa: E501

        :return: The day_type of this CSUsualHoursDay.  # noqa: E501
        :rtype: str
        """
        return self._day_type

    @day_type.setter
    def day_type(self, day_type):
        """Sets the day_type of this CSUsualHoursDay.

        Specify which day this collection of Roster timeslots is for (Monday-Sunday)  # noqa: E501

        :param day_type: The day_type of this CSUsualHoursDay.  # noqa: E501
        :type: str
        """
        allowed_values = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]  # noqa: E501
        if day_type not in allowed_values:
            raise ValueError(
                "Invalid value for `day_type` ({0}), must be one of {1}"  # noqa: E501
                .format(day_type, allowed_values)
            )

        self._day_type = day_type

    @property
    def time_slots(self):
        """Gets the time_slots of this CSUsualHoursDay.  # noqa: E501

        A collection of TimeSlots within this day  # noqa: E501

        :return: The time_slots of this CSUsualHoursDay.  # noqa: E501
        :rtype: list[CSTimeSlot]
        """
        return self._time_slots

    @time_slots.setter
    def time_slots(self, time_slots):
        """Sets the time_slots of this CSUsualHoursDay.

        A collection of TimeSlots within this day  # noqa: E501

        :param time_slots: The time_slots of this CSUsualHoursDay.  # noqa: E501
        :type: list[CSTimeSlot]
        """

        self._time_slots = time_slots

    @property
    def delete_usual_hours(self):
        """Gets the delete_usual_hours of this CSUsualHoursDay.  # noqa: E501

        Mark here which existing UsualHours are to be deleted  # noqa: E501

        :return: The delete_usual_hours of this CSUsualHoursDay.  # noqa: E501
        :rtype: list[int]
        """
        return self._delete_usual_hours

    @delete_usual_hours.setter
    def delete_usual_hours(self, delete_usual_hours):
        """Sets the delete_usual_hours of this CSUsualHoursDay.

        Mark here which existing UsualHours are to be deleted  # noqa: E501

        :param delete_usual_hours: The delete_usual_hours of this CSUsualHoursDay.  # noqa: E501
        :type: list[int]
        """

        self._delete_usual_hours = delete_usual_hours

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
        if issubclass(CSUsualHoursDay, dict):
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
        if not isinstance(other, CSUsualHoursDay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
