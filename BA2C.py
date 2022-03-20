def kmerProbablity(kmer, profile):
    poss = []
    rez=1
    for i in range(0,len(kmer)):
        if kmer[i] == 'A':
            poss.append(profile[0][i])
        elif kmer[i] == 'C':
            poss.append(profile[1][i])
        elif kmer[i] == 'G':
            poss.append(profile[2][i])
        elif kmer[i] == 'T':
            poss.append(profile[3][i])
    for j in range(0, len(poss)):
      rez=rez*poss[j]
    return rez
  

def BestPattern(dna, k, profile):
  bestpattern = ""
  bestprob = 0.0
  for i in range(len(dna) - k + 1):
      kmer = dna[i:i+k]
      kmerprob=kmerProbablity(kmer, profile)
      if kmerprob > bestprob:
          bestpattern = kmer
          bestprob = kmerprob
  print(bestpattern)


BestPattern(dna, k, profile)

