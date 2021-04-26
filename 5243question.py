#Python3
import collections


def tupleSameProduct(nums):
    counts=collections.Counter()
    N=len(nums)
    for index in range(N):
        for index2 in range(index):
            count[nums[index]*nums[index2]]+=1
    total=0
    for y in counts.values():
        total+=math.comb(y,2)*8
    return total

if __name__ == '__main__':
    nums = [2,3,4,6,8,12]
    print(tupleSameProduct(nums))
    


