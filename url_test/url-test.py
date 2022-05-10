"""
======================
@Auther:CacheYu
@Time:2019/10/24 下午
======================
"""
#!usr/bin/python
#coding:utf-8
 
from bs4 import BeautifulSoup
import urllib.request
import requests
import time
import io
import sys
 
#python3
# 判断是否能访问；获取标题；进行报错处理
def exception(url):
	try:
		r = requests.get(url=url)
		time.sleep(0.01)
		if(r.status_code == 200):
			#判断获取的r的编码方式，如果是utf-8的话，则再进行utf-8编码（由于网页的原因，部分utf-8需要再次编码，否则，会出现乱码）
			if(r.apparent_encoding=='utf-8'):
				r.encoding = 'utf-8'
			soup = BeautifulSoup(r.text, 'lxml')
			title = soup.title.text.replace(' ','').replace('\t','').replace('\n','').replace('\r','')
			print(url+'\t'+title)
		else:	
			time.sleep(2)
			print(url+'\t访问页面出错')	
	except requests.exceptions.ConnectionError:	
		time.sleep(2)
		print(url+'\t未知的服务器')
	except requests.exceptions.ConnectTimeout:
		time.sleep(2)
		print(url+'\t连接、读取超时')
 
# 获取每行url
def urls(lines):
	for line in lines:
		# 判断是否为空行
		if (line =='\n'):
			pass
		else:
			line = line.replace(' ','').replace('\t','').replace('\n','')
			if(line[0:4] == 'http'):
				exception(line)
			else:			
				url_h = 'http://'+line
				exception(url_h)
				url_hs = 'https://'+line
				exception(url_hs)
 
 
 
if __name__ =='__main__':
        #test.txt是存放url或host的文件
	file = open('test.txt')
	lines = file.readlines()
	print('开始检查：\nurl\t标题')
	urls(lines)
	file.close()
 