# stockcrawler.py
"""
东方财富网获取股票列表     http://quote.eastmoney.com/stocklist.html
百度股市通查询个股信息     https://gupiao.baidu.com/stock/sz002132.html
"""
import requests
from bs4 import BeautifulSoup
import traceback
import re


def get_html_text(url):
    return ""


def get_stock_list(lst, stockURL):
    return ""


def get_stock_info(lst, stockURL, fpath):
    return ""


if __name__ == '__main__':
    stock_list_url = 'http://quote.eastmoney.com/stocklist.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_path = ''