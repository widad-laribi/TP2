#!/usr/bin/env python
# -*- coding: utf-8 -*-
#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Factory.html
# A simple static factory method.
import sys
class Shape():
    def __init__(self,):
        pass
class ShapeFactory_SCT:
 @staticmethod
 def createShape(type):
   if type == "Circle": return Circle()
   elif type == "Square": return Square()
   elif type == "triangle": return triangle()
   else:
      print ("Bad shape creation: " + type)
      sys.exit()
      
class ShapeFactory_SCR:
 @staticmethod
 def createShape(type):
   if type == "Circle": return Circle()
   elif type == "Square": return Square()
   elif type == "rectangle": return rectangle()
   #else:
      #print ("Bad shape creation: " + type)
   sys.exit()
      
class Circle(Shape):
 def draw(self): print("Circle.draw")
 def erase(self): print("Circle.erase")
 
class Square(Shape):
 def draw(self): print("Square.draw")
 def erase(self): print("Square.erase")
 
class  triangle(Shape):
 def draw(self): print("Triangle.draw")
 def erase(self): print("Triangle.erase")
 
class  rectangle(Shape):
 def draw(self): print("Rectangle.draw")
 def erase(self): print("Rectangle.erase")
if __name__ == "__main__":
 for type in ("Circle", "Square", "triangle"):
   #shape = ShapeFactory_SCR.createShape(type)
   shape = ShapeFactory_SCT.createShape(type)
   shape.draw()
   shape.erase()
   

    
   
 


  
  
