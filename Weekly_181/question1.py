# python3
import math
def nums(num,ind):
    #print(len(a))
    target=[1234565432999]*(len(num))
    count=0
    x=0
    for k in ind:
        p=int(k)
        if (target[p]==1234565432999):
            target[p]=num[count]
            #print("Target_inif="+str(target))
            count+=1

        else:
            for f in range(len(num)-1,p,-1):
                #print("Target_inelse="+str(target))
                x=target[f]
                target[f]=target[f-1]
                target[f-1]=x
                #print("Target_aftermove="+str(target))
            target[p]=num[count]
            count+=1
    print("Target="+str(target))
if __name__ == '__main__':
    num=list(map(int,input("Num: ").split()))
    ind=list(map(int,input("Index: ").split()))
    nums(num,ind)
for f in range(7,3,-1):
    print(f)
