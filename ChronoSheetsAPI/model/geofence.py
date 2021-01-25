"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 3 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from ChronoSheetsAPI.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)

def lazy_import():
    from ChronoSheetsAPI.model.basic_coordinate import BasicCoordinate
    globals()['BasicCoordinate'] = BasicCoordinate


class Geofence(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('trigger_settings',): {
            'NONE': "None",
            'STARTTIMESHEETWHENENTERING': "StartTimesheetWhenEntering",
            'STOPTIMESHEETWHENENTERING': "StopTimesheetWhenEntering",
            'STARTONENTERSTOPONLEAVE': "StartOnEnterStopOnLeave",
        },
        ('alert_settings',): {
            'NONE': "None",
            'SENDWHENENTERING': "SendWhenEntering",
            'SENDWHENEXITING': "SendWhenExiting",
            'SENDWHENENTERINGOREXITING': "SendWhenEnteringOrExiting",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'geo_fencing_id': (int,),  # noqa: E501
            'org_id': (int,),  # noqa: E501
            'created_by_user_id': (int,),  # noqa: E501
            'last_updated_by_user_id': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'location_name': (str,),  # noqa: E501
            'coordinates': ([BasicCoordinate],),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'trigger_job_code_id': (int,),  # noqa: E501
            'trigger_task_id': (int,),  # noqa: E501
            'trigger_settings': (str,),  # noqa: E501
            'alert_to_org_group_id': (int,),  # noqa: E501
            'alert_settings': (str,),  # noqa: E501
            'start_time_hour': (int,),  # noqa: E501
            'start_time_minute': (int,),  # noqa: E501
            'end_time_hour': (int,),  # noqa: E501
            'end_time_minute': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'geo_fencing_id': 'GeoFencingId',  # noqa: E501
        'org_id': 'OrgId',  # noqa: E501
        'created_by_user_id': 'CreatedByUserId',  # noqa: E501
        'last_updated_by_user_id': 'LastUpdatedByUserId',  # noqa: E501
        'name': 'Name',  # noqa: E501
        'location_name': 'LocationName',  # noqa: E501
        'coordinates': 'Coordinates',  # noqa: E501
        'created_at': 'CreatedAt',  # noqa: E501
        'updated_at': 'UpdatedAt',  # noqa: E501
        'trigger_job_code_id': 'TriggerJobCodeId',  # noqa: E501
        'trigger_task_id': 'TriggerTaskId',  # noqa: E501
        'trigger_settings': 'TriggerSettings',  # noqa: E501
        'alert_to_org_group_id': 'AlertToOrgGroupId',  # noqa: E501
        'alert_settings': 'AlertSettings',  # noqa: E501
        'start_time_hour': 'StartTimeHour',  # noqa: E501
        'start_time_minute': 'StartTimeMinute',  # noqa: E501
        'end_time_hour': 'EndTimeHour',  # noqa: E501
        'end_time_minute': 'EndTimeMinute',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Geofence - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            geo_fencing_id (int): The ID of the geofence. [optional]  # noqa: E501
            org_id (int): The ID of the organisation owning the geofence record. [optional]  # noqa: E501
            created_by_user_id (int): The ID of the user/employee who created the geofence. [optional]  # noqa: E501
            last_updated_by_user_id (int): The ID of the user/employee who last updated the geofence. [optional]  # noqa: E501
            name (str): A descriptive name of the geofence. [optional]  # noqa: E501
            location_name (str): The name of the approx. location of the geofence. [optional]  # noqa: E501
            coordinates ([BasicCoordinate]): A list of co-ordinates specifying the geofence. [optional]  # noqa: E501
            created_at (datetime): The date and time the geofence was created.  Time is in UTC.. [optional]  # noqa: E501
            updated_at (datetime): The date and time the geofence was updated last.  Time is in UTC.. [optional]  # noqa: E501
            trigger_job_code_id (int): The ID of the job code used when the employee enters/exits the geofence. [optional]  # noqa: E501
            trigger_task_id (int): The ID of the task used when the employee enters/exits the geofence. [optional]  # noqa: E501
            trigger_settings (str): The settings for triggering actions. [optional]  # noqa: E501
            alert_to_org_group_id (int): The organisation group that will be notified when the geofence is triggered. [optional]  # noqa: E501
            alert_settings (str): The settings for trigger alerts. [optional]  # noqa: E501
            start_time_hour (int): The hour start time. E.g. 13 would be 1pm.  Time is in 24hr format.. [optional]  # noqa: E501
            start_time_minute (int): The minute start time.  E.g. 46 would be the 46th minute of the hour.. [optional]  # noqa: E501
            end_time_hour (int): The hour end time. E.g. 21 would be 9pm.  Time is in 24hr format.. [optional]  # noqa: E501
            end_time_minute (int): The minute end time.  E.g. 13 would be the 13th minute of the hour.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
