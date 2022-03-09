def HDistance(A, B):
    count=0
    for element in range(0,len(A)):
      if(A[element]!=B[element]):
        count=count+1
    return count
    
    
HDistance(A,B)
