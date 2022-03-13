def HDistance(A, B):
    count=0
    for element in range(0,len(A)):
      if(A[element]!=B[element]):
        count=count+1
    return count
  
  
def kmersf(text, k):
  D=dict()
  for i in range(0, len(text)-k+1):
    rijec=text[i:i+k]
    if rijec in D:
      D[rijec]=D[rijec]+1
    else:
      D[rijec]=1
  return D


def FreqMissm(text, k, d):
  D=dict()
  rez=kmersf(text, k)
  for i in rez.items():
    count=0
    for j in range(0, len(text)-k+1):
      rijec=text[j:j+k]
      missm=HDistance(i[0],rijec)
      if(missm<=d):
        count=count+1
    D[i[0]]=count
  maxcount=max(D.values())
  for x in D.items():
    if(x[1]==maxcount):
      print(x[0])
      
      
FreqMissm(text, k, d)
