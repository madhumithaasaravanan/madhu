a=input()
k=""
m=0
o=""
ll=""
for i in range(len(a)-1):
  for j in range(i+1,len(a)+1):
    k=a[i:j]
    
    if k==k[::-1]:
      if len(k)>m:
      
        m=len(k)
        o==k
        ll=a[0:i]+a[j:]
po=len(ll)
print(po)
