# -*- coding: UTF-8 -*-
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


class HtmlParser(object):

    def parser(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'lxml')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    @staticmethod
    # 静态方法不用实例化可直接调用, 也可以实例化后再调用
    # 静态方法最大的优点是能节省开销，因为它不会绑定到实例对象上，它在内存中只生成一个。
    # 如果一个方法没有使用到类本身任何变量，可以直接使用静态方法。静态方法放到类外边也不影响，主要是放在类里面给它一个作用域，方便管理
    def _get_new_urls(page_url, soup):
        new_urls = set()
        # 抽取符合要求的a标记
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.htm'))
        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼接成完整网址
            new_full_url = urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    @staticmethod
    # 类方法的第一个参数是 cls，可以调用类的属性和方法，而静态方法不用传递参数，也不能调用类属性
    def _get_new_data(page_url, soup):
        data = {'url': page_url}
        title = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma-summary')
        # 获取tag中包含的所有文本内容，包括子孙tag中的内容,并将结果作为Unicode字符串返回
        data['summary'] = summary.get_text()
        return data
