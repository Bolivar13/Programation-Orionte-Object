from math import*
import math


class Point():
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    

@property
def x(self):
     return self.__x
@x.setter
def x(self, value):
    self.__x = value 


@property
def y(self):
     return self.__y
@y.setter
def y(self, value):
    self.__y = value 

def __str__ (self):
    return (self.x, self.y)

def __eq__(self , a):
    return self.x == a.x and self.y == a.y

def calculer_distance(self , other):
   return math.sqrt((other.x - self.__x).pow(2) +  (other.y - self.__y).pow(2))   

def calculer_milieu(self, other):
    mx = ( other.__x  + self.__x)
    my = ( other.__y  + self.__y)
    return Point (mx , my )
    

 























