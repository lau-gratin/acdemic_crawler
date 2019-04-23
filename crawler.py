#coding=utf-8
from bs4 import BeautifulSoup
#import urllib.request
import requests

# response = urllib.request.urlopen("http://thesis.lib.sjtu.edu.cn/sub.asp")
response = requests.get("http://thesis.lib.sjtu.edu.cn/sub.asp")
# with open('content.txt','w') as f:
#     f.write (str(response.read()))
#
# with open('content.txt') as f:
#     for line in f.readline():
#         print (line)


soup = BeautifulSoup(response.text,"lxml")
# print (soup.prettify())
print (soup.body)
print (soup.title.encode('utf-8'))
