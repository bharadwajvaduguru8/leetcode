# python3
import math
def score(s):
    #print(len(s))
    len_ar=[0]*(len(s))
    for a in range(0,len(s)):
        len_ar[a]=len(s[a])
    #print("Hi")

    result=[""]*len(s)
    for b in range(0,len(s)-1):
        #print("jfhsdj")
        result[b]=max(len_ar[b:len(s)])
    print(result)

    #return(result)
        
if __name__ == '__main__':
    s=input("Enter an input:")
    sen=s.split(" ")
    print(score(sen))
