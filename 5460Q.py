#Python 3\
goodpairs=0
for a in range(0,len(nums)-1):
    for b in range(a,len(nums)-1):
        if nums[a]==nums[b] or nums[a]<nums[b]:
            goodpairs+=1

return(goodpairs)
