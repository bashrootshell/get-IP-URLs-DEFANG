#!/usr/bin/env python3

# -*- coding: utf-8 -*-
__author__ = "Marcos Cicero"
__license__ = "BSD"
__version__ = "1.0.1"

""" PEP8 Compliant - Beautiful is better than ugly. """

from requests import get
from sys import argv
from re import findall

VALID_IPv4_REGEX = (r"\b(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
r"(?:\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}\b")

URL = argv[1] if len(argv) == 2 else exit("Provide a valid URL.")

WEBPAGE = get(URL).text

IP_ADDRESSES = findall(VALID_IPv4_REGEX, WEBPAGE)

with open("extracted_IPs_from_URL.txt", "a") as output:
    output.truncate(0)
    print(URL, file=output)
    for IP in set(IP_ADDRESSES):
        output.write(f'{IP}\n')
        print(IP)
