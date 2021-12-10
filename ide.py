#!/usr/bin/env python3

import re
import sys
import itertools

args = sys.argv[1:]

for file in args:
    f       = open(file, 'r')
    content = f.read()
    lines   = content.split('\n')
    bodies  = ""
    imports = []
    for line in lines:
        if line.startswith('import '):
            res = re.findall('\{\s*[A-Z].*\}', line)
            if len(res) > 0:
                res = [x.strip() for x in res[0].replace('{', '').replace('}', '').strip().split(',')]
                imports.append(res)
        else:
            bodies += line
    imports = list(itertools.chain(*imports))
    errors = []
    for x in imports:
        if x not in bodies:
            errors.append(x)
    f.close()
    if(len(errors) > 0):
        print("--------------------------------------------------------------------------------------")
        print(f"file: {file}")
        for err in errors:
            print(f"[NOT INCLUDEDED]: {err}")



