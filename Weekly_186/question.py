# python3
import math
def score(s):
    j=[]
    for a in range(1,len(s)):
        score1=0
        score2=0
        for z in range(0,a):
            if s[z]=="0":
                score1+=1
        for p in range(a,len(s)):
            if s[p]=="1":
                score2+=1
        score=score1+score2
        j.append(score)
    return(max(j))
        
if __name__ == '__main__':
    s=input("S = ")
    print(score(s))
