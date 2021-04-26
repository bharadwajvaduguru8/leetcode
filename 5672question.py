#Python3

def check(nums):
    nums1=sorted(nums)
    #print(type(nums1))
    output=0
    nums2=list(nums1)
    #print(type(nums2))
    for a in nums1:
        #print(a)
        if nums2==nums:
            #print("hello")
            output=1
        else:
            pass
        #print("nums2",nums2)
        nums2.remove(a)
        nums2.insert(len(nums1),a)
            
    return(bool(output))


if __name__ == '__main__':
    nums = [3,4,5,1,2]
    print(check(nums))
