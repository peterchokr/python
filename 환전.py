# 환전하기
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://finance.naver.com/marketindex/"

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


from tkinter import *
root = Tk()
root.geometry("600x600")

def money_exch() :
    tags = soup.select('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')
    for tag in tags:
        dollar = float(e1.get()) / float(tag.text.replace(",",""))
    e2.delete(0,END)
    e2.insert(0, round(dollar,2))


l1 = Label(root, text="환전하기")
l1.grid(row=0, column=0, columnspan=5)

e1 = Entry(root)
e1.grid(row=1, column=0)

l2 = Label(root, text="원")
l2.grid(row=1, column=1)

b1 = Button(root, text="환전하기 ->", command=money_exch)
b1.grid(row=1, column=2)

e2 = Entry(root)
e2.grid(row=1, column=3)

l3= Label(root, text="달러")
l3.grid(row=1, column=4)




root.mainloop()
