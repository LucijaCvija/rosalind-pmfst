def CountPattern(text, pattern):
  count=0
  for i in range(0,len(text)-len(pattern)+1):
    rijec=text[i:i+len(pattern)]
    if(rijec==pattern):
      count=count+1
  return count


CountPattern(text, pattern)
