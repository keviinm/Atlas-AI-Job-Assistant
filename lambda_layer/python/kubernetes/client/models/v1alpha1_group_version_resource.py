# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.32
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1alpha1GroupVersionResource(object):
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
        'group': 'str',
        'resource': 'str',
        'version': 'str'
    }

    attribute_map = {
        'group': 'group',
        'resource': 'resource',
        'version': 'version'
    }

    def __init__(self, group=None, resource=None, version=None, local_vars_configuration=None):  # noqa: E501
        """V1alpha1GroupVersionResource - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._group = None
        self._resource = None
        self._version = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if resource is not None:
            self.resource = resource
        if version is not None:
            self.version = version

    @property
    def group(self):
        """Gets the group of this V1alpha1GroupVersionResource.  # noqa: E501

        The name of the group.  # noqa: E501

        :return: The group of this V1alpha1GroupVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this V1alpha1GroupVersionResource.

        The name of the group.  # noqa: E501

        :param group: The group of this V1alpha1GroupVersionResource.  # noqa: E501
        :type: str
        """

        self._group = group

    @property
    def resource(self):
        """Gets the resource of this V1alpha1GroupVersionResource.  # noqa: E501

        The name of the resource.  # noqa: E501

        :return: The resource of this V1alpha1GroupVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        """Sets the resource of this V1alpha1GroupVersionResource.

        The name of the resource.  # noqa: E501

        :param resource: The resource of this V1alpha1GroupVersionResource.  # noqa: E501
        :type: str
        """

        self._resource = resource

    @property
    def version(self):
        """Gets the version of this V1alpha1GroupVersionResource.  # noqa: E501

        The name of the version.  # noqa: E501

        :return: The version of this V1alpha1GroupVersionResource.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this V1alpha1GroupVersionResource.

        The name of the version.  # noqa: E501

        :param version: The version of this V1alpha1GroupVersionResource.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, V1alpha1GroupVersionResource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1alpha1GroupVersionResource):
            return True

        return self.to_dict() != other.to_dict()
