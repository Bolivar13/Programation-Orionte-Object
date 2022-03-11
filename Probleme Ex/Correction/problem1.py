from math import*
import math
class point():
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    @property
    def x(self):
         return self.__x
    @x.setter
    def x(self,value):
        self.__x=value
    @property
    def y(self):
         return self.__y
    @x.setter
    def y(self,value):
        self.__y=value
    
    def __str__(self):
        return f"x y({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def distance (self,other):
        return math.sqrt((other.x - self.__x).pow(2) + (other.y - self.__y).pow(2)) 

    def milieu (self,other):
        mx = (self.__x + other.__x)
        my = (self.__y + other.__y)
        return point(mx , my)

    class TroiPoint():
        def __init__(self,point1, point2, point3):
            self.point1 = point1
            self.point2 = point2
            self.point3 = point3
        

 