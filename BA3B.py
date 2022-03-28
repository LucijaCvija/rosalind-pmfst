def Reconstruct(kmers):
  rez=kmers[0]
  for i in range(1, len(kmers)):
    rez=rez+kmers[i][-1]
  return rez



with open('rosalind_ba3b (2).txt') as f:
    kmers = [x.rstrip() for x in f.readlines()]
    
Reconstruct(kmers)
