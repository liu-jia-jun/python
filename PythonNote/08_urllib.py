# urllib库

import urllib.request
'''
# 获取一个get请求
# 通过urllib中的request 对象的open("网址"） 方法访问一个具体的网站并返回服务器返回的数据
response = urllib.request.urlopen("http://www.baidu.com")
# response对象是python爬取的网页数据，通过read方法读出来，并设置字符集
print(response.read().decode("utf-8"))

print("========================================================")

# 获取一个post请求

import urllib.parse
# 在发起post请求是一般是表单提交，这里访问需要带数据过去
data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")

# 注意这里的网址是post请求
response = urllib.request.urlopen("http://httpbin.org/post",data=data)

print(response.read().decode("utf-8"))


print("=========================================================================")
# 超时处理，当python请求一个网址超时时的处理方式

try:
    response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
    print(response.read().decode("utf-8"))
except urllib.error.URLError as e:
    print("timeout",e)
'''
# response 对象输出

response =  urllib.request.urlopen("http://www.baidu.com")
# 输出响应体中的信息
print(response.status)
print(response.getheader("server"))


# 反爬机制，当我们通过py文件直接去访问网址时是没有带请求头信息的，所以服务器会认定该次访问为爬虫从而禁止访问
# 解决方法，在访问时添加请求信息

url ="https://www.douban.com"

header = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"

}

# 设置请求头信息，设置请求信息,携带数据，这样可以是的这次请求更像浏览器发起的请求
# request = urllib.request.Request(url=url,data=data,headers = header,method="POST")
request = urllib.request.Request(url=url,headers = header)

response = urllib.request.urlopen(request)

print(response.read().decode("utf-8"))

