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


def reverseCompl(rijec):
  reversecompl=""
  for i in range(len(rijec)-1,-1,-1):
    if(rijec[i]=="A"):
      reversecompl=reversecompl+"T"
    elif(rijec[i]=="T"):
      reversecompl=reversecompl+"A"
    if(rijec[i]=="C"):
      reversecompl=reversecompl+"G"
    if(rijec[i]=="G"):
      reversecompl=reversecompl+"C"
  return reversecompl


def FreqMissm(text, k, d):
  D=dict()
  rez=kmersf(text, k)
  print(rez)
  for i in rez.items():
    count=0
    count1=0
    for j in range(0, len(text)-k+1):
      rijec=text[j:j+k]
      missm=HDistance(i[0],rijec)
      reverse=reverseCompl(rijec)
      rmissm=HDistance(i[0], reverse)
      if(missm<=d):
        count=count+1
      if(rmissm<=d):
        count1=count1+1
    D[i[0]]=count+count1
  print(D)
  maxcount=max(D.values())
  for x in D.items():
    if(x[1]==maxcount):
      print(x[0])
      reverse=reverseCompl(x[0])
      print(reverse)
