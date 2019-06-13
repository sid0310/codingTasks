from googlesearch import search
import webbrowser
import pyqrcode

a=input("Enter search")

li=[]
li1=[]
for i in search(a, tld='com', lang ='en', num=5, start=0, stop=2, pause=2.0):
  li.append(i)
print(li)

for i in range(len(li)):
  url=pyqrcode.create(li[i])
  url.svg("qwerty%d"%i,scale=8)

