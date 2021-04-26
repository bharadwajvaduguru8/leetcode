class Solution:
    def modifyString(self, s: str) -> str:
        #print("1")
        import random
        import string
        letters = string.ascii_lowercase
        #print(letters)
        #result_str = ''.join(random.choice(letters) for i in range(26))
        array_for_questionmark_location=[]
        #print("2")
        for i,a in enumerate(s):
            if a=='?':
                #print(str(i)+" "+a)
                array_for_questionmark_location.append(i)
        #print("3")
        if len(s)==1 and s[0]=='?':
            s1=list(s)
            s1[0]=random.choice(letters)
            s="".join(s1)
        else:
            for c,d in enumerate(array_for_questionmark_location):
                #p=random.choice(letters)
                #s.replace(s[c],p)
                if d==0:
                    #print("4")
                    if s[d]==s[d+1]:
                        print("4.1")
                        while s[d]==s[d+1]:
                            #print("4.2")
                            s1=list(s)
                            s1[d]=random.choice(letters)
                            s="".join(s1)
                            #print(s)
                    else:
                        s1=list(s)
                        s1[d]=random.choice(letters)
                        s="".join(s1)
                        pass
                    #c=c+1

                elif d==(len(s)-1):
                    #print("5")
                    if s[d]==s[d-1]:
                        while s[d]==s[d-1]:
                            s1=list(s)
                            s1[d]=random.choice(letters)
                            s="".join(s1)
                    else:
                        s1=list(s)
                        s1[d]=random.choice(letters)
                        s="".join(s1)
                        pass
                    #c=c+1
                else:
                    #print("6")
                    if s[d]==s[d+1] or s[d]==s[d-1]:
                        if s[d]==s[d+1]:
                            while s[d]==s[d+1]:
                                #print("6.1")
                                s1=list(s)
                                s1[d]=random.choice(letters)
                                s="".join(s1)
                        else:
                            while s[d]==s[d-1]:
                                #print("6.2")
                                s1=list(s)
                                s1[d]=random.choice(letters)
                                s="".join(s1)
                    else:
                        #print("6.3")
                        s1=list(s)
                        s1[d]=random.choice(letters)
                        s="".join(s1)
                        pass
                    #c=c+1
            #return(array_for_questionmark_location)
        return(s)
        
