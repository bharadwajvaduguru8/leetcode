# python3
import math
def score(s,e,q):
    count_start=0
    count=0
    for a in range(len(s)):
        if s[a]<q or s[a]==q:
            if e[a]>q or e[a]==q:
                count+=1

    return(count)   
        
if __name__ == '__main__':
    s=num=list(map(int,input("Start time: ").split()))
    e=num=list(map(int,input("Start time: ").split()))
    q=int(input("Query time:"))

    print(score(s,e,q))
