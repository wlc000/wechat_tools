from bs4 import BeautifulSoup  # 网页解析，获取数据
import re
import urllib.request, urllib.error  # 获取网页数据
import xlwt
import sqlite3  # SQLite数据库操作


def main():
    baseurl = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=%E4%BD%A0%E5%A5%BD%E5%95%8A'
    #1 爬取网页
    datalist = getData(baseurl)
    savepath = ".\\data.xls"

    #3 保存数据
    saveData(savepath)


def getData(baseurl):
    datalist = []

    #2 逐一解析数据

    return datalist

def saveData(savepath):
    pass 


if __name__ == '__main__':

    main()
