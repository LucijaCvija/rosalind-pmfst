def input(permutations):
  tmp = [int(x) for x in permutations[1:-1].split(" ")]
  return [0] + tmp + [len(tmp) + 1]

def n_breakpoints(permutation):
  count = 0
  for i in range(len(permutation) - 1):
    if permutation[i + 1] - permutation[i] == 1:
      count+=1
  return len(permutation) - 1 - count

n_breakpoints(input(permutations))
