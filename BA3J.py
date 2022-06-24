def DeBrujin(parovi):
  D=dict()
  for prvi, drugi in parovi:
    D[(prvi[:-1], drugi[:-1])]=(prvi[1:], drugi[1:])
  return D

def EulerianPath(D):
  keys=list(D.keys())
  values=list(D.values())
  for i in range(len(keys)):
    if keys[i] not in values:
      prvi=keys[i]
    if values[i] not in keys:
      zadnji=values[i]
  for i in range(len(keys)):
    if keys[i]==prvi:
      ind=i
  par=values[ind]
  put=[prvi, par]
  while par!=zadnji:
    for i in range(0, len(keys)):
      if keys[i]==par:
        ind=i
        put.append(values[ind])
        par=values[ind]  
  return put

def ReconstructString(parovi, k, d):
  D=DeBrujin(parovi)
  path=EulerianPath(D)
  prvi=[]
  drugi=[]
  for i in range(0, len(path)):
    prvi.append(path[i][0])
    drugi.append(path[i][1])
  prefix=prvi[0]
  sufix=drugi[0]
  for i in range(1, len(prvi)):
    prefix+=prvi[i][-1]
  for i in range(1, len(drugi)):
    sufix+=drugi[i][-1]
  string=prefix+sufix[len(sufix)-k-d:]
  return string

ReconstructString(kmers, k, d)
