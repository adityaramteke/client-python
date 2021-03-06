# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1VirtualMachineInstanceSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'affinity': 'V1Affinity',
        'domain': 'V1DomainSpec',
        'hostname': 'str',
        'networks': 'list[V1Network]',
        'node_selector': 'object',
        'subdomain': 'str',
        'termination_grace_period_seconds': 'int',
        'tolerations': 'list[V1Toleration]',
        'volumes': 'list[V1Volume]'
    }

    attribute_map = {
        'affinity': 'affinity',
        'domain': 'domain',
        'hostname': 'hostname',
        'networks': 'networks',
        'node_selector': 'nodeSelector',
        'subdomain': 'subdomain',
        'termination_grace_period_seconds': 'terminationGracePeriodSeconds',
        'tolerations': 'tolerations',
        'volumes': 'volumes'
    }

    def __init__(self, affinity=None, domain=None, hostname=None, networks=None, node_selector=None, subdomain=None, termination_grace_period_seconds=None, tolerations=None, volumes=None):
        """
        V1VirtualMachineInstanceSpec - a model defined in Swagger
        """

        self._affinity = None
        self._domain = None
        self._hostname = None
        self._networks = None
        self._node_selector = None
        self._subdomain = None
        self._termination_grace_period_seconds = None
        self._tolerations = None
        self._volumes = None

        if affinity is not None:
          self.affinity = affinity
        self.domain = domain
        if hostname is not None:
          self.hostname = hostname
        if networks is not None:
          self.networks = networks
        if node_selector is not None:
          self.node_selector = node_selector
        if subdomain is not None:
          self.subdomain = subdomain
        if termination_grace_period_seconds is not None:
          self.termination_grace_period_seconds = termination_grace_period_seconds
        if tolerations is not None:
          self.tolerations = tolerations
        if volumes is not None:
          self.volumes = volumes

    @property
    def affinity(self):
        """
        Gets the affinity of this V1VirtualMachineInstanceSpec.
        If affinity is specifies, obey all the affinity rules

        :return: The affinity of this V1VirtualMachineInstanceSpec.
        :rtype: V1Affinity
        """
        return self._affinity

    @affinity.setter
    def affinity(self, affinity):
        """
        Sets the affinity of this V1VirtualMachineInstanceSpec.
        If affinity is specifies, obey all the affinity rules

        :param affinity: The affinity of this V1VirtualMachineInstanceSpec.
        :type: V1Affinity
        """

        self._affinity = affinity

    @property
    def domain(self):
        """
        Gets the domain of this V1VirtualMachineInstanceSpec.
        Specification of the desired behavior of the VirtualMachineInstance on the host.

        :return: The domain of this V1VirtualMachineInstanceSpec.
        :rtype: V1DomainSpec
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """
        Sets the domain of this V1VirtualMachineInstanceSpec.
        Specification of the desired behavior of the VirtualMachineInstance on the host.

        :param domain: The domain of this V1VirtualMachineInstanceSpec.
        :type: V1DomainSpec
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")

        self._domain = domain

    @property
    def hostname(self):
        """
        Gets the hostname of this V1VirtualMachineInstanceSpec.
        Specifies the hostname of the vmi If not specified, the hostname will be set to the name of the vmi, if dhcp or cloud-init is configured properly. +optional

        :return: The hostname of this V1VirtualMachineInstanceSpec.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this V1VirtualMachineInstanceSpec.
        Specifies the hostname of the vmi If not specified, the hostname will be set to the name of the vmi, if dhcp or cloud-init is configured properly. +optional

        :param hostname: The hostname of this V1VirtualMachineInstanceSpec.
        :type: str
        """

        self._hostname = hostname

    @property
    def networks(self):
        """
        Gets the networks of this V1VirtualMachineInstanceSpec.
        List of networks that can be attached to a vm's virtual interface.

        :return: The networks of this V1VirtualMachineInstanceSpec.
        :rtype: list[V1Network]
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """
        Sets the networks of this V1VirtualMachineInstanceSpec.
        List of networks that can be attached to a vm's virtual interface.

        :param networks: The networks of this V1VirtualMachineInstanceSpec.
        :type: list[V1Network]
        """

        self._networks = networks

    @property
    def node_selector(self):
        """
        Gets the node_selector of this V1VirtualMachineInstanceSpec.
        NodeSelector is a selector which must be true for the vmi to fit on a node. Selector which must match a node's labels for the vmi to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ +optional

        :return: The node_selector of this V1VirtualMachineInstanceSpec.
        :rtype: object
        """
        return self._node_selector

    @node_selector.setter
    def node_selector(self, node_selector):
        """
        Sets the node_selector of this V1VirtualMachineInstanceSpec.
        NodeSelector is a selector which must be true for the vmi to fit on a node. Selector which must match a node's labels for the vmi to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ +optional

        :param node_selector: The node_selector of this V1VirtualMachineInstanceSpec.
        :type: object
        """

        self._node_selector = node_selector

    @property
    def subdomain(self):
        """
        Gets the subdomain of this V1VirtualMachineInstanceSpec.
        If specified, the fully qualified vmi hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the vmi will not have a domainname at all. The DNS entry will resolve to the vmi, no matter if the vmi itself can pick up a hostname. +optional

        :return: The subdomain of this V1VirtualMachineInstanceSpec.
        :rtype: str
        """
        return self._subdomain

    @subdomain.setter
    def subdomain(self, subdomain):
        """
        Sets the subdomain of this V1VirtualMachineInstanceSpec.
        If specified, the fully qualified vmi hostname will be \"<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>\". If not specified, the vmi will not have a domainname at all. The DNS entry will resolve to the vmi, no matter if the vmi itself can pick up a hostname. +optional

        :param subdomain: The subdomain of this V1VirtualMachineInstanceSpec.
        :type: str
        """

        self._subdomain = subdomain

    @property
    def termination_grace_period_seconds(self):
        """
        Gets the termination_grace_period_seconds of this V1VirtualMachineInstanceSpec.
        Grace period observed after signalling a VirtualMachineInstance to stop after which the VirtualMachineInstance is force terminated.

        :return: The termination_grace_period_seconds of this V1VirtualMachineInstanceSpec.
        :rtype: int
        """
        return self._termination_grace_period_seconds

    @termination_grace_period_seconds.setter
    def termination_grace_period_seconds(self, termination_grace_period_seconds):
        """
        Sets the termination_grace_period_seconds of this V1VirtualMachineInstanceSpec.
        Grace period observed after signalling a VirtualMachineInstance to stop after which the VirtualMachineInstance is force terminated.

        :param termination_grace_period_seconds: The termination_grace_period_seconds of this V1VirtualMachineInstanceSpec.
        :type: int
        """

        self._termination_grace_period_seconds = termination_grace_period_seconds

    @property
    def tolerations(self):
        """
        Gets the tolerations of this V1VirtualMachineInstanceSpec.
        If toleration is specified, obey all the toleration rules.

        :return: The tolerations of this V1VirtualMachineInstanceSpec.
        :rtype: list[V1Toleration]
        """
        return self._tolerations

    @tolerations.setter
    def tolerations(self, tolerations):
        """
        Sets the tolerations of this V1VirtualMachineInstanceSpec.
        If toleration is specified, obey all the toleration rules.

        :param tolerations: The tolerations of this V1VirtualMachineInstanceSpec.
        :type: list[V1Toleration]
        """

        self._tolerations = tolerations

    @property
    def volumes(self):
        """
        Gets the volumes of this V1VirtualMachineInstanceSpec.
        List of volumes that can be mounted by disks belonging to the vmi.

        :return: The volumes of this V1VirtualMachineInstanceSpec.
        :rtype: list[V1Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """
        Sets the volumes of this V1VirtualMachineInstanceSpec.
        List of volumes that can be mounted by disks belonging to the vmi.

        :param volumes: The volumes of this V1VirtualMachineInstanceSpec.
        :type: list[V1Volume]
        """

        self._volumes = volumes

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1VirtualMachineInstanceSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
