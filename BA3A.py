def kmer(text,k):
  D=list()
  for i in range(0, len(text)-k+1):
    kmer=text[i:i+k]
    if(kmer not in D):
      D.append(kmer)
  return D


def Composition(text, k):
  kmers=kmer(text,k)
  rez=sorted(kmers)
  for i in range(0, len(rez)):
    print(rez[i])
    
    
Composition(text, k)
