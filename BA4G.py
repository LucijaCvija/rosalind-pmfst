def Expand(peptides):
  novi=[]
  mass=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
  for peptide in peptides:
    for masa in mass:
      novi.append(peptide + [masa])
  return novi

def Cyclospectrum(peptide):
  masa_peptida=sum(peptide)
  niz=[0, masa_peptida]
  tmp=peptide+peptide
  for i in range(1, len(peptide)):
    for j in range(0, len(peptide)):
      sub=tmp[j:(j+i)]
      niz.append(sum(sub))
  niz.sort()
  return niz

def Score(peptide, spectrum):
  pep_spec = Cyclospectrum(peptide)
  rez = 0
  unique_masses = set(pep_spec + spectrum)
  for mass in unique_masses:
      rez += min(pep_spec.count(mass), spectrum.count(mass))
  return rez

def Cut(leaderboard, spectrum, N):
  if len(leaderboard) <= N:
      return leaderboard
  scores = {}
  for i, peptide in enumerate(leaderboard):
      scores[i] = Score(peptide, spectrum)
  sort_score=sorted(scores.values(),reverse=True)
  threshold = sort_score[N - 1]
  return [leaderboard[idx] for idx, score in scores.items() if score >= threshold]

def leaderboard_cyclopeptide_sequencing(spectrum, N):
  leaderboard = [[]]
  leader_peptide = []
  while len(leaderboard)>0:
      leaderboard = Expand(leaderboard)
      for peptide in leaderboard:
          if sum(peptide) == spectrum[-1]:
              if Score(peptide, spectrum) > Score(leader_peptide, spectrum):
                  leader_peptide = peptide
          elif sum(peptide) > spectrum[-1]:
              leaderboard = [pep for pep in leaderboard if pep != peptide]
      leaderboard = Cut(leaderboard, spectrum, N)
  return leader_peptide

with open('/content/rosalind_ba4g.txt') as f:
    input = f.read().splitlines()
N=int(input[0])
spectrum=[int(x) for x in input[1].split()]

rez=leaderboard_cyclopeptide_sequencing(spectrum,N)
print("-".join(map(str, rez)))
