def prefix(string):
    return string[:len(string)-1]
  
def suffix(string):
    return string[1:]
  
def Overlap(patterns):
  pairs={}
  for i in range(len(patterns)):
        for j in range(len(patterns)):
            if (i != j) and (suffix(patterns[i]) == prefix(patterns[j])):
                print(patterns[i] + ' -> ' + patterns[j])
              
              
              
with open('rosalind_ba3c (1).txt') as f:
  kmers = [x.rstrip() for x in f.readlines()]

Overlap(kmers)
