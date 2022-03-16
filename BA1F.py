def Skew(genome):
  countg=0
  countc=0
  rez=[]
  index=0
  indeksi=[]
  for i in genome:
    index=index+1
    indeksi.append(index)
    if(i=="G"):
      countg=countg+1
    elif(i=="C"):
      countc=countc+1
    skew=countg-countc
    rez.append(skew)
  minimum=min(rez)
  for i in range(0,len(rez)):
    if(rez[i]==minimum):
      print(indeksi[i])
      
Skew(genome)
