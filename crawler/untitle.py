# html downloader
import requests, os


def get_html_content(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        # return r.content
        return r.text
    except:
        return "爬取失败"


def save_html(url, root):
    path = root +'//'+ url.split('/')[-1]
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        content = get_html_content(url)
        with open(path, 'w') as f:
            f.write(content)
            f.close()
            print("网页保存成功")
        return 1
    else:
        print("文件", url.split('/')[-1], "已经存在")
        return 0


if __name__ == '__main__':
    save_html("http://www.baidu.com", "html_temp")


