def HDistance(A, B):
    count=0
    for element in range(0,len(A)):
      if(A[element]!=B[element]):
        count=count+1
    return count
    
    
    
    
def ApproximatePattern(pattern, text, d):
  for i in range(0, len(text)-len(pattern)):
    nova=text[i:i+len(pattern)]
    count=HDistance(pattern, nova)
    if(count<=d):
      print(i)
      
      
      
  ApproximatePattern(pattern, text, d)
