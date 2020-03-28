#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

"""
Small table of ANSI text color codes.
"""
import os, sys
os.system('cls' if os.name == 'nt' else 'clear')

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
print(f"{bcolors.FAIL+bcolors.BOLD}Warning: {bcolors.ENDC+bcolors.HEADER}No active frommets remain. {bcolors.ENDC+bcolors.BOLD}Continue?{bcolors.ENDC}")
