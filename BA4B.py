def get_genetic_code_codons():
    genetic_code = {
        "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F",
    }
    return genetic_code
  
  def Translation(rna_pattern):
  G=get_genetic_code_codons()
  rezultat=[]
  for i in range(0, len(rna_pattern), 3):
    slovo = G[rna_pattern[i : i + 3]]
    if(slovo == "*"):
        break
    rezultat.append(slovo)
  rezultat = "".join(rezultat)
  return rezultat

def ReverseComplement(DNApattern):
  rc=""
  for i in range(len(DNApattern)-1,-1,-1):
    if(DNApattern[i]=="A"):
      rc=rc+"T"
    elif(DNApattern[i]=="C"):
      rc=rc+"G"
    elif(DNApattern[i]=="G"):
      rc=rc+"C"
    elif(DNApattern[i]=="T"):
      rc=rc+"A"
  return rc

def substrings_encoding(dna, peptide):
    k = len(peptide) * 3
    rezultat = []
    for i in range(len(dna) - k + 1):
        substr = dna[i:i + k]
        reversecompl_substr = ReverseComplement(substr)
        substr = substr.replace("T", "U")
        reversecompl_substr = reversecompl_substr.replace("T", "U")
        if Translation(substr) == peptide or Translation(reversecompl_substr) == peptide:
            rezultat.append(substr.replace("U", "T"))
    return rezultat
  
  
rez=substrings_encoding(DNA, peptide)
for i in range(0, len(rez)):
  print(rez[i])
