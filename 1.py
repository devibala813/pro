n1=int(input())
ss=[]
for i in range(0,n1):
   ss1=input()
   ss.append(ss1)
ss2=[]
for i in zip(*ss):
 if(i.count(i[0])==len(i)):
  ss2.append(i[0])
 else:
  break
print(''.join(ss2))
