# python3
import math
def nums(num):
    num.sort()
    print(b)
    for a in range(1,len(num)+1):
        total1=0#For lst digits
        total2=0#For non included digits
        for b in range(len(num)-1,len(num)-1-a,-1):
            total1=total1+num[b]
        for c in range(len(num)-1-a,-1,-1):
            total2=total2+num[c]
        if(total1>total2):
            for d in range(len(num)-1,len(num)-1-a,-1):
                print(num[d],end=' ')
            break
if __name__ == '__main__':
    num=list(map(int,input("Num= ").split()))
    b=10
    nums(num)
