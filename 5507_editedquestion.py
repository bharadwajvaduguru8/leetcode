#Python3

def replacea(s):
    print("1")
    import random
    import string
    letters = string.ascii_lowercase
    #print(letters)
    #result_str = ''.join(random.choice(letters) for i in range(26))
    array_for_questionmark_location=[]
    print("2")
    for i,a in enumerate(s):
        if a=='?':
            #print(str(i)+" "+a)
            array_for_questionmark_location.append(i)
    print("3")
    for c,d in enumerate(array_for_questionmark_location):
        #p=random.choice(letters)
        #s.replace(s[c],p)
        if d==0:
            print("4")
            if s[d]==s[d+1]:
                print("4.1")
                while s[d]==s[d+1]:
                    print("4.2")
                    p=random.choice(letters)
                    print("4.21")
                    s=s.replace(s[d],p)
                    print(s)
            else:
                p=random.choice(letters)
                s=s.replace(s[c],p)
                print("4.3")
                pass
            #c=c+1
            
        elif d==(len(s)-1):
            print("5")
            if s[d]==s[d-1]:
                while s[d]==s[d-1]:
                    p=random.choice(letters)
                    s=s.replace(s[d],p)
            else:
                p=random.choice(letters)
                s=s.replace(s[c],p)
                pass
            #c=c+1
        else:
            print("6")
            if s[d]==s[d+1] or s[d]==s[d-1]:
                if s[d]==s[d+1]:
                    while s[d]==s[d+1]:
                        print("6.1")
                        p=random.choice(letters)
                        s=s.replace(s[d],p)
                else:
                    while s[d]==s[d-1]:
                        print("6.2")
                        p=random.choice(letters)
                        s=s.replace(s[d],p)
            else:
                print("6.3")
                pass
            #c=c+1
    #return(array_for_questionmark_location)
    return(s)
if __name__ == '__main__':
    s=input("S:")
    print(replacea(s))
