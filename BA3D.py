def deBrujinGraph(text,k):
  D=dict()
  for i in range(0, len(text)-k+1):
    prvi=text[i:i+k-1]
    drugi=text[i+1:i+k]
    if prvi not in D:
          D[prvi] = [drugi]
    else:
        D[prvi].append(drugi)
  for x in D.items():
    forPrint=x[0]+" -> "
    for i in range(0,len(x[1])):
      if(i==len(x[1])-1):
        forPrint+=x[1][i]
      elif(i!=len(x[1])):
        forPrint+=x[1][i]+","
    print(forPrint)
    
    
deBrujinGraph(text,k)
