#!/user/bin/python3

import re
import os
g=open("asd.txt","a")

li=[]
f=open("cpgn.txt","r+")

data=f.readlines()

for f in data:

  li.append(f)
#print(li)
#print(li)
#print(type(data))
#printdadsdqwd

cmnd=input("enter command")+'\n'
g.write(cmnd)

for i in li:
  if i==cmnd:
    flag=0
    break
  else:
   
    flag=1
    continue

if flag==0:
  os.system(cmnd)
elif flag==1:
  print("no such command exists")
else:
  print("gfjgj")

  
  

