def NumberToSymbol(broj):
  symbol=""
  if(broj==0):
    symbol=symbol+"A"
  elif(broj==1):
    symbol=symbol+"C"
  elif(broj==2):
    symbol=symbol+"G"
  elif(broj==3):
    symbol=symbol+"T"
  return symbol
  
  
def NumberToPattern(indeks, k):
  if(k==1):
    return NumberToSymbol(indeks)
  prefixindex=indeks//4
  r=indeks%4
  symbol=NumberToSymbol(r)
  Prefixpattern=NumberToPattern(prefixindex,k-1)
  return Prefixpattern + symbol
  
  
NumberToPattern(indeks, k)
