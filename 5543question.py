#Python3

def nums1(s):
    count=-1
    check=0
    if len(s)==1:
        return(-1)
    elif len(s)==2:
        if s[0]==s[1]:
            return(0)
        else:
            return(-1)
    else:
        for a in range(0,len(s)-1):
            #print(a)
            for b in range(a+1,len(s)):
                #print(b)
                if s[a]==s[b] and ((b-a) > count):
                    #print("In if")
                    check=999
                    count=b-a-1
    if check==999:
        return(count)
    else:
        return(-1)

if __name__ == '__main__':
    s=input("s= ")
    print(nums1(s))


