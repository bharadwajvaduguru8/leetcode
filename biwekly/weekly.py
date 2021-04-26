# python3
import math

def dates(a,b):
#d1[0],d2[0]=year
    ly={1:"31",2:"29",3:"31",4:"30",5:"31",6:"30",7:"31",8:"31",9:"30",10:"31",11:"30",12:"31"}
    nly={1:"31",2:"28",3:"31",4:"30",5:"31",6:"30",7:"31",8:"31",9:"30",10:"31",11:"30",12:"31"} 
    d1=a.split("-")
    d2=b.split("-")
#    print(int(ly[1])+int(ly[2]))
    count=0
    if(d1[0]>d2[0]):
        bigdate=d1
        smalldate=d2
    elif(d2[0]>d1[0]):
        bigdate=d2
        smalldate=d1
    while(smalldate[1]<bigdate[1] or smalldate[1]==bigdate[1]):
        if smalldate[0]%4 ==0:
            
        
if __name__ == '__main__':
    a = input("date1= ")
    b=input("date2= ")
    dates(a,b)
