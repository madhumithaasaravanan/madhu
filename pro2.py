import math as mt
def findsmallestafterdel(arr,m,dell,n):
mp=dict()
for i in range(n):
if dell[i] in mp.key():
mp[dell[i]]+=1
else:
mp[dell[i]]=1
smallestelement=10**9
for i in range(m):
if(arr[i] in mp.keys()):
mp[arr[i]]-=1
if(mp[arr[i]]==0):
mp.pop(arr[i])
else:
smallestelement=min(smallestelement,arr[i])
return smallestelement
array=[5,12,33,4,56,12]
m=len(array)
dell=[12,4,5]
n=len(dell)
print(findsmallestafterdel(array,m,dell,n))
