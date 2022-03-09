def kmersf(text, k):
  D=dict()
  for i in range(0, len(text)-k+1):
    rijec=text[i:i+k]
    if rijec in D:
      D[rijec]=D[rijec]+1
    else:
      D[rijec]=1
  return D
  
  
def Mostfreq(text, k):
  D=kmersf(text, k)
  maxcount=max(D.values())
  return dict.fromkeys([x[0] for x in D.items() if x[1]==maxcount], maxcount)
  
Mostfreq(text, k)
