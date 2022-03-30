with open('rosalind_ba3e.txt') as f:
    patterns = [x.rstrip() for x in f.readlines()]
    
def DeBrujin(patterns):
  D=dict()
  for i in patterns:
    prvi=i[:len(i)-1]
    drugi=i[1:]
    if prvi not in D.keys():
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
    
    
DeBrujin(patterns)
