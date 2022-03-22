import random
def RandKmers(dna, k):
  motifs=[]
  for linija in dna:
    rand=random.randrange(0, len(dna[1])-k+1)
    kmer=linija[rand:rand+k]
    motifs.append(kmer)
  return motifs

def Profile(motifs,pseudocounts=False):
    k = len(motifs[0])
    D = dict()
    D["A"] = [0] * k
    D["C"] = [0] * k
    D["G"] = [0] * k
    D["T"] = [0] * k

    for pattern in motifs:
        for x in enumerate(pattern):
            D[x[1]][x[0]] = D[x[1]][x[0]] + 1

    if pseudocounts:
        D["A"] = [x + 1 for x in D["A"]]
        D["C"] = [x + 1 for x in D["C"]]
        D["G"] = [x + 1 for x in D["G"]]
        D["T"] = [x + 1 for x in D["T"]]

    for i in range(0, k):
        s = D["A"][i] + D["C"][i] + D["G"][i] + D["T"][i]
        D["A"][i] = D["A"][i] / s
        D["C"][i] = D["C"][i] / s
        D["G"][i] = D["G"][i] / s
        D["T"][i] = D["T"][i] / s
    return D
  
def kmerProbablity(kmer, profile):
  p = 1
  for x in enumerate(kmer):
      p = p * profile[x[1]][x[0]]
  return p

def BestPattern(dna, k, profile):
  bestpattern = ""
  bestprob = 0.0000
  for i in range(len(dna) - k + 1):
      kmer = dna[i:i+k]
      kmerprob=kmerProbablity(kmer, profile)
      if kmerprob > bestprob:
          bestpattern = kmer
          bestprob = kmerprob
  return bestpattern

def Score(motifs):
  t = len(motifs)
  tmp = "'" + motifs[0] + "'"
  for m in motifs[1:]:
      tmp = tmp + ", '" + m + "'"
  zzip = eval("zip(" + tmp + ")")
  maxcount = []
  for x in zzip:
      As = sum([y == "A" for y in x])
      Cs = sum([y == "C" for y in x])
      Gs = sum([y == "G" for y in x])
      Ts = sum([y == "T" for y in x])
      maxcount.append(t - max(As, Cs, Gs, Ts))
  return sum(maxcount)

def RandMotifSearch(dna, k, t):
  motifs=RandKmers(dna, k)
  bestMotifs = motifs
  while(True):
    profile=Profile(motifs,pseudocounts=True)
    motifs=[]
    for i in range(0,t):
      najvjer=BestPattern(dna[i], k, profile)
      motifs.append(najvjer)
    if(Score(motifs)< Score(bestMotifs)):
      bestMotifs = motifs
    else:
      return bestMotifs
    

def RandomizedMotifSearch(dnalist, k, N=1000):
    bestmotifs = RandMotifSearch(dnalist, k,t)
    for i in range(1, N):
        motifs = RandMotifSearch(dnalist, k,t)
        if Score(motifs) < Score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs
  
  
rez=RandomizedMotifSearch(dna, k, 1000)
for i in range(0, len(rez)):
  print(rez[i])
