def Expand(peptides):
  novi=[]
  mass=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
  for peptide in peptides:
    for masa in mass:
      novi.append(peptide + [masa])
  return novi

def Consistent(peptide, Spectrum):
  teorijski_spektar=[0, sum(peptide)]
  for i in range(1, len(peptide)):
    for j in range(0, len(peptide)-i+1):
      sub=peptide[j:(j+1)]
      teorijski_spektar.append(sum(sub))
  rez=[]
  for element in teorijski_spektar:
    if element in Spectrum:
      rez.append(True)
    else:
      rez.append(False)
  return rez

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

def CyclopepSeq(Spectrum):
  result = []
  peptides = [[]]
  while len(peptides)>0:
      peptides=Expand(peptides)
      for peptide in peptides:
          if sum(peptide)==Spectrum[-1]:
              if Cyclospectrum(peptide)==Spectrum:
                  result.append(peptide)
              peptides=[p for p in peptides if p!=peptide]
          elif False in Consistent(peptide, Spectrum):
              peptides=[p for p in peptides if p!=peptide]
  return result

with open('/content/rosalind_ba4e.txt') as f:
  spectrum = [int(x) for x in f.readline().strip().split()]
  
rez=CyclopepSeq(spectrum)
for element in rez:
  print("-".join(map(str, element)),end=" ")
