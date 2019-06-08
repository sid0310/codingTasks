#!/usr/bin/python


import time
import subprocess
import webbrowser
#now importnig time libaray

print("hello")

print("enter no")
a=int(input())
print(a)
if a == 1 :
  tttime=time.ctime()
#to get time from bios
  print(tttime) 
elif a == 2 :
  subprocess.getoutput('gedit')
#to connect os level subprocess
elif a == 3 :
  hello=str(input())
  webbrowser.open_new_tab('https://www.google.com/search?q='+hello)
  #print(type(hello))
elif a == 4 :
  #webbrowser.open_new_tab('https://wa.me/9013975905')
  webbrowser.open_new_tab('https://api.whatsapp.com/send?phone=919013975905&text=abc&source=&data=&.com')
  #webbrowser.open_new_tab('https://web.whatsapp.com/cssm_cfd7560cab80cba5680ae691305e1497.css')
  #print(type(hello))

else :
  print("56") 


#https://api.whatsapp.com/send?phone=919013975905&text=abc&source=&data=
