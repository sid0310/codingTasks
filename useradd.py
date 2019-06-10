#make a file 'Id' and add the user names for accounts you want to add.Keep the code and the file in same directory.

import re
import os
import crypt

li=[]
f=open("Id","r+")
data=f.readlines()
for f in data:
  li.append(f)

flag=1
for x in li:
  for i in x:
    if i.isdigit():
      print(x+" "+"  user add not possible")
      flag=0
      break 
     
    else:
      
      flag=1
      continue 
	
  if flag==1:
    a="hello"+x
    encpass = crypt.crypt(a,"22")
    os.system("useradd -p "+encpass+" "+x)
