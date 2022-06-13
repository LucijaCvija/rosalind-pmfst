import sys
permutations = [x.strip("\n") for x in sys.stdin.readlines()]
helper = [int(x) for x in permutations[1:-1].split()]

def GreedySorting(helper):
    S = []
    for i in range(0, len(helper)):
        if helper[i] == i + 1:
            continue
        idx = i
        while True:
            if helper[idx] == i + 1 or helper[idx] == -1 * (i + 1):
                break
            idx += 1
        mid = [-1 * x for x in helper[i : (idx + 1)]][::-1]
        helper = helper[0:i] + mid + helper[(idx + 1) :]
        S.append(helper.copy())
        if helper[i] < 0:
            helper[i] = abs(helper[i])
            S.append(helper.copy())
    return S
  
  
  
def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"
      
      
 def rosalind_print(permutations):
    strings = []
    for perm in permutations:
        strings.append("(" + " ".join([f(x) for x in perm]) + ")")
    return "\n".join(strings)
  
  
  
rez=GreedySorting(helper)
rosalind_print(rez)
