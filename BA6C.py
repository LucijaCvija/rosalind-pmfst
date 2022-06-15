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

def find_next_edge(current, edges):
  if len(edges) == 0:
      return -1
  idx = 0
  while not (current[0] in edges[idx] or current[1] in edges[idx]):
      idx += 1
      if idx == len(edges):
          return -1
  return edges[idx]

def two_break_distance(P, Q):
  edgesP = get_colored_edges(P)
  edgesQ = get_colored_edges(Q)
  edges = edgesP + edgesQ
  blocks = set()
  for edge in edges:
      blocks.add(edge[0])
      blocks.add(edge[1])
  Cycles = []
  while len(edges) != 0:
      start = edges[0]
      edges.remove(edges[0])
      Cycle = [start]
      current = find_next_edge(start, edges)
      while current != -1:
          Cycle.append(current)
          edges.remove(current)
          current = find_next_edge(current, edges)
      Cycles.append(Cycle)
  return len(blocks) // 2 - len(Cycles)

with open('/content/rosalind_ba6c.txt') as f:
    input = [x.rstrip() for x in f.readlines()]
P = input[0]
P = P[1:-1]
P = P.split(')(')
for i in range(len(P)):
  P[i] = [int(x) for x in P[i].split(' ')]

Q = input[1]
Q = Q[1:-1]
Q = Q.split(')(')
for i in range(len(Q)):
  Q[i] = [int(x) for x in Q[i].split(' ')]
  
two_break_distance(P,Q)
