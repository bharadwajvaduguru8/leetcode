#Python 3
nums=list(map(int, input("Input: ").split()))
a=max(nums)
nums.remove(a)
b=max(nums)
return((a-1)*(b-1))
