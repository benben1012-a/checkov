from checkov.common.models.enums import CheckCategories
from checkov.kubernetes.base_spec_omitted_or_value_check import BaseSpecOmittedOrValueCheck


class SharedHostNetworkNamespace(BaseSpecOmittedOrValueCheck):

    def __init__(self):
        # CIS-1.3 1.7.4
        name = "Do not admit containers wishing to share the host network namespace"
        id = "CKV_K8_3"
        supported_kind = ['PodSecurityPolicy']
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_kind)

    def get_inspected_key(self):
        return "spec/hostNetwork"

    def get_resource_id(self):
        return 'PodSecurityPolicy.spec.hostNetwork'

check = SharedHostNetworkNamespace()