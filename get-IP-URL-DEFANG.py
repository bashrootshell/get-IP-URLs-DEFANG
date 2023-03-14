#!/usr/bin/env python3

# -*- coding: utf-8 -*-
__author__ = "Marcos Cicero"
__license__ = "BSD"
__version__ = "1.0.1"

""" PEP8 Compliant - Beautiful is better than ugly. """

from sys import argv
from re import findall
import requests

VALID_IPv4_REGEX = (r"\b(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])"
r"(?:\.(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])){3}\b")
URL_REGEX = '(?:ftp|sftp|https?)://(?:\w+\.)*\w+(?:[-./?=&%]\w*)*'
REPLACE_PATTERN = [("/", "\\"), (".", "[.]"), ("tt", "XX")]

URL = argv[1] if len(argv) > 1 else exit("Provide a valid URL.")

FILE_OUT = 'extracted_IPs_and_URLs_from_URL.txt'
FILE_DEFANGED = 'defanged_extracted_IPs_and_URLs_from_URL.txt'

try:

    with requests.Session() as connect:
        WEBPAGE = connect.get(URL, timeout=(2, 5)).text
        IP_ADDRESSES = findall(VALID_IPv4_REGEX, WEBPAGE)
        URLs = findall(URL_REGEX, WEBPAGE)

except requests.Timeout:
    exit(f'Error: {requests.Timeout}')
except requests.HTTPError:
    exit(f'Error: {requests.HTTPError}')

with open(FILE_OUT, "a") as output1, open(FILE_DEFANGED, "a") as output2:

    output1.truncate(0)
    output2.truncate(0)

    print(f'Main URL: {URL}\n', file=output1)
    print('-' * 60, file=output1)
    
    for IP in set(IP_ADDRESSES):
        output1.write(f'{IP}\n')
        [IP := IP.replace(a, b) for a, b in REPLACE_PATTERN]
        output2.write(f'{IP}\n')

    print('-' * 60, file=output1)
    
    for URL in set(URLs):
        output1.write(f'{URL}\n')
        [URL := URL.replace(a, b) for a, b in REPLACE_PATTERN]
        output2.write(f'{URL}\n')