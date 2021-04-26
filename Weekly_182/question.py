# python3
import math
def nums(num):
    dict={}
    #f=0
    for b in nums:
        for a in dict.keys:
            if(a==b):
                dict.update({a:dict[a]+1})
            else:
                dict.add(b,0)
    print(dict)
if __name__ == '__main__':
    num=list(map(int,input("Num: ").split()))
    nums(num)
