def HDistance(A, B):
    count=0
    for element in range(0,len(A)):
      if(A[element]!=B[element]):
        count=count+1
    return count
  
def neighbors(pattern, d):
	if d == 0:
		return [pattern]
	if len(pattern) == 1:
		return ['A', 'C', 'G', 'T']
	neighborhood = []
	sufneigh = neighbors(pattern[1:],d)
	for x in sufneigh:
		if HDistance(pattern[1:],x) < d:
			for y in ['A', 'C', 'G', 'T']:
				 neighborhood.append(y + x)
		else:
			neighborhood.append(pattern[0] + x)
	return neighborhood


def symbolToNumber(symbol):
	if symbol == "A":
		return 0
	if symbol == "C":
		return 1
	if symbol == "G":
		return 2
	if symbol == "T":
		return 3
  
  
def numberToSymbol(x):
	if x == 0:
		return "A"
	if x == 1:
		return "C"
	if x == 2:
		return "G"
	if x == 3:
		return "T"
  
  
def patternToNumber(pattern):
	if len(pattern) == 0:
		return 0
	return 4 * patternToNumber(pattern[0:-1]) + symbolToNumber(pattern[-1:])


def numberToPattern(x, k):
	if k == 1:
		return numberToSymbol(x)
	return numberToPattern(x // 4, k-1) + numberToSymbol(x % 4)


def motifEnumeration(dna, k, d):
	patterns = [0]*4**k
	for x in  dna:
		for i in range(len(x)-k+1):
			neighborhood = neighbors(x[i:i+k], d)
			for n in neighborhood:
				inAll = True
				for y in dna:
					inY = False
					for j in range(len(y)-k+1):
						if HDistance(n, y[j:j+k]) <= d:
							inY = True
					if not inY:
						inAll = False
				if inAll:
					patterns[patternToNumber(n)] = 1
	finalPatterns = []
	for i in range(4**k):
		if patterns[i] == 1:	
			finalPatterns.append(numberToPattern(i, k))
	return finalPatterns


rez=motifEnumeration(Dna,k,d)
for i in range(0, len(rez)):
  print(rez[i])
