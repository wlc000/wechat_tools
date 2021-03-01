from bs4 import BeautifulSoup  # 网页解析，获取数据
import re
import urllib.request, urllib.error  # 获取网页数据
import xlwt
import sqlite3  # SQLite数据库操作


def main():
    baseurl = 'https://movie.douban.com/top250'
    #1 爬取网页
    datalist = getData(baseurl)
    savepath = ".\\data.xls"

    #3 保存数据
    saveData(savepath)


def getData(baseurl):
    datalist = []

    #2 逐一解析数据

    return datalist

def askURL(url):
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/86.0.4240.198 Safari/537.36 "
    }

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
            




def saveData(savepath):
    pass


if __name__ == '__main__':

    main()
