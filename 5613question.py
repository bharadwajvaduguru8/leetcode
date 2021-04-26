#Python3

def rich(accounts):
    richest=0
    for i in range(0,len(accounts)):
        value=0
        for  j in range(0,len(accounts[0])):
            value+=accounts[i][j]
        if richest<value:
            richest=value
        else:
            pass
    return(richest)

if __name__ == '__main__':
    accounts = [[1,5],[7,3],[3,5]]
    print(rich(accounts))


