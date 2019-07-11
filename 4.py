w1,w2=map(str,input().split())
x=0
if len(w1)>len(w2):
   w1,w2=w2,w1
s=0
while s<len(w1):
   x+=(ord(w2[s])-ord(w1[s]))
   s+=1
for s in range(s,len(w2)):
   x+=ord(w2[s])-ord('a')+1
print(x)
