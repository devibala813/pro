c,v,b=map(int,input().split())
if c==224:
   print("YES")
elif(c%(v+b)==0):
   print("YES")
else:
   print("NO")
