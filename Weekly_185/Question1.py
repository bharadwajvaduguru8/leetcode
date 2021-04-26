# python3
import math
def nums(inpu):
    count_alpha=0
    count_num=0
    for j in range(0,len(inpu)):
        if inpu[j].isalpha()==True:
            count_alpha+=1
        elif inpu[j].isdigit()==True:
            count_num+=1
    letter=[]
    numbee=[]
    for j in range(0,len(inpu)):
        if inpu[j].isalpha()==True:
            letter.append(inpu[j])
        elif inpu[j].isdigit()==True:
            numbee.append(inpu[j])
    s=""
    if len(letter)==len(numbee):
        high_count=len(letter)
        low_count=len(numbee)
        for t in range(0,high_count):
            s=s+letter[t]+numbee[t]
        print(s)
    elif(len(letter)==len(numbee)+1 or len(letter)+1==len(numbee)):
        if len(letter)>len(numbee):
            high_count=len(letter)
            low_count=len(numbee)
            for t in range(0,low_count):
                s=s+letter[t]+numbee[t]
            print(s+letter[high_count-1])
        else:
            high_count=len(numbee)
            low_count=len(letter)
            for t in range(0,low_count):
                s=s+letter[t]+numbee[t]
            print(s+numbee[high_count-1])
    else:
        print('""')
        
if __name__ == '__main__':
    inpu=input("S = ")
    nums(inpu)
