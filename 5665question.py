#Python3

def restoreArray(adjacentPairs):
    output=[]
    for a in range(len(adjacentPairs)-1):
        for b in adjacentPairs[a]:
            if b in adjacentPairs[a+1]:
                output.append(b)
            else:
                pass
    return(output)


if __name__ == '__main__':
    adjacentPairs = [[2,1],[3,4],[3,2]]
    print(restoreArray(adjacentPairs))
