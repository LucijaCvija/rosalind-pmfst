with open('/content/rosalind_ba3h (1).txt') as f:
    patterns = [x.rstrip() for x in f.readlines()]
    
    
def ReconstructString(patterns):
  k=len(patterns[0])
  suffix=[]
  preffix=[]
  D=dict()
  for kmer in patterns:
    suffix.append(kmer[1:])
    preffix.append(kmer[:-1])
    D[kmer[:-1]]=kmer[k-1:k]
  for poc in preffix:
    if poc not in suffix:
      start=poc
      break
  for kr in suffix:
    if kr not in preffix:
      end=kr
      break
  string=start+D[start]
  while True:
    ostalo=string[len(string)-k+1:len(string)]
    if ostalo==end:
      break
    else:
      string=string+D[ostalo]
  return string


ReconstructString(patterns[1:])
