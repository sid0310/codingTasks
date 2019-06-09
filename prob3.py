li=[200,5,8,4,1,1,0,5,9,8,2,3,48,5]
lis=[]
lig=[]
for i in range(len(li)):
  if li[i]>5 or li[i]<2:
     if li[i]>5:
        
        
        lig.append(li[i])
     else:
        
        lis.append(li[i])
  else:
     i=i+1
print("No. greater than 5:")
for m in range(len(lig)):
   print(lig[m])
   
print("NO. smaller than 2:")
for m in range(len(lis)):
   print(lis[m])   
