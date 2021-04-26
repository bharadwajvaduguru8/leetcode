#Python3

def nums1(arr,a,b,c):
    count=0
    for q in range(0,len(arr)-2):
        for w in range(q+1,len(arr)-1):
            for e in range(w+1,len(arr)):
                if ((abs(arr[q]-arr[w])<a or abs(arr[q]-arr[w])==a)):
                    if(abs(arr[w]-arr[e])<b or abs(arr[w]-arr[e])==b):
                        if(abs(arr[q]-arr[e])<c or abs(arr[q]-arr[e])==c):
                            #print(str(arr[q])+" "+str(arr[w])+" "+str(arr[e])+" "+"good one")
                            count+=1
                        else:
                            #print(str(arr[q])+" "+str(arr[w])+" "+str(arr[e])+" "+" onebad")
                            pass
                    else:
                        pass
                else:
                    pass
    return(count)
if __name__ == '__main__':
    arr=list(map(int,input("Num: ").split()))
    a=int(input("A:"))
    b=int(input("B:"))
    c=int(input("C:"))
    print(nums1(arr,a,b,c))
