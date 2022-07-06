def cycle_to_chromosome(Nodes):
    Chromosome = []
    for i in range(0, len(Nodes), 2):
        if Nodes[i] < Nodes[i + 1]:
            Chromosome.append(Nodes[i + 1] // 2)
        else:
            Chromosome.append(-Nodes[i] // 2)
    return Chromosome
  
def graph_to_genome(GenomeGraph):
    P = []
    Cycles = []
    temp = []
    for i in range(len(GenomeGraph)):
        if i == len(GenomeGraph) - 1:
            temp += GenomeGraph[i]
            Cycles.append(temp)
        elif GenomeGraph[i][1] == GenomeGraph[i + 1][0] + 1 or GenomeGraph[i][1] == GenomeGraph[i + 1][0] - 1:
            temp += GenomeGraph[i]
        else:
            temp += GenomeGraph[i]
            Cycles.append(temp)
            temp = []
    for Cycle in Cycles:
        Chromosome = cycle_to_chromosome([Cycle[-1]] + Cycle[:-1])
        P.append(Chromosome)
    return P
  
  
with open('/content/rosalind_ba6i (1).txt') as f:
    Edges = f.readline().strip()
    Edges = Edges.split('), (')
    for i in range(len(Edges)):
        Edges[i] = Edges[i].replace("(", "").replace(")", "")
        Edges[i] = [int(x) for x in Edges[i].split(", ")]
        
result = graph_to_genome(Edges)
for j in range(len(result)):
    result[j] = '(' + ' '.join(('+' if i > 0 else '') + str(i) for i in result[j]) + ')'
print(''.join(result))
