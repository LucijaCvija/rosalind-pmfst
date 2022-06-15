def chromosome_to_cycle(chromosome):
  cycle = []
  for x in chromosome:
      if x > 0:
          cycle.extend([2 * x - 1, 2 * x])
      if x < 0:
          x = abs(x)
          cycle.extend([2 * x, 2 * x - 1])
  return cycle

def get_colored_edges(chromosomes):
  edges = []
  for chrom in chromosomes:
      nodes = chromosome_to_cycle(chrom)
      for j in range(1, len(nodes) - 1, 2):
          edges.append((nodes[j], nodes[j + 1]))
      edges.append((nodes[-1], nodes[0]))
  return edges

with open('/content/rosalind_ba6h.txt') as f:
    input = [x.rstrip() for x in f.readlines()]
P = input[0]
P = P[1:-1]
P = P.split(')(')
for i in range(len(P)):
    P[i] = [int(x) for x in P[i].split(' ')]
    
    
rez=get_colored_edges(P)
print(rez)
  
