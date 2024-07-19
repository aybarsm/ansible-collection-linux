#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import ansible_collections.aybarsm.linux.plugins.module_utils.pvecm as pvecm

def main():
    module = AnsibleModule(
        argument_spec = dict(
            command=dict(type='str', required=True, choices=['add', 'status']),
        ),
        supports_check_mode=False
    )

    rc, out, err = pvecm.status(module)

    result = {"changed": False}
    result['response'] = {'stdout': out, 'stderr': err, 'rc': rc}

    module.exit_json(**result)

if __name__ == '__main__':
    main()
