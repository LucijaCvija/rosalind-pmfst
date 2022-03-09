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

ReverseComplement(DNApattern)
