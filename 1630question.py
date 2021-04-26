#Python3

def arithmeticsubarrays(nums,l,r):
    output=[]
    for a in range(len(l)):
        arr=[]
        for b in range(l[a],r[a]+1):
            arr.append(nums[b])
        arr.sort()
        #print(arr)
        for c in range(len(arr)-1):
            if arr[1]-arr[0]==arr[c+1]-arr[c]:
                output_value=1
                pass
            else:
                output_value=0
                break
        output.append(bool(output_value))
    return(output)
    
if __name__ == '__main__':
    nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10]
    l = [0,1,6,4,8,7]
    r = [4,4,9,7,9,10]
    print(arithmeticsubarrays(nums,l,r))
