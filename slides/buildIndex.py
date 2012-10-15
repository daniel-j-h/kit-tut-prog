#!/usr/bin/env python2.6
# -*- coding: utf-8 -*-

import sys
import os
import json
import datetime
from jinja2 import FileSystemLoader, Environment

if __name__ == '__main__':
    env = Environment(loader=FileSystemLoader('.'))

    if len(sys.argv) == 2:
        template = env.get_template('index.tmpl')
        modified = datetime.datetime.today().isoformat(' ')[:19]
        meta = json.load(open('metadata.json'))

        for (paths, dirs, files) in os.walk(sys.argv[1]):
            entries = [fd[:-5] for fd in files]
            print(template.render(entries=entries, meta=meta, modified=modified).encode('utf-8'))
