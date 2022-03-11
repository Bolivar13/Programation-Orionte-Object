from math import *
#Constrepteur

class  Point ():
  



  def __init__(self, x , y):  
     self.x = x
     self.y = y 
     
 

  def __add__(self, a):
      return  Point(self.x + a.x , self.y + a.y )

  def __supp__ (self , a ):
      return   Point( self.x - a.x ,  self.y - a.y )

  def __equal__ (self , a ):
      return   self.x == a.x ,  self.y == a.x 
  
if __name__ == '__main__' :
    p1 = Point (20, 100)
    p2 = Point (20, 100)
    print(p1 == p2)






