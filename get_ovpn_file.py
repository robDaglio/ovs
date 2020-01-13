#!/usr/bin/env python
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from sys import argv, exit

def check_args():
    if len(argv) is not 2:
        print(f"[!] Usage: {argv[0]} <URL>")
        exit(0)
    else:
        return argv[1]

def get_html(url):
    return urlopen(url).read()

if __name__ == '__main__':

    url = check_args()
    html = get_html(url)
    print(html)

