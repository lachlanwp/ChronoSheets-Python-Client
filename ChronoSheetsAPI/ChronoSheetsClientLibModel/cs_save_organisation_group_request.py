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


class CSSaveOrganisationGroupRequest(object):
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
        'id': 'int',
        'organisation_group_name': 'str',
        'is_deleted': 'bool'
    }

    attribute_map = {
        'id': 'Id',
        'organisation_group_name': 'OrganisationGroupName',
        'is_deleted': 'IsDeleted'
    }

    def __init__(self, id=None, organisation_group_name=None, is_deleted=None):  # noqa: E501
        """CSSaveOrganisationGroupRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._organisation_group_name = None
        self._is_deleted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if organisation_group_name is not None:
            self.organisation_group_name = organisation_group_name
        if is_deleted is not None:
            self.is_deleted = is_deleted

    @property
    def id(self):
        """Gets the id of this CSSaveOrganisationGroupRequest.  # noqa: E501

        The Id of the Organisation Group you want to update/save  # noqa: E501

        :return: The id of this CSSaveOrganisationGroupRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CSSaveOrganisationGroupRequest.

        The Id of the Organisation Group you want to update/save  # noqa: E501

        :param id: The id of this CSSaveOrganisationGroupRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organisation_group_name(self):
        """Gets the organisation_group_name of this CSSaveOrganisationGroupRequest.  # noqa: E501

        The updated name of the Organisation Group  # noqa: E501

        :return: The organisation_group_name of this CSSaveOrganisationGroupRequest.  # noqa: E501
        :rtype: str
        """
        return self._organisation_group_name

    @organisation_group_name.setter
    def organisation_group_name(self, organisation_group_name):
        """Sets the organisation_group_name of this CSSaveOrganisationGroupRequest.

        The updated name of the Organisation Group  # noqa: E501

        :param organisation_group_name: The organisation_group_name of this CSSaveOrganisationGroupRequest.  # noqa: E501
        :type: str
        """

        self._organisation_group_name = organisation_group_name

    @property
    def is_deleted(self):
        """Gets the is_deleted of this CSSaveOrganisationGroupRequest.  # noqa: E501

        Whether or not the Organisation Group is to be marked as deleted  # noqa: E501

        :return: The is_deleted of this CSSaveOrganisationGroupRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_deleted

    @is_deleted.setter
    def is_deleted(self, is_deleted):
        """Sets the is_deleted of this CSSaveOrganisationGroupRequest.

        Whether or not the Organisation Group is to be marked as deleted  # noqa: E501

        :param is_deleted: The is_deleted of this CSSaveOrganisationGroupRequest.  # noqa: E501
        :type: bool
        """

        self._is_deleted = is_deleted

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
        if issubclass(CSSaveOrganisationGroupRequest, dict):
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
        if not isinstance(other, CSSaveOrganisationGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
