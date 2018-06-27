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


class CSInsertVehicleRequest(object):
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
        'name': 'str',
        'cost_per_kilometer': 'float',
        'make': 'str',
        'model': 'str',
        'year': 'str',
        'licence_plate_number': 'str',
        'linked_org_group_ids': 'list[int]'
    }

    attribute_map = {
        'name': 'Name',
        'cost_per_kilometer': 'CostPerKilometer',
        'make': 'Make',
        'model': 'Model',
        'year': 'Year',
        'licence_plate_number': 'LicencePlateNumber',
        'linked_org_group_ids': 'LinkedOrgGroupIds'
    }

    def __init__(self, name=None, cost_per_kilometer=None, make=None, model=None, year=None, licence_plate_number=None, linked_org_group_ids=None):  # noqa: E501
        """CSInsertVehicleRequest - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._cost_per_kilometer = None
        self._make = None
        self._model = None
        self._year = None
        self._licence_plate_number = None
        self._linked_org_group_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cost_per_kilometer is not None:
            self.cost_per_kilometer = cost_per_kilometer
        if make is not None:
            self.make = make
        if model is not None:
            self.model = model
        if year is not None:
            self.year = year
        if licence_plate_number is not None:
            self.licence_plate_number = licence_plate_number
        if linked_org_group_ids is not None:
            self.linked_org_group_ids = linked_org_group_ids

    @property
    def name(self):
        """Gets the name of this CSInsertVehicleRequest.  # noqa: E501


        :return: The name of this CSInsertVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CSInsertVehicleRequest.


        :param name: The name of this CSInsertVehicleRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def cost_per_kilometer(self):
        """Gets the cost_per_kilometer of this CSInsertVehicleRequest.  # noqa: E501


        :return: The cost_per_kilometer of this CSInsertVehicleRequest.  # noqa: E501
        :rtype: float
        """
        return self._cost_per_kilometer

    @cost_per_kilometer.setter
    def cost_per_kilometer(self, cost_per_kilometer):
        """Sets the cost_per_kilometer of this CSInsertVehicleRequest.


        :param cost_per_kilometer: The cost_per_kilometer of this CSInsertVehicleRequest.  # noqa: E501
        :type: float
        """

        self._cost_per_kilometer = cost_per_kilometer

    @property
    def make(self):
        """Gets the make of this CSInsertVehicleRequest.  # noqa: E501


        :return: The make of this CSInsertVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._make

    @make.setter
    def make(self, make):
        """Sets the make of this CSInsertVehicleRequest.


        :param make: The make of this CSInsertVehicleRequest.  # noqa: E501
        :type: str
        """

        self._make = make

    @property
    def model(self):
        """Gets the model of this CSInsertVehicleRequest.  # noqa: E501


        :return: The model of this CSInsertVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this CSInsertVehicleRequest.


        :param model: The model of this CSInsertVehicleRequest.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def year(self):
        """Gets the year of this CSInsertVehicleRequest.  # noqa: E501


        :return: The year of this CSInsertVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._year

    @year.setter
    def year(self, year):
        """Sets the year of this CSInsertVehicleRequest.


        :param year: The year of this CSInsertVehicleRequest.  # noqa: E501
        :type: str
        """

        self._year = year

    @property
    def licence_plate_number(self):
        """Gets the licence_plate_number of this CSInsertVehicleRequest.  # noqa: E501


        :return: The licence_plate_number of this CSInsertVehicleRequest.  # noqa: E501
        :rtype: str
        """
        return self._licence_plate_number

    @licence_plate_number.setter
    def licence_plate_number(self, licence_plate_number):
        """Sets the licence_plate_number of this CSInsertVehicleRequest.


        :param licence_plate_number: The licence_plate_number of this CSInsertVehicleRequest.  # noqa: E501
        :type: str
        """

        self._licence_plate_number = licence_plate_number

    @property
    def linked_org_group_ids(self):
        """Gets the linked_org_group_ids of this CSInsertVehicleRequest.  # noqa: E501


        :return: The linked_org_group_ids of this CSInsertVehicleRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._linked_org_group_ids

    @linked_org_group_ids.setter
    def linked_org_group_ids(self, linked_org_group_ids):
        """Sets the linked_org_group_ids of this CSInsertVehicleRequest.


        :param linked_org_group_ids: The linked_org_group_ids of this CSInsertVehicleRequest.  # noqa: E501
        :type: list[int]
        """

        self._linked_org_group_ids = linked_org_group_ids

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
        if not isinstance(other, CSInsertVehicleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
