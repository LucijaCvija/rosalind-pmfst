def StringSpelledGappedPatterns(lista,k,d):
    FirstPatterns=[]
    SecondPatterns=[]
    for i in range(0,len(lista)):
        FirstPatterns.append(lista[i][0])
        SecondPatterns.append(lista[i][1])
    PrefixString=FirstPatterns[0]
    SufixString=SecondPatterns[0]  
    for i in range(1,len(FirstPatterns)):
        PrefixString+=FirstPatterns[i][-1]      
    for i in range(1,len(SecondPatterns)):
        SufixString+=SecondPatterns[i][-1]
    for i in range(k+d+1,len(PrefixString)):
        if PrefixString[i]!=SufixString[i-k-d]:
            return "there is no string spelled by the gapped patterns"
    return PrefixString+SufixString[len(SufixString)-k-d:]
