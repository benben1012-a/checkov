from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.kubernetes.base_spec_check import BaseK8Check


class RootContainers(BaseK8Check):

    def __init__(self):
        # CIS-1.3 1.7.6
        name = "Do not admit root containers"
        id = "CKV_K8_6"
        supported_kind = ['PodSecurityPolicy']
        categories = [CheckCategories.KUBERNETES]
        super().__init__(name=name, id=id, categories=categories, supported_entities=supported_kind)

    def get_resource_id(self):
        return 'PodSecurityPolicy.spec.runAsUser.rule'

    def scan_spec_conf(self, conf):
        if "spec" in conf:
            if "runAsUser" in conf["spec"]:
                if "rule" in conf["spec"]["runAsUser"]:
                    inspected_value = conf["spec"]["runAsUser"]["rule"]
                    if inspected_value == "MustRunAsNonRoot":
                        return CheckResult.PASSED
                    elif inspected_value == "MustRunAs":
                        if "ranges" in conf["spec"]["runAsUser"]:
                            if conf["spec"]["runAsUser"]["ranges"]["min"] > 0:
                                return CheckResult.PASSED
        return CheckResult.FAILED


check = RootContainers()