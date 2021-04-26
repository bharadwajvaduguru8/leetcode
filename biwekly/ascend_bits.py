# python3
import math
def ascend(arr):
    assert 1 <= len(arr) <= 500 #and 0 <= arr[i] <= 10^4
    bina=[0]*(len(arr))
    for j in range(0,len(arr)):
        p=format(arr[j],"b")
        bina[j]=p
        setBits = [ones for ones in bina if ones=='1']
        print(len(setBits))
    print(arr)
    print(bina)
if __name__ == '__main__':
    arr = list(map(int,input().split(" ")))
    print(ascend(arr))
