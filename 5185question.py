#Python3

def nums1(arr):
    p=0
    for a in range(0,len(arr)-2):
        if arr[a]%2!=0 and arr[a+1]%2!=0 and arr[a+2]%2!=0:
            p=1
        else:
            pass
    return(str(bool(p)).lower())
    
if __name__ == '__main__':
    arr=list(map(int,input("Num: ").split()))
    print(nums1(arr))
