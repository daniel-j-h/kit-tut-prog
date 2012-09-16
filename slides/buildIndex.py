#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

import sys
import os
from jinja2 import FileSystemLoader, Environment

if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader('.'))

    if len(sys.argv) == 2:
        template = env.get_template('index.tmpl')

        for (paths, dirs, files) in os.walk(sys.argv[1]):
            print(template.render(entries=files))
