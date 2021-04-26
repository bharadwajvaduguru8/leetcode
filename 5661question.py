#Python3

def maximumTime(time):
    hours=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
    minutes=[]
    for a in range(0,60):
        minutes.append(a)
    time1=time.split(":")
    if time1[0]=="??":
        time1[0]='23'
    elif time1[1]=="??":
        time1[0]='59'
    elif time1[0]=='??' and time1[1]=='??':
        time1[0]='23'
        time1[1]='59'
    else:
        for z in range(9,-1,-1):
            c=time1[0].replace("?",str(z))
           # print("c=",c)
            if int(c) in hours:
                time1[0]=c
    #            print(c)
                break
            else:
                pass
        for z in range(9,-1,-1):
            c=time1[1].replace("?",str(z))
            if int(c) in minutes:
                time1[1]=c
                break
            else:
                pass
    return(time1[0]+":"+time1[1])
    print(time1)


if __name__ == '__main__':
    time = "2?:?0"
    print(maximumTime(time))
