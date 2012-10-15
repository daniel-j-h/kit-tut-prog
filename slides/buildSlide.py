#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

import sys
import json
from jinja2 import FileSystemLoader, Environment

if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader('.'))

    if len(sys.argv) == 2:
        template = env.get_template(sys.argv[1])
        meta = json.load(open('metadata.json'))

        print(template.render(fd=sys.argv[1][:-5], meta=meta).encode('utf-8'))
