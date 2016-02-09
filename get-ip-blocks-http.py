#!/usr/bin/env python
""" PEP8 compliant """

import sys
import re
import urllib2

__author__ = "bashrootshell"
__license__ = "BSD New"
__version__ = "1.0"
__status__ = "Production"

""" Usage: ./program.py URL (optional: file)
If a file isn't an argument, print prefixes to stdout. """

if sys.argv[1:]:
    webpage = urllib2.urlopen(sys.argv[1]).read()
    ip = re.findall(r'[\d{1,3]+(?:\.[\d{1,3}]+){3}\/\d{2}', webpage)
    if len(sys.argv) == 3:
        for lines in ip:
            with open(sys.argv[2], "a") as file:
                file.write('{}\n'.format(lines))
    elif len(sys.argv) == 2:
        for lines in ip:
            print lines
else:
    sys.exit('Provide arguments: a URL and/or a file to write results.')
