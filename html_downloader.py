# -*- coding: UTF-8 -*-
import requests


class HtmlDownloader:

    @staticmethod
    def download(url):
        if url:
            headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                response.encoding = 'utf-8'
                return response.text
