#Python3

def arrangingspaces(text):
    count=0
    c=text.split(" ")
    for a,b in enumerate(text):
        if b==" ":
            count+=1
            #print(a)
    words_list=[]
    for d in c:
        if d.isalpha()==True:
            words_list.append(d)
    if len(c)==1 or len(c)==0:
        return(text)
    elif len(c)==2:
        output=""
        g=[]
        if text[0]==" ":
            g.append(c[1])
            g.append(c[0])
            return(output.join(g))
        else:
            return(output.join(c))
    else:
        if len(words_list)==1:
            output=""
            g=[]
            for k in words_list:
                g.append(k)
                for u in range(count):
                    g.append(" ")
            return(output.join(g))
        else:
            spaces=count/(len(words_list)-1)
            final_list=[]
            count_space=0
            output=""
            for e in words_list:
                final_list.append(e)
                print(final_list)
                for f in range(int(spaces)):
                    if count_space>=count:
                        return(output.join(final_list))
                    else:
                        count_space+=1
                        final_list.append(" ")
                        #print(count_space)
            if len(c)!=len(final_list):
                for p in range(0,len(c)-len(final_list)):
                    final_list.append(" ")
                #print(final_list)
                return(output.join(final_list))

if __name__ == '__main__':
    text="xmwol ulbyf"
    print(arrangingspaces(text))
