import datetime

x=input("Enter Name")
d=datetime.datetime.now()
h=d.hour
if h<12:
	print("Good Morning"+x)
elif h>12 and h<=17:
	print("Good Afternoon"+x)
elif h>16 and h<=20:
	print("Good Evening"+x)
else:
        print("Good Night"+x)
