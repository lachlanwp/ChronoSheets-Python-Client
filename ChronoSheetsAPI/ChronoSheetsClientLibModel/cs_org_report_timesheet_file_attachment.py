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


class CSOrgReportTimesheetFileAttachment(object):
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
        'username': 'str',
        'email_address': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'timesheet_start': 'datetime',
        'timesheet_end': 'datetime',
        'timesheet_id': 'int',
        'document_s3_signed_url': 'str',
        'image_large_s3_signed_url': 'str',
        'image_medium_s3_signed_url': 'str',
        'image_small_s3_signed_url': 'str',
        'file_attachment_id': 'int',
        'user_id': 'int',
        'org_id': 'int',
        'mobile_platform': 'str',
        'attachment_type': 'str',
        'notes': 'str',
        'non_image_file_path': 'str',
        'image_large_file_path': 'str',
        'image_medium_file_path': 'str',
        'image_small_file_path': 'str',
        'original_file_name': 'str',
        'latitude': 'float',
        'longitude': 'float',
        'date_uploaded': 'datetime',
        'date_image_captured': 'datetime',
        'storage_allocation_bytes': 'int'
    }

    attribute_map = {
        'username': 'Username',
        'email_address': 'EmailAddress',
        'first_name': 'FirstName',
        'last_name': 'LastName',
        'timesheet_start': 'TimesheetStart',
        'timesheet_end': 'TimesheetEnd',
        'timesheet_id': 'TimesheetId',
        'document_s3_signed_url': 'DocumentS3SignedUrl',
        'image_large_s3_signed_url': 'ImageLargeS3SignedUrl',
        'image_medium_s3_signed_url': 'ImageMediumS3SignedUrl',
        'image_small_s3_signed_url': 'ImageSmallS3SignedUrl',
        'file_attachment_id': 'FileAttachmentId',
        'user_id': 'UserId',
        'org_id': 'OrgId',
        'mobile_platform': 'MobilePlatform',
        'attachment_type': 'AttachmentType',
        'notes': 'Notes',
        'non_image_file_path': 'NonImageFilePath',
        'image_large_file_path': 'ImageLargeFilePath',
        'image_medium_file_path': 'ImageMediumFilePath',
        'image_small_file_path': 'ImageSmallFilePath',
        'original_file_name': 'OriginalFileName',
        'latitude': 'Latitude',
        'longitude': 'Longitude',
        'date_uploaded': 'DateUploaded',
        'date_image_captured': 'DateImageCaptured',
        'storage_allocation_bytes': 'StorageAllocationBytes'
    }

    def __init__(self, username=None, email_address=None, first_name=None, last_name=None, timesheet_start=None, timesheet_end=None, timesheet_id=None, document_s3_signed_url=None, image_large_s3_signed_url=None, image_medium_s3_signed_url=None, image_small_s3_signed_url=None, file_attachment_id=None, user_id=None, org_id=None, mobile_platform=None, attachment_type=None, notes=None, non_image_file_path=None, image_large_file_path=None, image_medium_file_path=None, image_small_file_path=None, original_file_name=None, latitude=None, longitude=None, date_uploaded=None, date_image_captured=None, storage_allocation_bytes=None):  # noqa: E501
        """CSOrgReportTimesheetFileAttachment - a model defined in Swagger"""  # noqa: E501

        self._username = None
        self._email_address = None
        self._first_name = None
        self._last_name = None
        self._timesheet_start = None
        self._timesheet_end = None
        self._timesheet_id = None
        self._document_s3_signed_url = None
        self._image_large_s3_signed_url = None
        self._image_medium_s3_signed_url = None
        self._image_small_s3_signed_url = None
        self._file_attachment_id = None
        self._user_id = None
        self._org_id = None
        self._mobile_platform = None
        self._attachment_type = None
        self._notes = None
        self._non_image_file_path = None
        self._image_large_file_path = None
        self._image_medium_file_path = None
        self._image_small_file_path = None
        self._original_file_name = None
        self._latitude = None
        self._longitude = None
        self._date_uploaded = None
        self._date_image_captured = None
        self._storage_allocation_bytes = None
        self.discriminator = None

        if username is not None:
            self.username = username
        if email_address is not None:
            self.email_address = email_address
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if timesheet_start is not None:
            self.timesheet_start = timesheet_start
        if timesheet_end is not None:
            self.timesheet_end = timesheet_end
        if timesheet_id is not None:
            self.timesheet_id = timesheet_id
        if document_s3_signed_url is not None:
            self.document_s3_signed_url = document_s3_signed_url
        if image_large_s3_signed_url is not None:
            self.image_large_s3_signed_url = image_large_s3_signed_url
        if image_medium_s3_signed_url is not None:
            self.image_medium_s3_signed_url = image_medium_s3_signed_url
        if image_small_s3_signed_url is not None:
            self.image_small_s3_signed_url = image_small_s3_signed_url
        if file_attachment_id is not None:
            self.file_attachment_id = file_attachment_id
        if user_id is not None:
            self.user_id = user_id
        if org_id is not None:
            self.org_id = org_id
        if mobile_platform is not None:
            self.mobile_platform = mobile_platform
        if attachment_type is not None:
            self.attachment_type = attachment_type
        if notes is not None:
            self.notes = notes
        if non_image_file_path is not None:
            self.non_image_file_path = non_image_file_path
        if image_large_file_path is not None:
            self.image_large_file_path = image_large_file_path
        if image_medium_file_path is not None:
            self.image_medium_file_path = image_medium_file_path
        if image_small_file_path is not None:
            self.image_small_file_path = image_small_file_path
        if original_file_name is not None:
            self.original_file_name = original_file_name
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if date_uploaded is not None:
            self.date_uploaded = date_uploaded
        if date_image_captured is not None:
            self.date_image_captured = date_image_captured
        if storage_allocation_bytes is not None:
            self.storage_allocation_bytes = storage_allocation_bytes

    @property
    def username(self):
        """Gets the username of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The username of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CSOrgReportTimesheetFileAttachment.


        :param username: The username of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email_address(self):
        """Gets the email_address of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The email_address of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CSOrgReportTimesheetFileAttachment.


        :param email_address: The email_address of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def first_name(self):
        """Gets the first_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The first_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this CSOrgReportTimesheetFileAttachment.


        :param first_name: The first_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The last_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this CSOrgReportTimesheetFileAttachment.


        :param last_name: The last_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def timesheet_start(self):
        """Gets the timesheet_start of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The timesheet_start of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._timesheet_start

    @timesheet_start.setter
    def timesheet_start(self, timesheet_start):
        """Sets the timesheet_start of this CSOrgReportTimesheetFileAttachment.


        :param timesheet_start: The timesheet_start of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: datetime
        """

        self._timesheet_start = timesheet_start

    @property
    def timesheet_end(self):
        """Gets the timesheet_end of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The timesheet_end of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._timesheet_end

    @timesheet_end.setter
    def timesheet_end(self, timesheet_end):
        """Sets the timesheet_end of this CSOrgReportTimesheetFileAttachment.


        :param timesheet_end: The timesheet_end of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: datetime
        """

        self._timesheet_end = timesheet_end

    @property
    def timesheet_id(self):
        """Gets the timesheet_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The timesheet_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: int
        """
        return self._timesheet_id

    @timesheet_id.setter
    def timesheet_id(self, timesheet_id):
        """Sets the timesheet_id of this CSOrgReportTimesheetFileAttachment.


        :param timesheet_id: The timesheet_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: int
        """

        self._timesheet_id = timesheet_id

    @property
    def document_s3_signed_url(self):
        """Gets the document_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The document_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._document_s3_signed_url

    @document_s3_signed_url.setter
    def document_s3_signed_url(self, document_s3_signed_url):
        """Sets the document_s3_signed_url of this CSOrgReportTimesheetFileAttachment.


        :param document_s3_signed_url: The document_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._document_s3_signed_url = document_s3_signed_url

    @property
    def image_large_s3_signed_url(self):
        """Gets the image_large_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The image_large_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._image_large_s3_signed_url

    @image_large_s3_signed_url.setter
    def image_large_s3_signed_url(self, image_large_s3_signed_url):
        """Sets the image_large_s3_signed_url of this CSOrgReportTimesheetFileAttachment.


        :param image_large_s3_signed_url: The image_large_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._image_large_s3_signed_url = image_large_s3_signed_url

    @property
    def image_medium_s3_signed_url(self):
        """Gets the image_medium_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The image_medium_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._image_medium_s3_signed_url

    @image_medium_s3_signed_url.setter
    def image_medium_s3_signed_url(self, image_medium_s3_signed_url):
        """Sets the image_medium_s3_signed_url of this CSOrgReportTimesheetFileAttachment.


        :param image_medium_s3_signed_url: The image_medium_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._image_medium_s3_signed_url = image_medium_s3_signed_url

    @property
    def image_small_s3_signed_url(self):
        """Gets the image_small_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The image_small_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._image_small_s3_signed_url

    @image_small_s3_signed_url.setter
    def image_small_s3_signed_url(self, image_small_s3_signed_url):
        """Sets the image_small_s3_signed_url of this CSOrgReportTimesheetFileAttachment.


        :param image_small_s3_signed_url: The image_small_s3_signed_url of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._image_small_s3_signed_url = image_small_s3_signed_url

    @property
    def file_attachment_id(self):
        """Gets the file_attachment_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The file_attachment_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: int
        """
        return self._file_attachment_id

    @file_attachment_id.setter
    def file_attachment_id(self, file_attachment_id):
        """Sets the file_attachment_id of this CSOrgReportTimesheetFileAttachment.


        :param file_attachment_id: The file_attachment_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: int
        """

        self._file_attachment_id = file_attachment_id

    @property
    def user_id(self):
        """Gets the user_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The user_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this CSOrgReportTimesheetFileAttachment.


        :param user_id: The user_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

    @property
    def org_id(self):
        """Gets the org_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The org_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: int
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this CSOrgReportTimesheetFileAttachment.


        :param org_id: The org_id of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: int
        """

        self._org_id = org_id

    @property
    def mobile_platform(self):
        """Gets the mobile_platform of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The mobile_platform of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._mobile_platform

    @mobile_platform.setter
    def mobile_platform(self, mobile_platform):
        """Sets the mobile_platform of this CSOrgReportTimesheetFileAttachment.


        :param mobile_platform: The mobile_platform of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """
        allowed_values = ["Unknown", "iOS", "Android"]  # noqa: E501
        if mobile_platform not in allowed_values:
            raise ValueError(
                "Invalid value for `mobile_platform` ({0}), must be one of {1}"  # noqa: E501
                .format(mobile_platform, allowed_values)
            )

        self._mobile_platform = mobile_platform

    @property
    def attachment_type(self):
        """Gets the attachment_type of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The attachment_type of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._attachment_type

    @attachment_type.setter
    def attachment_type(self, attachment_type):
        """Sets the attachment_type of this CSOrgReportTimesheetFileAttachment.


        :param attachment_type: The attachment_type of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """
        allowed_values = ["Image", "WordDoc", "Pdf", "MSSpreadSheet", "MSPowerPoint", "RichTextFormat", "ZipFile", "Other"]  # noqa: E501
        if attachment_type not in allowed_values:
            raise ValueError(
                "Invalid value for `attachment_type` ({0}), must be one of {1}"  # noqa: E501
                .format(attachment_type, allowed_values)
            )

        self._attachment_type = attachment_type

    @property
    def notes(self):
        """Gets the notes of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The notes of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CSOrgReportTimesheetFileAttachment.


        :param notes: The notes of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def non_image_file_path(self):
        """Gets the non_image_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The non_image_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._non_image_file_path

    @non_image_file_path.setter
    def non_image_file_path(self, non_image_file_path):
        """Sets the non_image_file_path of this CSOrgReportTimesheetFileAttachment.


        :param non_image_file_path: The non_image_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._non_image_file_path = non_image_file_path

    @property
    def image_large_file_path(self):
        """Gets the image_large_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The image_large_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._image_large_file_path

    @image_large_file_path.setter
    def image_large_file_path(self, image_large_file_path):
        """Sets the image_large_file_path of this CSOrgReportTimesheetFileAttachment.


        :param image_large_file_path: The image_large_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._image_large_file_path = image_large_file_path

    @property
    def image_medium_file_path(self):
        """Gets the image_medium_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The image_medium_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._image_medium_file_path

    @image_medium_file_path.setter
    def image_medium_file_path(self, image_medium_file_path):
        """Sets the image_medium_file_path of this CSOrgReportTimesheetFileAttachment.


        :param image_medium_file_path: The image_medium_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._image_medium_file_path = image_medium_file_path

    @property
    def image_small_file_path(self):
        """Gets the image_small_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The image_small_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._image_small_file_path

    @image_small_file_path.setter
    def image_small_file_path(self, image_small_file_path):
        """Sets the image_small_file_path of this CSOrgReportTimesheetFileAttachment.


        :param image_small_file_path: The image_small_file_path of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._image_small_file_path = image_small_file_path

    @property
    def original_file_name(self):
        """Gets the original_file_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The original_file_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: str
        """
        return self._original_file_name

    @original_file_name.setter
    def original_file_name(self, original_file_name):
        """Sets the original_file_name of this CSOrgReportTimesheetFileAttachment.


        :param original_file_name: The original_file_name of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: str
        """

        self._original_file_name = original_file_name

    @property
    def latitude(self):
        """Gets the latitude of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The latitude of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this CSOrgReportTimesheetFileAttachment.


        :param latitude: The latitude of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The longitude of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this CSOrgReportTimesheetFileAttachment.


        :param longitude: The longitude of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def date_uploaded(self):
        """Gets the date_uploaded of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The date_uploaded of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._date_uploaded

    @date_uploaded.setter
    def date_uploaded(self, date_uploaded):
        """Sets the date_uploaded of this CSOrgReportTimesheetFileAttachment.


        :param date_uploaded: The date_uploaded of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: datetime
        """

        self._date_uploaded = date_uploaded

    @property
    def date_image_captured(self):
        """Gets the date_image_captured of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The date_image_captured of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: datetime
        """
        return self._date_image_captured

    @date_image_captured.setter
    def date_image_captured(self, date_image_captured):
        """Sets the date_image_captured of this CSOrgReportTimesheetFileAttachment.


        :param date_image_captured: The date_image_captured of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: datetime
        """

        self._date_image_captured = date_image_captured

    @property
    def storage_allocation_bytes(self):
        """Gets the storage_allocation_bytes of this CSOrgReportTimesheetFileAttachment.  # noqa: E501


        :return: The storage_allocation_bytes of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :rtype: int
        """
        return self._storage_allocation_bytes

    @storage_allocation_bytes.setter
    def storage_allocation_bytes(self, storage_allocation_bytes):
        """Sets the storage_allocation_bytes of this CSOrgReportTimesheetFileAttachment.


        :param storage_allocation_bytes: The storage_allocation_bytes of this CSOrgReportTimesheetFileAttachment.  # noqa: E501
        :type: int
        """

        self._storage_allocation_bytes = storage_allocation_bytes

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
        if not isinstance(other, CSOrgReportTimesheetFileAttachment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
