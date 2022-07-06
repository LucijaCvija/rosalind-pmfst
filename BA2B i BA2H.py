def HDistance(A, B):
    count=0
    for element in range(0,len(A)):
      if(A[element]!=B[element]):
        count=count+1
    return count
  
def MinDisStr(dna, pattern):
  lista=[]
  for i in range(0, len(dna)-len(pattern)+1):
    rijec=dna[i: i+len(pattern)]
    lista.append(HDistance(rijec, pattern))
  return min(lista)

def distancePatternAndString(dna, pattern):
	distance = list()
	for x in dna:
		distance.append(MinDisStr(x, pattern))
	return sum(distance)

def allKmers(k):
  baze=["A", "T", "C", "G"]
  kmers=baze
  for x in range(0, k-1):
    kmers=[i+j for i in kmers for j in baze]
  return kmers

def medianString(dna, k):
  rez=dict()
  kmers=allKmers(k)
  print(kmers)
  for kmer in kmers:
    rez[kmer]=distancePatternAndString(dna, kmer)
  print(rez)
  minimum=min(rez.values())
  for i in rez.items():
    if(i[1]==minimum):
      print(i[0])
      break
      
      
medianString(dna, k)
