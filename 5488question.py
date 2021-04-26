#Python3

def nums1(n):
    arr=[" "]*(n)
    for j in range(0,n):
        arr[j]=(2*j)+1
    count=0
    l=0
    value=0
    if len(arr)%2!=0:
        for b in range(0,int(len(arr)/2)+1):
            while(arr[b]!=arr[int(len(arr)/2)]):                
                arr[b]+=1
                arr[len(arr)-1-b]-=1
                #print("Hi")
                count+=1
        #print(arr)
    else:
        for b in range(0,int(len(arr)/2)):
            o=(arr[int(len(arr)/2)]+arr[int(len(arr)/2)-1])/2
            #print("O value:"+str(o))
            while(arr[b]!=o):                
                arr[b]+=1
                arr[len(arr)-1-b]-=1
                #print("Hi")
                count+=1
    return(count)

if __name__ == '__main__':
    n=int(input("Enter the number: "))
    print(nums1(n))


'''class Solution:
    def minOperations(self, n: int) -> int:
        arr=[" "]*(n)
        for j in range(0,n):
            arr[j]=(2*j)+1
        count=0
        value=0
        if len(arr)%2!=0:
            l=(n-1)/2
            count=(l*(l+1))
        else:
            count=(n*n)/4
        return(int(count))'''
