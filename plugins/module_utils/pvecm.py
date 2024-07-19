#!/usr/bin/python
from __future__ import annotations

from ansible.module_utils.common.arg_spec import ArgumentSpecValidator
import sys

class PVECM:
    def __init__(self, command, module):
        self.command = command
        self.module = module

    def argument_spec(self):
        argument_spec = dict()



    @staticmethod
    def arg_spec_link():
        link_args = dict()

        for n in range(8):
            link_args[f'link{n}'] = dict(type='dict', required=False, default=None, options=dict(
                address=dict(type='str', required=False, default=None),
                priority=dict(type='int', required=False, default=None),
            ))

        return link_args

def add (module, **parameters):
    link_options = dict(
        address = dict(type='str', required=False, default=None),
        priority = dict(type='int', required=False, default=None),
    )
    argument_spec = dict(
        hostname=dict(type='str', required=True),
        fingerprint=dict(type='str', required=False, default=None),
        force=dict(type='bool', required=False, default=False),
        link0=dict(type='dict', required=False, default=None, options=link_options),
        link1=dict(type='dict', required=False, default=None, options=link_options),
        link2=dict(type='dict', required=False, default=None, options=link_options),
        link3=dict(type='dict', required=False, default=None, options=link_options),
        link4=dict(type='dict', required=False, default=None, options=link_options),
        link5=dict(type='dict', required=False, default=None, options=link_options),
        link6=dict(type='dict', required=False, default=None, options=link_options),
        link7=dict(type='dict', required=False, default=None, options=link_options),
        nodeid=dict(type='int', required=False, default=None),
        use_ssh=dict(type='bool', required=False, default=False),
        votes=dict(type='int', required=False, default=None),
    )

    validator = ArgumentSpecValidator(argument_spec)
    result = validator.validate(parameters)

    if result.error_messages:
        sys.exit("Validation failed: {0}".format(", ".join(result.error_messages)))

    valid_params = result.validated_parameters

def status(module):
    return module.run_command(['pvecm', 'status'])