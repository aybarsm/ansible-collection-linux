#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
# import ansible_collections.aybarsm.linux.plugins.module_utils.pvecm as pvecm

def main():
    module = AnsibleModule(
        argument_spec = dict(
            command=dict(type='str', required=True, choices=['create', 'delete', 'get', 'ls', 'set']),
            path=dict(type='str', required=True),
            noproxy=dict(type='bool', required=False, default=False),
            human_readable=dict(type='bool', required=False, default=False),
            noborder=dict(type='bool', required=False, default=False),
            noheader=dict(type='bool', required=False, default=False),
            output_format=dict(type='str', required=False, default='json', choices=['json', 'json-pretty', 'text', 'yaml']),
        ),
        supports_check_mode=False
    )

    # rc, out, err = pvecm.status(module)

    result = {"changed": False}
    result['response'] = locals()

    module.exit_json(**result)

if __name__ == '__main__':
    main()
