#Python3

def alike_strings(s):
    count=0
    vowels={"a","e","i","o","u","A","E","I","O","U"}
    for a in range(0,int(len(s)/2)):
        if s[a] in vowels:
            count+=1
            #print("count-1st loop",count)
        else:
            pass
    for b in range(int(len(s)/2),len(s)):
        if s[b] in vowels:
            count-=1
            #print("count-2nd loop",count)
        else:
            pass
    if count==0:
        return(bool(1))
    else:
        return(bool(0))

if __name__ == '__main__':
    s = "book"
    print(alike_strings(s))


