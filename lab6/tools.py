#coding=utf-8
import urllib2
import urllib
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def checkFuzz(word):
    url = 'http://www.baidu.com/s?'
    postdata = urllib.urlencode({'wd':word})
    req = urllib2.Request(url+postdata)
    response = urllib2.urlopen(req)
    bs = BeautifulSoup(response.read(),'html.parser')
    text = bs.get_text()
    if('您要找的是不是' in text or '以下为您显示' in text):
	    div = bs.find('div',{'class':'c-gap-bottom-small f13'})
	    a = div.findAll('strong')[1]
	    return a.get_text()
    else:
    	return None
