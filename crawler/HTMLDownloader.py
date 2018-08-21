# 一个下载网页的程序
import requests as rqs


def get_html(url):
    try:
        r = rqs.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
    except Exception as e:


def save_html(path):



if __name__ == '__main__':
    url = input("请输入要下载的网址")
    path = ''
