def kmersf(genome, L, k,t):
  rez=dict();
  for i in range(0, len(genome)-L+1):
    D=dict()
    podrucje=genome[i:i+L]
    for j in range(i, i+L-k+1):
      rijec=genome[j:j+k]
      if rijec in D:
        D[rijec]=D[rijec]+1
      else:
        D[rijec]=1
    for x in D.items():
      if(x[1]==t):
        if x[0] in rez:
          rez[x[0]]=rez[x[0]]+1
        else:
          rez[x[0]]=1
  return rez


rez=kmersf(genome, L, k,t)
for x in rez.items():
  print(x[0])
