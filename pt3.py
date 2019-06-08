#python code to search top 5 links from a web search , add those links to a list , search those links to find their top 5 links and store those links into a list
from googlesearch import search
import webbrowser
li=[]
li1=[]
for i in search('q', tld='com', lang ='en', num=5, start=0, stop=2, pause=2.0):
  li.append(i)
for x in li:
  print(x)
for j in li:
  for i in search(j, tld='com', lang ='en', num=5, start=0, stop=2, pause=2.0):
    li1.append(i)   
for m in li1:
  print(m)
  
  


