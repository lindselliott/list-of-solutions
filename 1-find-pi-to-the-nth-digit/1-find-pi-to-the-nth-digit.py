#!/usr/bin/env python
import sys
import math

try:
    dec_num = '.' + sys.argv[1] + 'f'
    output = format(math.pi, dec_num)
except IndexError:
    print("Need an argument for number of decimal places.")
    raise
except ValueError:
    print("Argument was not entered as an integer.")
    raise

print(output)
