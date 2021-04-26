#Python3

def countGoodRectangles(rectangles):
    b=[]
    for a in rectangles:
        b.append(min(a))
    maxLen=max(b)
    count=b.count(maxLen)
        
    
    
    return(count)

if __name__ == '__main__':
    rectangles = [[2,3],[3,7],[4,3],[3,7]]
    print(countGoodRectangles(rectangles))
    


