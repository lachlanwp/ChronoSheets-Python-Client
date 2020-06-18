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


class CSExtendedGeofence(object):
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
        'job_code': 'str',
        'task_name': 'str',
        'created_by': 'str',
        'updated_by': 'str',
        'alert_organisation': 'str',
        'geo_fencing_id': 'int',
        'org_id': 'int',
        'created_by_user_id': 'int',
        'last_updated_by_user_id': 'int',
        'name': 'str',
        'location_name': 'str',
        'coordinates': 'list[CSBasicCoordinate]',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'trigger_job_code_id': 'int',
        'trigger_task_id': 'int',
        'trigger_settings': 'str',
        'alert_to_org_group_id': 'int',
        'alert_settings': 'str',
        'start_time_hour': 'int',
        'start_time_minute': 'int',
        'end_time_hour': 'int',
        'end_time_minute': 'int'
    }

    attribute_map = {
        'job_code': 'JobCode',
        'task_name': 'TaskName',
        'created_by': 'CreatedBy',
        'updated_by': 'UpdatedBy',
        'alert_organisation': 'AlertOrganisation',
        'geo_fencing_id': 'GeoFencingId',
        'org_id': 'OrgId',
        'created_by_user_id': 'CreatedByUserId',
        'last_updated_by_user_id': 'LastUpdatedByUserId',
        'name': 'Name',
        'location_name': 'LocationName',
        'coordinates': 'Coordinates',
        'created_at': 'CreatedAt',
        'updated_at': 'UpdatedAt',
        'trigger_job_code_id': 'TriggerJobCodeId',
        'trigger_task_id': 'TriggerTaskId',
        'trigger_settings': 'TriggerSettings',
        'alert_to_org_group_id': 'AlertToOrgGroupId',
        'alert_settings': 'AlertSettings',
        'start_time_hour': 'StartTimeHour',
        'start_time_minute': 'StartTimeMinute',
        'end_time_hour': 'EndTimeHour',
        'end_time_minute': 'EndTimeMinute'
    }

    def __init__(self, job_code=None, task_name=None, created_by=None, updated_by=None, alert_organisation=None, geo_fencing_id=None, org_id=None, created_by_user_id=None, last_updated_by_user_id=None, name=None, location_name=None, coordinates=None, created_at=None, updated_at=None, trigger_job_code_id=None, trigger_task_id=None, trigger_settings=None, alert_to_org_group_id=None, alert_settings=None, start_time_hour=None, start_time_minute=None, end_time_hour=None, end_time_minute=None):  # noqa: E501
        """CSExtendedGeofence - a model defined in Swagger"""  # noqa: E501

        self._job_code = None
        self._task_name = None
        self._created_by = None
        self._updated_by = None
        self._alert_organisation = None
        self._geo_fencing_id = None
        self._org_id = None
        self._created_by_user_id = None
        self._last_updated_by_user_id = None
        self._name = None
        self._location_name = None
        self._coordinates = None
        self._created_at = None
        self._updated_at = None
        self._trigger_job_code_id = None
        self._trigger_task_id = None
        self._trigger_settings = None
        self._alert_to_org_group_id = None
        self._alert_settings = None
        self._start_time_hour = None
        self._start_time_minute = None
        self._end_time_hour = None
        self._end_time_minute = None
        self.discriminator = None

        if job_code is not None:
            self.job_code = job_code
        if task_name is not None:
            self.task_name = task_name
        if created_by is not None:
            self.created_by = created_by
        if updated_by is not None:
            self.updated_by = updated_by
        if alert_organisation is not None:
            self.alert_organisation = alert_organisation
        if geo_fencing_id is not None:
            self.geo_fencing_id = geo_fencing_id
        if org_id is not None:
            self.org_id = org_id
        if created_by_user_id is not None:
            self.created_by_user_id = created_by_user_id
        if last_updated_by_user_id is not None:
            self.last_updated_by_user_id = last_updated_by_user_id
        if name is not None:
            self.name = name
        if location_name is not None:
            self.location_name = location_name
        if coordinates is not None:
            self.coordinates = coordinates
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if trigger_job_code_id is not None:
            self.trigger_job_code_id = trigger_job_code_id
        if trigger_task_id is not None:
            self.trigger_task_id = trigger_task_id
        if trigger_settings is not None:
            self.trigger_settings = trigger_settings
        if alert_to_org_group_id is not None:
            self.alert_to_org_group_id = alert_to_org_group_id
        if alert_settings is not None:
            self.alert_settings = alert_settings
        if start_time_hour is not None:
            self.start_time_hour = start_time_hour
        if start_time_minute is not None:
            self.start_time_minute = start_time_minute
        if end_time_hour is not None:
            self.end_time_hour = end_time_hour
        if end_time_minute is not None:
            self.end_time_minute = end_time_minute

    @property
    def job_code(self):
        """Gets the job_code of this CSExtendedGeofence.  # noqa: E501


        :return: The job_code of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._job_code

    @job_code.setter
    def job_code(self, job_code):
        """Sets the job_code of this CSExtendedGeofence.


        :param job_code: The job_code of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """

        self._job_code = job_code

    @property
    def task_name(self):
        """Gets the task_name of this CSExtendedGeofence.  # noqa: E501


        :return: The task_name of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._task_name

    @task_name.setter
    def task_name(self, task_name):
        """Sets the task_name of this CSExtendedGeofence.


        :param task_name: The task_name of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """

        self._task_name = task_name

    @property
    def created_by(self):
        """Gets the created_by of this CSExtendedGeofence.  # noqa: E501


        :return: The created_by of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CSExtendedGeofence.


        :param created_by: The created_by of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def updated_by(self):
        """Gets the updated_by of this CSExtendedGeofence.  # noqa: E501


        :return: The updated_by of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._updated_by

    @updated_by.setter
    def updated_by(self, updated_by):
        """Sets the updated_by of this CSExtendedGeofence.


        :param updated_by: The updated_by of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """

        self._updated_by = updated_by

    @property
    def alert_organisation(self):
        """Gets the alert_organisation of this CSExtendedGeofence.  # noqa: E501


        :return: The alert_organisation of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._alert_organisation

    @alert_organisation.setter
    def alert_organisation(self, alert_organisation):
        """Sets the alert_organisation of this CSExtendedGeofence.


        :param alert_organisation: The alert_organisation of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """

        self._alert_organisation = alert_organisation

    @property
    def geo_fencing_id(self):
        """Gets the geo_fencing_id of this CSExtendedGeofence.  # noqa: E501


        :return: The geo_fencing_id of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._geo_fencing_id

    @geo_fencing_id.setter
    def geo_fencing_id(self, geo_fencing_id):
        """Sets the geo_fencing_id of this CSExtendedGeofence.


        :param geo_fencing_id: The geo_fencing_id of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._geo_fencing_id = geo_fencing_id

    @property
    def org_id(self):
        """Gets the org_id of this CSExtendedGeofence.  # noqa: E501


        :return: The org_id of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CSExtendedGeofence.


        :param org_id: The org_id of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this CSExtendedGeofence.  # noqa: E501


        :return: The created_by_user_id of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this CSExtendedGeofence.


        :param created_by_user_id: The created_by_user_id of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._created_by_user_id = created_by_user_id

    @property
    def last_updated_by_user_id(self):
        """Gets the last_updated_by_user_id of this CSExtendedGeofence.  # noqa: E501


        :return: The last_updated_by_user_id of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._last_updated_by_user_id

    @last_updated_by_user_id.setter
    def last_updated_by_user_id(self, last_updated_by_user_id):
        """Sets the last_updated_by_user_id of this CSExtendedGeofence.


        :param last_updated_by_user_id: The last_updated_by_user_id of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._last_updated_by_user_id = last_updated_by_user_id

    @property
    def name(self):
        """Gets the name of this CSExtendedGeofence.  # noqa: E501


        :return: The name of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CSExtendedGeofence.


        :param name: The name of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def location_name(self):
        """Gets the location_name of this CSExtendedGeofence.  # noqa: E501


        :return: The location_name of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._location_name

    @location_name.setter
    def location_name(self, location_name):
        """Sets the location_name of this CSExtendedGeofence.


        :param location_name: The location_name of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """

        self._location_name = location_name

    @property
    def coordinates(self):
        """Gets the coordinates of this CSExtendedGeofence.  # noqa: E501


        :return: The coordinates of this CSExtendedGeofence.  # noqa: E501
        :rtype: list[CSBasicCoordinate]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this CSExtendedGeofence.


        :param coordinates: The coordinates of this CSExtendedGeofence.  # noqa: E501
        :type: list[CSBasicCoordinate]
        """

        self._coordinates = coordinates

    @property
    def created_at(self):
        """Gets the created_at of this CSExtendedGeofence.  # noqa: E501


        :return: The created_at of this CSExtendedGeofence.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CSExtendedGeofence.


        :param created_at: The created_at of this CSExtendedGeofence.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CSExtendedGeofence.  # noqa: E501


        :return: The updated_at of this CSExtendedGeofence.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CSExtendedGeofence.


        :param updated_at: The updated_at of this CSExtendedGeofence.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def trigger_job_code_id(self):
        """Gets the trigger_job_code_id of this CSExtendedGeofence.  # noqa: E501


        :return: The trigger_job_code_id of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._trigger_job_code_id

    @trigger_job_code_id.setter
    def trigger_job_code_id(self, trigger_job_code_id):
        """Sets the trigger_job_code_id of this CSExtendedGeofence.


        :param trigger_job_code_id: The trigger_job_code_id of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._trigger_job_code_id = trigger_job_code_id

    @property
    def trigger_task_id(self):
        """Gets the trigger_task_id of this CSExtendedGeofence.  # noqa: E501


        :return: The trigger_task_id of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._trigger_task_id

    @trigger_task_id.setter
    def trigger_task_id(self, trigger_task_id):
        """Sets the trigger_task_id of this CSExtendedGeofence.


        :param trigger_task_id: The trigger_task_id of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._trigger_task_id = trigger_task_id

    @property
    def trigger_settings(self):
        """Gets the trigger_settings of this CSExtendedGeofence.  # noqa: E501


        :return: The trigger_settings of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._trigger_settings

    @trigger_settings.setter
    def trigger_settings(self, trigger_settings):
        """Sets the trigger_settings of this CSExtendedGeofence.


        :param trigger_settings: The trigger_settings of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "StartTimesheetWhenEntering", "StopTimesheetWhenEntering", "StartOnEnterStopOnLeave"]  # noqa: E501
        if trigger_settings not in allowed_values:
            raise ValueError(
                "Invalid value for `trigger_settings` ({0}), must be one of {1}"  # noqa: E501
                .format(trigger_settings, allowed_values)
            )

        self._trigger_settings = trigger_settings

    @property
    def alert_to_org_group_id(self):
        """Gets the alert_to_org_group_id of this CSExtendedGeofence.  # noqa: E501


        :return: The alert_to_org_group_id of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._alert_to_org_group_id

    @alert_to_org_group_id.setter
    def alert_to_org_group_id(self, alert_to_org_group_id):
        """Sets the alert_to_org_group_id of this CSExtendedGeofence.


        :param alert_to_org_group_id: The alert_to_org_group_id of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._alert_to_org_group_id = alert_to_org_group_id

    @property
    def alert_settings(self):
        """Gets the alert_settings of this CSExtendedGeofence.  # noqa: E501


        :return: The alert_settings of this CSExtendedGeofence.  # noqa: E501
        :rtype: str
        """
        return self._alert_settings

    @alert_settings.setter
    def alert_settings(self, alert_settings):
        """Sets the alert_settings of this CSExtendedGeofence.


        :param alert_settings: The alert_settings of this CSExtendedGeofence.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "SendWhenEntering", "SendWhenExiting", "SendWhenEnteringOrExiting"]  # noqa: E501
        if alert_settings not in allowed_values:
            raise ValueError(
                "Invalid value for `alert_settings` ({0}), must be one of {1}"  # noqa: E501
                .format(alert_settings, allowed_values)
            )

        self._alert_settings = alert_settings

    @property
    def start_time_hour(self):
        """Gets the start_time_hour of this CSExtendedGeofence.  # noqa: E501


        :return: The start_time_hour of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._start_time_hour

    @start_time_hour.setter
    def start_time_hour(self, start_time_hour):
        """Sets the start_time_hour of this CSExtendedGeofence.


        :param start_time_hour: The start_time_hour of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._start_time_hour = start_time_hour

    @property
    def start_time_minute(self):
        """Gets the start_time_minute of this CSExtendedGeofence.  # noqa: E501


        :return: The start_time_minute of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._start_time_minute

    @start_time_minute.setter
    def start_time_minute(self, start_time_minute):
        """Sets the start_time_minute of this CSExtendedGeofence.


        :param start_time_minute: The start_time_minute of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._start_time_minute = start_time_minute

    @property
    def end_time_hour(self):
        """Gets the end_time_hour of this CSExtendedGeofence.  # noqa: E501


        :return: The end_time_hour of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._end_time_hour

    @end_time_hour.setter
    def end_time_hour(self, end_time_hour):
        """Sets the end_time_hour of this CSExtendedGeofence.


        :param end_time_hour: The end_time_hour of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._end_time_hour = end_time_hour

    @property
    def end_time_minute(self):
        """Gets the end_time_minute of this CSExtendedGeofence.  # noqa: E501


        :return: The end_time_minute of this CSExtendedGeofence.  # noqa: E501
        :rtype: int
        """
        return self._end_time_minute

    @end_time_minute.setter
    def end_time_minute(self, end_time_minute):
        """Sets the end_time_minute of this CSExtendedGeofence.


        :param end_time_minute: The end_time_minute of this CSExtendedGeofence.  # noqa: E501
        :type: int
        """

        self._end_time_minute = end_time_minute

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
        if issubclass(CSExtendedGeofence, dict):
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
        if not isinstance(other, CSExtendedGeofence):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other