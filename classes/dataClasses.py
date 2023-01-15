#method 1 to compare objects

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __eq__(self,other): 
        return self.x==other.x and self.y==other.y
    
p1=Point(1,2)
p2=Point(1,2)
print(p1 == p2)


#method 2 to compare objects
from collections import namedtuple

Point=namedtuple("Point",["x","y"])
p1=Point(x=1,y=2)
p2=Point(x=1,y=2)
print(f"{p1.x},{p2.y}")
print(p1 == p2)