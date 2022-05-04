with open('/content/rosalind_ba3f.txt') as f:
    input = [x.rstrip() for x in f.readlines()]
    
def InputToGraph(edges):
  D = {}
  for edge in edges:
    first, second = edge.split(" -> ")
    second = second.split(",")
    D[first] = second
  return D

def EulerianCycle(D):
    pocetni=list(D.keys())[0]
    trenutni=pocetni
    rezultat=[pocetni]
    while D:
        if trenutni in D:
            rezultat.append(D[trenutni][0])
            if len(D[trenutni])==1:
                del D[trenutni]
            else:
                del D[trenutni][0]
            trenutni=rezultat[-1]
        else:
            for i,elem in enumerate(rezultat):
                if elem in D:
                    novo=rezultat[i:-1]+rezultat[:i+1]
                    rezultat=novo
                    trenutni=elem
                    break           
    return rezultat
  
  
rez=EulerianCycle(InputToGraph(input))
print("->".join(rez))
