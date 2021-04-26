# python3
import math
def nums(num1):
    length_low=len(str(num1[0]))
    length_upper=len(str(num1[1]))
    num=[]
    z=[]
    for a in range(length_low,length_upper+1):
        #print(a)
        for c in range(1,11-a):
            length_low_usage=a
            inter=0
            for b in range(c,11):
                if(length_low_usage==0):
                    Z=int(inter)
                    num.append(Z)
                    #print(inter)
                    break
            
                inter=inter+b*(10**(length_low_usage-1))
                length_low_usage=length_low_usage-1
                #print(inter)
            #print("Cme to outer for loop")
    print(num)
    for p in num:
        if ((p>=num1[0])and (p<=num1[1])):
            z.append(p)
    print(z)
if __name__ == '__main__':
    #inpu=list(map(int, input("Nums: ").split()))
    num1=list(map(int,input("Num: ").split()))
    nums(num1)
