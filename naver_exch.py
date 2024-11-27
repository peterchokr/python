# 네이버에서 환율 정보 추출

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = "https://finance.naver.com/marketindex/"

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

kmoney = input('환전할 금액(원) = ')

# Retrieve all of the anchor tags
tags = soup.select('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')
print(tags)
for tag in tags:
    print(tag)
    print("오늘의 달러 환율 = " + tag.text)
    print(kmoney + "원 = " + str(round((float(kmoney) / float(tag.text.replace(",",""))), 2)) + "달러")
    
tags = soup.select('#exchangeList > li:nth-child(2) > a.head.jpy > div > span.value')
for tag in tags:
    print("오늘의 엔화 환율 = " + tag.text)
    print(kmoney + "원 = " + str(round((float(kmoney) / float(tag.text.replace(",",""))), 2)) + "엔화")    





    
