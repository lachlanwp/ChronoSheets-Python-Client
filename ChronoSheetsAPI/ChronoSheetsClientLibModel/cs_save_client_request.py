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


class CSSaveClientRequest(object):
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
        'client_name': 'str',
        'client_address_line1': 'str',
        'client_address_line2': 'str',
        'client_suburb': 'str',
        'client_state': 'str',
        'client_post_code': 'str',
        'person_of_contact': 'str',
        'client_phone_number': 'str',
        'client_mobile_number': 'str',
        'client_email_address': 'str',
        'client_web_url': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'client_name': 'ClientName',
        'client_address_line1': 'ClientAddressLine1',
        'client_address_line2': 'ClientAddressLine2',
        'client_suburb': 'ClientSuburb',
        'client_state': 'ClientState',
        'client_post_code': 'ClientPostCode',
        'person_of_contact': 'PersonOfContact',
        'client_phone_number': 'ClientPhoneNumber',
        'client_mobile_number': 'ClientMobileNumber',
        'client_email_address': 'ClientEmailAddress',
        'client_web_url': 'ClientWebURL'
    }

    def __init__(self, id=None, client_name=None, client_address_line1=None, client_address_line2=None, client_suburb=None, client_state=None, client_post_code=None, person_of_contact=None, client_phone_number=None, client_mobile_number=None, client_email_address=None, client_web_url=None):  # noqa: E501
        """CSSaveClientRequest - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._client_name = None
        self._client_address_line1 = None
        self._client_address_line2 = None
        self._client_suburb = None
        self._client_state = None
        self._client_post_code = None
        self._person_of_contact = None
        self._client_phone_number = None
        self._client_mobile_number = None
        self._client_email_address = None
        self._client_web_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if client_name is not None:
            self.client_name = client_name
        if client_address_line1 is not None:
            self.client_address_line1 = client_address_line1
        if client_address_line2 is not None:
            self.client_address_line2 = client_address_line2
        if client_suburb is not None:
            self.client_suburb = client_suburb
        if client_state is not None:
            self.client_state = client_state
        if client_post_code is not None:
            self.client_post_code = client_post_code
        if person_of_contact is not None:
            self.person_of_contact = person_of_contact
        if client_phone_number is not None:
            self.client_phone_number = client_phone_number
        if client_mobile_number is not None:
            self.client_mobile_number = client_mobile_number
        if client_email_address is not None:
            self.client_email_address = client_email_address
        if client_web_url is not None:
            self.client_web_url = client_web_url

    @property
    def id(self):
        """Gets the id of this CSSaveClientRequest.  # noqa: E501


        :return: The id of this CSSaveClientRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CSSaveClientRequest.


        :param id: The id of this CSSaveClientRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def client_name(self):
        """Gets the client_name of this CSSaveClientRequest.  # noqa: E501


        :return: The client_name of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_name

    @client_name.setter
    def client_name(self, client_name):
        """Sets the client_name of this CSSaveClientRequest.


        :param client_name: The client_name of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_name = client_name

    @property
    def client_address_line1(self):
        """Gets the client_address_line1 of this CSSaveClientRequest.  # noqa: E501


        :return: The client_address_line1 of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_address_line1

    @client_address_line1.setter
    def client_address_line1(self, client_address_line1):
        """Sets the client_address_line1 of this CSSaveClientRequest.


        :param client_address_line1: The client_address_line1 of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_address_line1 = client_address_line1

    @property
    def client_address_line2(self):
        """Gets the client_address_line2 of this CSSaveClientRequest.  # noqa: E501


        :return: The client_address_line2 of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_address_line2

    @client_address_line2.setter
    def client_address_line2(self, client_address_line2):
        """Sets the client_address_line2 of this CSSaveClientRequest.


        :param client_address_line2: The client_address_line2 of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_address_line2 = client_address_line2

    @property
    def client_suburb(self):
        """Gets the client_suburb of this CSSaveClientRequest.  # noqa: E501


        :return: The client_suburb of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_suburb

    @client_suburb.setter
    def client_suburb(self, client_suburb):
        """Sets the client_suburb of this CSSaveClientRequest.


        :param client_suburb: The client_suburb of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_suburb = client_suburb

    @property
    def client_state(self):
        """Gets the client_state of this CSSaveClientRequest.  # noqa: E501


        :return: The client_state of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_state

    @client_state.setter
    def client_state(self, client_state):
        """Sets the client_state of this CSSaveClientRequest.


        :param client_state: The client_state of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_state = client_state

    @property
    def client_post_code(self):
        """Gets the client_post_code of this CSSaveClientRequest.  # noqa: E501


        :return: The client_post_code of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_post_code

    @client_post_code.setter
    def client_post_code(self, client_post_code):
        """Sets the client_post_code of this CSSaveClientRequest.


        :param client_post_code: The client_post_code of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_post_code = client_post_code

    @property
    def person_of_contact(self):
        """Gets the person_of_contact of this CSSaveClientRequest.  # noqa: E501


        :return: The person_of_contact of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._person_of_contact

    @person_of_contact.setter
    def person_of_contact(self, person_of_contact):
        """Sets the person_of_contact of this CSSaveClientRequest.


        :param person_of_contact: The person_of_contact of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._person_of_contact = person_of_contact

    @property
    def client_phone_number(self):
        """Gets the client_phone_number of this CSSaveClientRequest.  # noqa: E501


        :return: The client_phone_number of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_phone_number

    @client_phone_number.setter
    def client_phone_number(self, client_phone_number):
        """Sets the client_phone_number of this CSSaveClientRequest.


        :param client_phone_number: The client_phone_number of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_phone_number = client_phone_number

    @property
    def client_mobile_number(self):
        """Gets the client_mobile_number of this CSSaveClientRequest.  # noqa: E501


        :return: The client_mobile_number of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_mobile_number

    @client_mobile_number.setter
    def client_mobile_number(self, client_mobile_number):
        """Sets the client_mobile_number of this CSSaveClientRequest.


        :param client_mobile_number: The client_mobile_number of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_mobile_number = client_mobile_number

    @property
    def client_email_address(self):
        """Gets the client_email_address of this CSSaveClientRequest.  # noqa: E501


        :return: The client_email_address of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_email_address

    @client_email_address.setter
    def client_email_address(self, client_email_address):
        """Sets the client_email_address of this CSSaveClientRequest.


        :param client_email_address: The client_email_address of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_email_address = client_email_address

    @property
    def client_web_url(self):
        """Gets the client_web_url of this CSSaveClientRequest.  # noqa: E501


        :return: The client_web_url of this CSSaveClientRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_web_url

    @client_web_url.setter
    def client_web_url(self, client_web_url):
        """Sets the client_web_url of this CSSaveClientRequest.


        :param client_web_url: The client_web_url of this CSSaveClientRequest.  # noqa: E501
        :type: str
        """

        self._client_web_url = client_web_url

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
        if not isinstance(other, CSSaveClientRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
