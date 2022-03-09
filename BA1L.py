def SymbolToNumber(symbol):
  broj=0
  if(symbol=="A"):
    broj=broj+0
  elif(symbol=="C"):
    broj=broj+1
  elif(symbol=="G"):
    broj=broj+2
  elif(symbol=="T"):
    broj=broj+3
  return broj


def PatternToNumber(pattern):
  if(pattern==""):
    return 0
  elif(pattern!=""):
    symbol=pattern[len(pattern)-1]
    prefix=pattern[0:len(pattern)-1]
  return 4*PatternToNumber(prefix)+ SymbolToNumber(symbol)
  
  
  
PatternToNumber(pattern)
