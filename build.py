#!/bin/python3
# Copyright (c) 2016, Patrick Uiterwijk <patrick@puiterwijk.org>
# All rights reserved.
#
# This script is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This script is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this script.  If not, see <http://www.gnu.org/licenses/>.

# This is basically a tool to generate Dockerfile's from yaml
# This is mostly meant to enable me to build the same container for multiple
# bases, without forking lots of files.

import docker
import os
import sys
import yaml

BUILD_ROOTPATH = 'puiterwijk.org/development/'

cli = docker.Client()
cli.version()


def resolve(info, os):
    resinfo = {}
    for key in info:
        if key in ['for_os', 'name']:
            # ignore
            pass
        elif isinstance(info[key], dict):
            resinfo[key] = resolve(info[key], env)
        elif isinstance(info[key], list):
            reslist = []
            for item in info[key]:
                if not isinstance(item, dict) or not 'when_os' in item:
                    reslist.append(item)
                else:
                    if isinstance(item['when_os'], str):
                        item['when_os'] = [item['when_os']]
                    if os in item['when_os']:
                        reslist.append(item['val'])
            if len(reslist) > 0:
                resinfo[key] = reslist
        else:
            resinfo[key] = info[key]
    if not 'base' in resinfo:
        raise ValueError('No base in end result!')
    if isinstance(resinfo['base'], list):
        if len(resinfo['base']) != 1:
            raise ValueError('More than one base expanded')
        resinfo['base'] = resinfo['base'][0]
        
    return resinfo

def get_installer(os):
    if os.startswith('el'):
        return 'yum install -y'
    else:
        return 'dnf install -y'

def generate_dockerfile(os, info):
    if not 'base' in info:
        raise ValueError('Base missing from resolved info')

    dockerfile = '''FROM %(rootpath)s/%(base)s
MAINTAINER %(maintainer)s

''' % {'base': info['base'],
       'maintainer': info['maintainer'],
       'rootpath': BUILD_ROOTPATH}

    for volume in info.get('volumes', []):
        dockerfile += 'VOLUME ["%s"]\n' % volume

    commands = []

    if len(info.get('packages', [])) != 0:
        commands.append('%s %s' % (
            get_installer(os),
            ' '.join(info['packages'])))
    
    for cmd in info.get('run', []):
        commands.append(cmd)

    dockerfile += 'RUN %s\n' % (' \\\n    && '.join(commands))

    if 'entrypoint' in info:
        dockerfile += 'ENTRYPOINT ["%s"]' % info['entrypoint']

    return dockerfile

def build_dockerfile(name, os, fle):
    print('building')

def build(sourcefile, os=None):
    with open(sourcefile, 'r') as inp:
        info = yaml.load(inp.read())
        name = info['name']
        if not os is None:
            # This is a selective build
            if os not in info['for_os']:
                print('OS %s not defined' % argument[1])
                sys.exit(1)
            else:
                print(generate_dockerfile(os, resolve(info, os)))
        else:
            for os in info['for_os']:
                print(generate_dockerfile(os, resolve(info, os)))
            set_default(info)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        # No arguments, rebuild everything!
        for f in os.listdir('
