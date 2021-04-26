#Python3

def most_competetive_subsequence(nums,k):
    output=[]*k
    for a in range(0,k):
        output.append(min(nums))
        #print("Hi")
        for b in range(0,nums.index(min(nums))+1):
            #print("InHi")
            nums.remove(nums[b])
            print("nums=",nums)
            print("output=",output)
    return(output)

if __name__ == '__main__':
    nums = [3,5,2,6]
    k = 2
    print(most_competetive_subsequence(nums,k))


