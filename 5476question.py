#Python3

def nums1(arr,k):
    z=0
    p=0
    while(1):
        if(arr[0]>arr[1]):
            p=0
            b=arr[1]
            arr.remove(b)
            arr.append(b)
            z+=1
            if(z==k):
                return(arr[0])
            else:
                pass
                
        elif(arr[0]<arr[1]):
            z=0
            d=arr[0]
            arr.remove(d)
            arr.append(d)
            p+=1
            if(p==k):
                return(arr[0])
            else:
                pass
        else:
            pass
    return(max(p,z))
    
 
    arr=list(map(int,input("Num: ").split()))
    k=int(input("K:"))
    print(nums1(arr,k))
