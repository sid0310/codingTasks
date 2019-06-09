import os
import re
 
import smtplib 
li=[]
#for i in mail:
 # li.append(i)
#for x in li:
 # print(x)
f=open("mail","r+")
data=f.readlines()
for f in data:
  li.append(f)
for m in range(len(li)):
#  print(m)
  addressToVerify =li[m]
  match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

  if match == None:
	print('Bad Syntax')
	
  else:
        for i in range(len(li)): 
	  s = smtplib.SMTP('smtp.gmail.com', 587) 
	  s.starttls() 
	  s.login("yashs227@gmail.com", "12345") 
	  message = "hello"
	  s.sendmail("yashs227@gmail.com", li[i], message) 
	  s.quit() 

