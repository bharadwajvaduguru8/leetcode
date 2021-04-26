# python3
def score(sentence,searchWord):
    a=sentence.split()
    count=[]
    for b in range(0,len(a)):
        if searchWord in a[b]:
            p=min(len(searchWord),len(a[b]))
            for j in range(0,p):
                if searchWord[j] in a[b][j]:
                    count.append(b)
            
    if len(count)==0:
        return(-1)
    else:
        return(min(count))

if __name__ == '__main__':
    sentence=input("Enter an input:")
    searchWord=input("Enter an input:")
    print(score(sentence,searchWord))
