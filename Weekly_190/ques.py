# python3
import math
def score(s,k):
    #count=0
    count1=0
    for a in range(0,len(s)-k+1):
        count=0
    
    for b in range(0,k):
        if s[b]=="a" or s[b]=="e" or s[b]=="i" or s[b]=="o" or s[b]=="u":
            count+=1
    if count1<count or count1==count:
        count1=count
    return(count1)

if __name__ == '__main__':
    s=input("Enter an input:")
    k=int(input("Enter an input:"))
    print(score(s,k))
