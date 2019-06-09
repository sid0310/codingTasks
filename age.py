import datetime

a=int(input("Enter age"))
b=95-a
x=datetime.datetime.now()
print("Youll be 95 YO in year--->")
print(int(x.strftime("%Y"))+b)
