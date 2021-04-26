#Python3

def countBalls(lowLimit,highLimit):
    ball_count=[0]*(highLimit+1)
    
    for a in range(lowLimit, highLimit+1):
        #print(a)
        if len(str(a))==1:
            #print("if")
            ball_count[a]+=1
        else:
            print("in else")
            p=0
            for x in str(a):
                p=int(x)+p
            ball_count[p]+=1
    return max(ball_count)


if __name__ == '__main__':
    lowLimit = 1
    highLimit =9
    print(countBalls(lowLimit, highLimit))
