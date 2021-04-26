#Python3

def slowestkey(releaseTimes,keysPressed):
    key_duration=[""]*len(keysPressed)
    key_duration[0]=releaseTimes[0]-0
    for a in range(1,len(releaseTimes)):
        key_duration[a]=releaseTimes[a]-releaseTimes[a-1]
    array_duplicates=[]

    for b in range(0,len(key_duration)):
        if key_duration[b]==max(key_duration):
            array_duplicates.append(keysPressed[b])
    #array_duplicates=array_duplicates.sort
    return(max(array_duplicates))        
    
if __name__ == '__main__':
    releaseTimes=[9,29,49,50]
    keysPressed="cbcd"
    print(slowestkey(releaseTimes,keysPressed))
