#Python3

def nums1(arr):
    j=len(arr)
    i=len(arr[0])
    inde=[]
    count_final=0
    for a in range(0,j):
        for b in range(0,i):
            if arr[a][b]==1:
                inde.append(a)
                inde.append(b)
    #print(inde)
    for c in range(0,len(inde)-1,2):
        count=0
        for d in range(0,i):
            m=inde[c]
            if arr[m][d]==1:
                count+=1
        if count==1:
            count=0
            for e in range(0,j):
                n=inde[c+1]
                if arr[e][n]==1:
                    count+=1
                else:
                    pass
            if count==1:
                count_final+=1
        else:
            pass
            
    return(count_final)
        #print(inde[c])
                
if __name__ == '__main__':
    arr=[[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
    print(nums1(arr))
