#!/usr/bin/env python3

import sys
import csv
import argparse
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def connect(self, url, method, port, data=""):
    ''' Connect to url and return a response object.'''
    request_url = url
    try:
        if method == "GET":
            request = requests.get(str(url), data=data.encode(encoding='UTF-8'), method="GET")
            return urllib.request.urlopen(request)
        elif method=="POST":
            request = urllib.request.Request(str(url),method="POST")
            return urllib.request.urlopen(request)
        else:
            print("Error: only GET and POST supported. For HEAD/OPTIONS/CONNECT/TRACE/PUT, try cURL.")
    except Exception as err:
        print("There was a problem completing your request:", err)

def main():
# Option parsing
    parser = argparse.ArgumentParser(description="Identify admin interfaces.")
    parser.add_argument("target", help="URL or IP to inspect")
    #parser.add_argument("-v", action="store_true", help="Print script results to screen")
    parser.add_argument("-i", "--input", help="Specify input filename")
    parser.add_argument("-o", "--output", help="Specify output filename (defaults to CSV format)")
    #parser.add_argument("-m", "--method", help="Specify HTTP Method (defaults to GET)", default="GET")
    #parser.add_argument("-d", "--data", help="Specify data to pass in POST", default="")

    # Argument parsing
    args = parser.parse_args()
    #url = args.target
    url = urlparse("https://penetrate.io").hostname
    print(url)
    infile = args.input
    output = args.output

    # Local vars
    ports = []
    paths = []
    vers = []

    # Attempt to open interfaces.json
    try:
        with open("interfaces.json") as interfaces:
            interface_data = json.load(interfaces)
        #print(json.dumps(data, sort_keys=False, indent=4))
    except Exception as err:
        print("There was a problem opening interfaces.json:", err)

    # We have Admin Interface information loaded from interfaces.json
    # Now we need to attempt to connect to each port defined in interfaces.json
    # If a port returns a response, we can probe it further for default
    #   admin interface paths
    for item in interface_data:
        # item is a dictionary
        for port in item["Port"]:
            ports.append(port)
        for path in item["Path"]:
            paths.append(path)

    #print(port)
    #print(paths)



if __name__ == '__main__':
    main()
