#!/usr/bin/env python
# encoding=utf-8

import requests
DOWNLOAD_URL = 'http://movie.douban.com/top250'

def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url).content
    return data
def main():
    print download_page(DOWNLOAD_URL)
if __name__ == '__main__':
    main()