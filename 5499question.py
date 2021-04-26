#Python3

def nums1(arr,m,k):
    value=0
    dummy_array=['']*m
    for i in range(0,m+1):
        a=arr[i]
        b=arr[i+1]
        count=0
        for d in range(0,len(arr)-1):
            if(arr[d]==a) and arr[d+1]==b:
                count+=1
        if count>=k:
            value=1
        else:
            pass
    
    return(bool(value))
    
if __name__ == '__main__':
    arr=list(map(int,input("Num: ").split()))
    m=int(input("m:"))
    k=int(input("K:"))
    print(nums1(arr,m,k))
