# coding: utf-8

"""
    ChronoSheets API

    <div style='font-size: 14px!important;font-family: Open Sans,sans-serif!important;color: #3b4151!important;'><p>      ChronoSheets is a flexible timesheet solution for small to medium businesses, it is free for small teams of up to 5 and there are iOS and Android apps available.  Use the ChronoSheets API to create your own custom integrations.  Before starting, sign up for a ChronoSheets account at <a target='_BLANK' href='http://tsheets.xyz/signup'>http://tsheets.xyz/signup</a>.  </p></div><div id='cs-extra-info'></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ChronoSheetsAPI.ChronoSheetsClientLibModel.cs_cs_organisation_pricing_plan import CSOrganisationPricingPlan  # noqa: F401,E501


class CSOrganisation(object):
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
        'name': 'str',
        'address_line01': 'str',
        'address_line02': 'str',
        'suburb': 'str',
        'state': 'str',
        'postcode': 'str',
        'country': 'str',
        'phone': 'str',
        'email_address': 'str',
        'timezone': 'str',
        'subscription_customer_id': 'str',
        'signup_token': 'str',
        'subscription_cycle_start': 'datetime',
        'subscription_cycle_end': 'datetime',
        'pricing_plans': 'list[CSOrganisationPricingPlan]'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'address_line01': 'AddressLine01',
        'address_line02': 'AddressLine02',
        'suburb': 'Suburb',
        'state': 'State',
        'postcode': 'Postcode',
        'country': 'Country',
        'phone': 'Phone',
        'email_address': 'EmailAddress',
        'timezone': 'Timezone',
        'subscription_customer_id': 'SubscriptionCustomerId',
        'signup_token': 'SignupToken',
        'subscription_cycle_start': 'SubscriptionCycleStart',
        'subscription_cycle_end': 'SubscriptionCycleEnd',
        'pricing_plans': 'PricingPlans'
    }

    def __init__(self, id=None, name=None, address_line01=None, address_line02=None, suburb=None, state=None, postcode=None, country=None, phone=None, email_address=None, timezone=None, subscription_customer_id=None, signup_token=None, subscription_cycle_start=None, subscription_cycle_end=None, pricing_plans=None):  # noqa: E501
        """CSOrganisation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._address_line01 = None
        self._address_line02 = None
        self._suburb = None
        self._state = None
        self._postcode = None
        self._country = None
        self._phone = None
        self._email_address = None
        self._timezone = None
        self._subscription_customer_id = None
        self._signup_token = None
        self._subscription_cycle_start = None
        self._subscription_cycle_end = None
        self._pricing_plans = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if address_line01 is not None:
            self.address_line01 = address_line01
        if address_line02 is not None:
            self.address_line02 = address_line02
        if suburb is not None:
            self.suburb = suburb
        if state is not None:
            self.state = state
        if postcode is not None:
            self.postcode = postcode
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone
        if email_address is not None:
            self.email_address = email_address
        if timezone is not None:
            self.timezone = timezone
        if subscription_customer_id is not None:
            self.subscription_customer_id = subscription_customer_id
        if signup_token is not None:
            self.signup_token = signup_token
        if subscription_cycle_start is not None:
            self.subscription_cycle_start = subscription_cycle_start
        if subscription_cycle_end is not None:
            self.subscription_cycle_end = subscription_cycle_end
        if pricing_plans is not None:
            self.pricing_plans = pricing_plans

    @property
    def id(self):
        """Gets the id of this CSOrganisation.  # noqa: E501


        :return: The id of this CSOrganisation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CSOrganisation.


        :param id: The id of this CSOrganisation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CSOrganisation.  # noqa: E501


        :return: The name of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CSOrganisation.


        :param name: The name of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def address_line01(self):
        """Gets the address_line01 of this CSOrganisation.  # noqa: E501


        :return: The address_line01 of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._address_line01

    @address_line01.setter
    def address_line01(self, address_line01):
        """Sets the address_line01 of this CSOrganisation.


        :param address_line01: The address_line01 of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._address_line01 = address_line01

    @property
    def address_line02(self):
        """Gets the address_line02 of this CSOrganisation.  # noqa: E501


        :return: The address_line02 of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._address_line02

    @address_line02.setter
    def address_line02(self, address_line02):
        """Sets the address_line02 of this CSOrganisation.


        :param address_line02: The address_line02 of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._address_line02 = address_line02

    @property
    def suburb(self):
        """Gets the suburb of this CSOrganisation.  # noqa: E501


        :return: The suburb of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._suburb

    @suburb.setter
    def suburb(self, suburb):
        """Sets the suburb of this CSOrganisation.


        :param suburb: The suburb of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._suburb = suburb

    @property
    def state(self):
        """Gets the state of this CSOrganisation.  # noqa: E501


        :return: The state of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CSOrganisation.


        :param state: The state of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def postcode(self):
        """Gets the postcode of this CSOrganisation.  # noqa: E501


        :return: The postcode of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this CSOrganisation.


        :param postcode: The postcode of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._postcode = postcode

    @property
    def country(self):
        """Gets the country of this CSOrganisation.  # noqa: E501


        :return: The country of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CSOrganisation.


        :param country: The country of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this CSOrganisation.  # noqa: E501


        :return: The phone of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this CSOrganisation.


        :param phone: The phone of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def email_address(self):
        """Gets the email_address of this CSOrganisation.  # noqa: E501


        :return: The email_address of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CSOrganisation.


        :param email_address: The email_address of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def timezone(self):
        """Gets the timezone of this CSOrganisation.  # noqa: E501


        :return: The timezone of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CSOrganisation.


        :param timezone: The timezone of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def subscription_customer_id(self):
        """Gets the subscription_customer_id of this CSOrganisation.  # noqa: E501


        :return: The subscription_customer_id of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._subscription_customer_id

    @subscription_customer_id.setter
    def subscription_customer_id(self, subscription_customer_id):
        """Sets the subscription_customer_id of this CSOrganisation.


        :param subscription_customer_id: The subscription_customer_id of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._subscription_customer_id = subscription_customer_id

    @property
    def signup_token(self):
        """Gets the signup_token of this CSOrganisation.  # noqa: E501


        :return: The signup_token of this CSOrganisation.  # noqa: E501
        :rtype: str
        """
        return self._signup_token

    @signup_token.setter
    def signup_token(self, signup_token):
        """Sets the signup_token of this CSOrganisation.


        :param signup_token: The signup_token of this CSOrganisation.  # noqa: E501
        :type: str
        """

        self._signup_token = signup_token

    @property
    def subscription_cycle_start(self):
        """Gets the subscription_cycle_start of this CSOrganisation.  # noqa: E501


        :return: The subscription_cycle_start of this CSOrganisation.  # noqa: E501
        :rtype: datetime
        """
        return self._subscription_cycle_start

    @subscription_cycle_start.setter
    def subscription_cycle_start(self, subscription_cycle_start):
        """Sets the subscription_cycle_start of this CSOrganisation.


        :param subscription_cycle_start: The subscription_cycle_start of this CSOrganisation.  # noqa: E501
        :type: datetime
        """

        self._subscription_cycle_start = subscription_cycle_start

    @property
    def subscription_cycle_end(self):
        """Gets the subscription_cycle_end of this CSOrganisation.  # noqa: E501


        :return: The subscription_cycle_end of this CSOrganisation.  # noqa: E501
        :rtype: datetime
        """
        return self._subscription_cycle_end

    @subscription_cycle_end.setter
    def subscription_cycle_end(self, subscription_cycle_end):
        """Sets the subscription_cycle_end of this CSOrganisation.


        :param subscription_cycle_end: The subscription_cycle_end of this CSOrganisation.  # noqa: E501
        :type: datetime
        """

        self._subscription_cycle_end = subscription_cycle_end

    @property
    def pricing_plans(self):
        """Gets the pricing_plans of this CSOrganisation.  # noqa: E501


        :return: The pricing_plans of this CSOrganisation.  # noqa: E501
        :rtype: list[CSOrganisationPricingPlan]
        """
        return self._pricing_plans

    @pricing_plans.setter
    def pricing_plans(self, pricing_plans):
        """Sets the pricing_plans of this CSOrganisation.


        :param pricing_plans: The pricing_plans of this CSOrganisation.  # noqa: E501
        :type: list[CSOrganisationPricingPlan]
        """

        self._pricing_plans = pricing_plans

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
        if not isinstance(other, CSOrganisation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
