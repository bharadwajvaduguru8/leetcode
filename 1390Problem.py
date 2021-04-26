#Python 3
#a=[]
def divisor(a):
    #print("In divisor method")
    for j in a:
        count=0
        sum1=0
        g=int(j)
        for p in range(1,int(g+1)):
            if (g%p)==0:
                count+=1
                sum1=sum1+p
        if count==4:
            return(sum1)
if __name__=='__main__':    
    a=list(map(int,input("Please enter matrix:").split()))
    #print(a)
    print(divisor(a))
