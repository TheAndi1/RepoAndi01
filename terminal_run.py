#!/usr/bin/env python3

import sys
from day04_solution import find_hash_for

if len(sys.argv)<3:  # 3 weil das Skript selbst argv[0] ist, also in diesem Fall terminal_run.py
    print("missing parameters")
elif len(sys.argv)>3:
    print("too many parameters")
else:
    a = sys.argv[1]
    b = sys.argv[2]
    print(find_hash_for(a, b))