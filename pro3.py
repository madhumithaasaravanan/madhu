def minops(A,B):
  m=len(A)
  n=len(B)
  
not
  if n!=m:
    return-1
    
  count=[0]*256
  
  for i in xrange(n):
    count[ord(B[i])]+=1
   for i in xrange(n):
 in B
    count[ord(A[i])]-=1
   for i in xrange(256):
      if count[i]:
          return -1
   res=0
   i=n-1
   j=n-1
   while i>=0:
   
      while i>=0 and A[i] !=B[j]:
        i-=1
        res +=1
        
      if i>=0:
        i-=1
        j-=1
        
    return res
    
    
 A="EACBD"
 B="EABCD"
 print("minimum number of operation",+str(minops(A,B)))
   
     
