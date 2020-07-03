# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from ChronoSheetsAPI.configuration import Configuration


class Trip(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'trip_id': 'int',
        'timesheet_id': 'int',
        'vehicle_id': 'int',
        'user_id': 'int',
        'org_id': 'int',
        'mobile_platform': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'vehicle_name': 'str',
        'vehicle_make': 'str',
        'vehicle_model': 'str',
        'vehicle_year': 'str',
        'cost_per_kilometer': 'float',
        'trip_total_cost': 'float',
        'total_trip_distance_meters': 'float',
        'start_address': 'str',
        'end_address': 'str',
        'path_coordinates': 'list[TripCoordinate]',
        'cache_expiry_date': 'datetime'
    }

    attribute_map = {
        'trip_id': 'TripId',
        'timesheet_id': 'TimesheetId',
        'vehicle_id': 'VehicleId',
        'user_id': 'UserId',
        'org_id': 'OrgId',
        'mobile_platform': 'MobilePlatform',
        'start_date': 'StartDate',
        'end_date': 'EndDate',
        'vehicle_name': 'VehicleName',
        'vehicle_make': 'VehicleMake',
        'vehicle_model': 'VehicleModel',
        'vehicle_year': 'VehicleYear',
        'cost_per_kilometer': 'CostPerKilometer',
        'trip_total_cost': 'TripTotalCost',
        'total_trip_distance_meters': 'TotalTripDistanceMeters',
        'start_address': 'StartAddress',
        'end_address': 'EndAddress',
        'path_coordinates': 'PathCoordinates',
        'cache_expiry_date': 'CacheExpiryDate'
    }

    def __init__(self, trip_id=None, timesheet_id=None, vehicle_id=None, user_id=None, org_id=None, mobile_platform=None, start_date=None, end_date=None, vehicle_name=None, vehicle_make=None, vehicle_model=None, vehicle_year=None, cost_per_kilometer=None, trip_total_cost=None, total_trip_distance_meters=None, start_address=None, end_address=None, path_coordinates=None, cache_expiry_date=None, local_vars_configuration=None):  # noqa: E501
        """Trip - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._trip_id = None
        self._timesheet_id = None
        self._vehicle_id = None
        self._user_id = None
        self._org_id = None
        self._mobile_platform = None
        self._start_date = None
        self._end_date = None
        self._vehicle_name = None
        self._vehicle_make = None
        self._vehicle_model = None
        self._vehicle_year = None
        self._cost_per_kilometer = None
        self._trip_total_cost = None
        self._total_trip_distance_meters = None
        self._start_address = None
        self._end_address = None
        self._path_coordinates = None
        self._cache_expiry_date = None
        self.discriminator = None

        if trip_id is not None:
            self.trip_id = trip_id
        if timesheet_id is not None:
            self.timesheet_id = timesheet_id
        if vehicle_id is not None:
            self.vehicle_id = vehicle_id
        if user_id is not None:
            self.user_id = user_id
        if org_id is not None:
            self.org_id = org_id
        if mobile_platform is not None:
            self.mobile_platform = mobile_platform
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if vehicle_name is not None:
            self.vehicle_name = vehicle_name
        if vehicle_make is not None:
            self.vehicle_make = vehicle_make
        if vehicle_model is not None:
            self.vehicle_model = vehicle_model
        if vehicle_year is not None:
            self.vehicle_year = vehicle_year
        if cost_per_kilometer is not None:
            self.cost_per_kilometer = cost_per_kilometer
        if trip_total_cost is not None:
            self.trip_total_cost = trip_total_cost
        if total_trip_distance_meters is not None:
            self.total_trip_distance_meters = total_trip_distance_meters
        if start_address is not None:
            self.start_address = start_address
        if end_address is not None:
            self.end_address = end_address
        if path_coordinates is not None:
            self.path_coordinates = path_coordinates
        if cache_expiry_date is not None:
            self.cache_expiry_date = cache_expiry_date

    @property
    def trip_id(self):
        """Gets the trip_id of this Trip.  # noqa: E501


        :return: The trip_id of this Trip.  # noqa: E501
        :rtype: int
        """
        return self._trip_id

    @trip_id.setter
    def trip_id(self, trip_id):
        """Sets the trip_id of this Trip.


        :param trip_id: The trip_id of this Trip.  # noqa: E501
        :type: int
        """

        self._trip_id = trip_id

    @property
    def timesheet_id(self):
        """Gets the timesheet_id of this Trip.  # noqa: E501


        :return: The timesheet_id of this Trip.  # noqa: E501
        :rtype: int
        """
        return self._timesheet_id

    @timesheet_id.setter
    def timesheet_id(self, timesheet_id):
        """Sets the timesheet_id of this Trip.


        :param timesheet_id: The timesheet_id of this Trip.  # noqa: E501
        :type: int
        """

        self._timesheet_id = timesheet_id

    @property
    def vehicle_id(self):
        """Gets the vehicle_id of this Trip.  # noqa: E501


        :return: The vehicle_id of this Trip.  # noqa: E501
        :rtype: int
        """
        return self._vehicle_id

    @vehicle_id.setter
    def vehicle_id(self, vehicle_id):
        """Sets the vehicle_id of this Trip.


        :param vehicle_id: The vehicle_id of this Trip.  # noqa: E501
        :type: int
        """

        self._vehicle_id = vehicle_id

    @property
    def user_id(self):
        """Gets the user_id of this Trip.  # noqa: E501


        :return: The user_id of this Trip.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Trip.


        :param user_id: The user_id of this Trip.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def org_id(self):
        """Gets the org_id of this Trip.  # noqa: E501


        :return: The org_id of this Trip.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this Trip.


        :param org_id: The org_id of this Trip.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def mobile_platform(self):
        """Gets the mobile_platform of this Trip.  # noqa: E501


        :return: The mobile_platform of this Trip.  # noqa: E501
        :rtype: str
        """
        return self._mobile_platform

    @mobile_platform.setter
    def mobile_platform(self, mobile_platform):
        """Sets the mobile_platform of this Trip.


        :param mobile_platform: The mobile_platform of this Trip.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "iOS", "Android"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and mobile_platform not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `mobile_platform` ({0}), must be one of {1}"  # noqa: E501
                .format(mobile_platform, allowed_values)
            )

        self._mobile_platform = mobile_platform

    @property
    def start_date(self):
        """Gets the start_date of this Trip.  # noqa: E501


        :return: The start_date of this Trip.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this Trip.


        :param start_date: The start_date of this Trip.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this Trip.  # noqa: E501


        :return: The end_date of this Trip.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this Trip.


        :param end_date: The end_date of this Trip.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def vehicle_name(self):
        """Gets the vehicle_name of this Trip.  # noqa: E501


        :return: The vehicle_name of this Trip.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_name

    @vehicle_name.setter
    def vehicle_name(self, vehicle_name):
        """Sets the vehicle_name of this Trip.


        :param vehicle_name: The vehicle_name of this Trip.  # noqa: E501
        :type: str
        """

        self._vehicle_name = vehicle_name

    @property
    def vehicle_make(self):
        """Gets the vehicle_make of this Trip.  # noqa: E501


        :return: The vehicle_make of this Trip.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_make

    @vehicle_make.setter
    def vehicle_make(self, vehicle_make):
        """Sets the vehicle_make of this Trip.


        :param vehicle_make: The vehicle_make of this Trip.  # noqa: E501
        :type: str
        """

        self._vehicle_make = vehicle_make

    @property
    def vehicle_model(self):
        """Gets the vehicle_model of this Trip.  # noqa: E501


        :return: The vehicle_model of this Trip.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_model

    @vehicle_model.setter
    def vehicle_model(self, vehicle_model):
        """Sets the vehicle_model of this Trip.


        :param vehicle_model: The vehicle_model of this Trip.  # noqa: E501
        :type: str
        """

        self._vehicle_model = vehicle_model

    @property
    def vehicle_year(self):
        """Gets the vehicle_year of this Trip.  # noqa: E501


        :return: The vehicle_year of this Trip.  # noqa: E501
        :rtype: str
        """
        return self._vehicle_year

    @vehicle_year.setter
    def vehicle_year(self, vehicle_year):
        """Sets the vehicle_year of this Trip.


        :param vehicle_year: The vehicle_year of this Trip.  # noqa: E501
        :type: str
        """

        self._vehicle_year = vehicle_year

    @property
    def cost_per_kilometer(self):
        """Gets the cost_per_kilometer of this Trip.  # noqa: E501


        :return: The cost_per_kilometer of this Trip.  # noqa: E501
        :rtype: float
        """
        return self._cost_per_kilometer

    @cost_per_kilometer.setter
    def cost_per_kilometer(self, cost_per_kilometer):
        """Sets the cost_per_kilometer of this Trip.


        :param cost_per_kilometer: The cost_per_kilometer of this Trip.  # noqa: E501
        :type: float
        """

        self._cost_per_kilometer = cost_per_kilometer

    @property
    def trip_total_cost(self):
        """Gets the trip_total_cost of this Trip.  # noqa: E501


        :return: The trip_total_cost of this Trip.  # noqa: E501
        :rtype: float
        """
        return self._trip_total_cost

    @trip_total_cost.setter
    def trip_total_cost(self, trip_total_cost):
        """Sets the trip_total_cost of this Trip.


        :param trip_total_cost: The trip_total_cost of this Trip.  # noqa: E501
        :type: float
        """

        self._trip_total_cost = trip_total_cost

    @property
    def total_trip_distance_meters(self):
        """Gets the total_trip_distance_meters of this Trip.  # noqa: E501


        :return: The total_trip_distance_meters of this Trip.  # noqa: E501
        :rtype: float
        """
        return self._total_trip_distance_meters

    @total_trip_distance_meters.setter
    def total_trip_distance_meters(self, total_trip_distance_meters):
        """Sets the total_trip_distance_meters of this Trip.


        :param total_trip_distance_meters: The total_trip_distance_meters of this Trip.  # noqa: E501
        :type: float
        """

        self._total_trip_distance_meters = total_trip_distance_meters

    @property
    def start_address(self):
        """Gets the start_address of this Trip.  # noqa: E501


        :return: The start_address of this Trip.  # noqa: E501
        :rtype: str
        """
        return self._start_address

    @start_address.setter
    def start_address(self, start_address):
        """Sets the start_address of this Trip.


        :param start_address: The start_address of this Trip.  # noqa: E501
        :type: str
        """

        self._start_address = start_address

    @property
    def end_address(self):
        """Gets the end_address of this Trip.  # noqa: E501


        :return: The end_address of this Trip.  # noqa: E501
        :rtype: str
        """
        return self._end_address

    @end_address.setter
    def end_address(self, end_address):
        """Sets the end_address of this Trip.


        :param end_address: The end_address of this Trip.  # noqa: E501
        :type: str
        """

        self._end_address = end_address

    @property
    def path_coordinates(self):
        """Gets the path_coordinates of this Trip.  # noqa: E501


        :return: The path_coordinates of this Trip.  # noqa: E501
        :rtype: list[TripCoordinate]
        """
        return self._path_coordinates

    @path_coordinates.setter
    def path_coordinates(self, path_coordinates):
        """Sets the path_coordinates of this Trip.


        :param path_coordinates: The path_coordinates of this Trip.  # noqa: E501
        :type: list[TripCoordinate]
        """

        self._path_coordinates = path_coordinates

    @property
    def cache_expiry_date(self):
        """Gets the cache_expiry_date of this Trip.  # noqa: E501


        :return: The cache_expiry_date of this Trip.  # noqa: E501
        :rtype: datetime
        """
        return self._cache_expiry_date

    @cache_expiry_date.setter
    def cache_expiry_date(self, cache_expiry_date):
        """Sets the cache_expiry_date of this Trip.


        :param cache_expiry_date: The cache_expiry_date of this Trip.  # noqa: E501
        :type: datetime
        """

        self._cache_expiry_date = cache_expiry_date

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if not isinstance(other, Trip):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Trip):
            return True

        return self.to_dict() != other.to_dict()