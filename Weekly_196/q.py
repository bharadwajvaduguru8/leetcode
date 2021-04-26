#python3
def arr():
    arr=list(map(int,input("Enter the values:").split()))
    arr.sort()
    p=0
    diff=arr[1]-arr[0]
    for a in range(0,len(arr)-1):
        if (arr[a+1]-arr[a]==diff):
            pass
        else:
            p=3
            break
    if p==3:
        return(bool(0))
    else:
        return(bool(1))


print(arr())
