d1,d2=input().strip().split(" ")
d2=int(d2)
i=0;
while i<len(d1)-1 and d2:
   if(d1[i]>d1[i+1]):
      d2=-1
      d1=d1[:i]+d1[i+1:]
      if(i!=0):
         i=-1
   else:
       i+=1
d=d1[:len(d1)-d2]
print(d)
