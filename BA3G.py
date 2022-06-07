with open("/content/rosalind_ba3g (2).txt") as f:
    input1 = [x.rstrip() for x in f.readlines()]
    
    
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
 
def RebalanceGraphFromEulerianPathToCycle(graph):
    from collections import Counter
    graph = graph.copy()
    outbalance = {first: len(graph[first]) for first in graph.keys()}
    new_list = []
    for v in graph.values():
        new_list.extend(v)
    inbalance = Counter(new_list)

    all_nodes = set(list(outbalance.keys()) + list(inbalance.keys()))

    for node in all_nodes:
        balance = outbalance.get(node, 0) - inbalance.get(node, 0)
        if balance == 1:
            second = node
        if balance == -1:
            first = node

    if first not in graph:
        graph[first] = [second]
    else:
        graph[first].append(second)

    return graph, first, second
  
  
  
graph, first, second=RebalanceGraphFromEulerianPathToCycle(InputToGraph(input1))

cycle=EulerianCycle(graph)[:-1]

for i in range(len(cycle)):
        if cycle[i] == first and cycle[(i+1) % len(cycle)] == second:
            rez = cycle[i+1:] + cycle[:i+1]
print("->".join(rez))
