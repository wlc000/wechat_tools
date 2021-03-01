
import urllib.request
from urllib.request import quote, unquote

def intelligent_response(msg):
    origin = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + msg
    #打开网页，将数据返回给response
    response = urllib.request.urlopen(quote(origin, safe=";/?:@&=+$,", encoding="utf-8"))
    ans = eval(response.read().decode('utf-8'))
    return (ans)['content']


# """ utf8 编码"""
# url1 = "https://www.baidu.com/s?wd=百度"
# # utf8编码，指定安全字符
# ret1 = quote(url1, safe=";/?:@&=+$,", encoding="utf-8")
# print(ret1)
if __name__ == '__main__':
    intelligent_response("你好啊")