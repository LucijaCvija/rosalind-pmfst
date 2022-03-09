def IndexofPattern(genome, pattern):
  for i in range(0, len(genome)-len(pattern)+1):
    rijec=genome[i:i+len(pattern)]
    if(rijec==pattern):
      print(i)
      
      
 IndexofPattern(genome, pattern)
