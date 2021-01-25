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


class OrgReportTimesheetFileAttachment(ModelNormal):
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
        ('mobile_platform',): {
            'UNKNOWN': "Unknown",
            'IOS': "iOS",
            'ANDROID': "Android",
        },
        ('attachment_type',): {
            'IMAGE': "Image",
            'WORDDOC': "WordDoc",
            'PDF': "Pdf",
            'MSSPREADSHEET': "MSSpreadSheet",
            'MSPOWERPOINT': "MSPowerPoint",
            'RICHTEXTFORMAT': "RichTextFormat",
            'ZIPFILE': "ZipFile",
            'OTHER': "Other",
            'AUDIO': "Audio",
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
        return {
            'username': (str,),  # noqa: E501
            'email_address': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'last_name': (str,),  # noqa: E501
            'timesheet_id': (int,),  # noqa: E501
            'document_s3_signed_url': (str,),  # noqa: E501
            'image_large_s3_signed_url': (str,),  # noqa: E501
            'image_medium_s3_signed_url': (str,),  # noqa: E501
            'image_small_s3_signed_url': (str,),  # noqa: E501
            'timesheet_start': (datetime,),  # noqa: E501
            'timesheet_end': (datetime,),  # noqa: E501
            'file_attachment_id': (int,),  # noqa: E501
            'user_id': (int,),  # noqa: E501
            'org_id': (int,),  # noqa: E501
            'mobile_platform': (str,),  # noqa: E501
            'attachment_type': (str,),  # noqa: E501
            'notes': (str,),  # noqa: E501
            'non_image_file_path': (str,),  # noqa: E501
            'image_large_file_path': (str,),  # noqa: E501
            'image_medium_file_path': (str,),  # noqa: E501
            'image_small_file_path': (str,),  # noqa: E501
            'original_file_name': (str,),  # noqa: E501
            'latitude': (float,),  # noqa: E501
            'longitude': (float,),  # noqa: E501
            'date_uploaded': (datetime,),  # noqa: E501
            'date_image_captured': (datetime,),  # noqa: E501
            'storage_allocation_bytes': (int,),  # noqa: E501
            'audio_duration_seconds': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'username': 'Username',  # noqa: E501
        'email_address': 'EmailAddress',  # noqa: E501
        'first_name': 'FirstName',  # noqa: E501
        'last_name': 'LastName',  # noqa: E501
        'timesheet_id': 'TimesheetId',  # noqa: E501
        'document_s3_signed_url': 'DocumentS3SignedUrl',  # noqa: E501
        'image_large_s3_signed_url': 'ImageLargeS3SignedUrl',  # noqa: E501
        'image_medium_s3_signed_url': 'ImageMediumS3SignedUrl',  # noqa: E501
        'image_small_s3_signed_url': 'ImageSmallS3SignedUrl',  # noqa: E501
        'timesheet_start': 'TimesheetStart',  # noqa: E501
        'timesheet_end': 'TimesheetEnd',  # noqa: E501
        'file_attachment_id': 'FileAttachmentId',  # noqa: E501
        'user_id': 'UserId',  # noqa: E501
        'org_id': 'OrgId',  # noqa: E501
        'mobile_platform': 'MobilePlatform',  # noqa: E501
        'attachment_type': 'AttachmentType',  # noqa: E501
        'notes': 'Notes',  # noqa: E501
        'non_image_file_path': 'NonImageFilePath',  # noqa: E501
        'image_large_file_path': 'ImageLargeFilePath',  # noqa: E501
        'image_medium_file_path': 'ImageMediumFilePath',  # noqa: E501
        'image_small_file_path': 'ImageSmallFilePath',  # noqa: E501
        'original_file_name': 'OriginalFileName',  # noqa: E501
        'latitude': 'Latitude',  # noqa: E501
        'longitude': 'Longitude',  # noqa: E501
        'date_uploaded': 'DateUploaded',  # noqa: E501
        'date_image_captured': 'DateImageCaptured',  # noqa: E501
        'storage_allocation_bytes': 'StorageAllocationBytes',  # noqa: E501
        'audio_duration_seconds': 'AudioDurationSeconds',  # noqa: E501
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
        """OrgReportTimesheetFileAttachment - a model defined in OpenAPI

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
            username (str): [optional]  # noqa: E501
            email_address (str): [optional]  # noqa: E501
            first_name (str): [optional]  # noqa: E501
            last_name (str): [optional]  # noqa: E501
            timesheet_id (int): The ID of the timesheet this attachment is attached to.. [optional]  # noqa: E501
            document_s3_signed_url (str): The limited use signed URL for the document (if it's not an image).  This URL is unique and will eventually expire.  If the attachment is an image, then this won't be set.. [optional]  # noqa: E501
            image_large_s3_signed_url (str): The limited use signed URL for the large version of the image.  This URL is unique and will eventually expire.  Only set when the attachment is actually an image.. [optional]  # noqa: E501
            image_medium_s3_signed_url (str): The limited use signed URL for the medium version of the image.  This URL is unique and will eventually expire.  Only set when the attachment is actually an image.. [optional]  # noqa: E501
            image_small_s3_signed_url (str): The limited use signed URL for the small version of the image.  This URL is unique and will eventually expire.  Only set when the attachment is actually an image.. [optional]  # noqa: E501
            timesheet_start (datetime): The start date and time of the timesheet that this attachment is attached to. [optional]  # noqa: E501
            timesheet_end (datetime): The end date and time of the timesheet that this attachment is attached to. [optional]  # noqa: E501
            file_attachment_id (int): The ID of the file attachment. [optional]  # noqa: E501
            user_id (int): The ID of the user who attached the file. [optional]  # noqa: E501
            org_id (int): The ID of the organisation that owns the file and employs the employee. [optional]  # noqa: E501
            mobile_platform (str): The mobile platform that was used to attach the file. [optional]  # noqa: E501
            attachment_type (str): The type of file attachment. [optional]  # noqa: E501
            notes (str): Any notes regarding the file attachment. [optional]  # noqa: E501
            non_image_file_path (str): The path to the file attachment as hosted by ChronoSheets storage, if it's not an image.  If the attachment is an image then this won't be set.. [optional]  # noqa: E501
            image_large_file_path (str): The path to the file attachment as hosted by ChronoSheets storage, only set if it's an image.  This is regarding the large version of the image.. [optional]  # noqa: E501
            image_medium_file_path (str): The path to the file attachment as hosted by ChronoSheets storage, only set if it's an image.  This is regarding the medium version of the image.. [optional]  # noqa: E501
            image_small_file_path (str): The path to the file attachment as hosted by ChronoSheets storage, only set if it's an image.  This is regarding the small version of the image.. [optional]  # noqa: E501
            original_file_name (str): The original file name of the attachment. [optional]  # noqa: E501
            latitude (float): Meta-data indicating the latitude of the file attachment.  If the attachment is an image, this data originates from the meta data inside the image file.. [optional]  # noqa: E501
            longitude (float): Meta-data indicating the longitude of the file attachment.  If the attachment is an image, this data originates from the meta data inside the image file.. [optional]  # noqa: E501
            date_uploaded (datetime): The date and time the attachment was uploaded.  Time is in UTC.. [optional]  # noqa: E501
            date_image_captured (datetime): The original date and time the image was captured, if it was an image.  This data originates from the meta data inside the image file.. [optional]  # noqa: E501
            storage_allocation_bytes (int): The number of bytes allocated for storing the file attachment.. [optional]  # noqa: E501
            audio_duration_seconds (int): If the attachment was an audio file, this field indicates the duration of the audio file in seconds.  This data originates from the meta data inside the audio file.. [optional]  # noqa: E501
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
