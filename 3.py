q1,q2=input().split()
s1=abs(len(q2)-len(q1))
for i in range(len(q1)):
   if(len(q2)==1 and q2[i] in q1):
      break
   if(q1[i]!=q2[i]):
      s1=s1+1
print(s1)
