#Data Hiding is the measure of accessibility,where we specify access by public,private,protected.
#Abstract classes are the blueprint of other classes and they do have objects.
#Modules in python are codes other programmer,abstraction is from abc module so use abstraction by importing

from abc import ABC, abstractmethod
class Animal(ABC): #animal class inherits ABC
    @abstractmethod
    def make_sound(): #in abstact class we dont implement method known as abstract method so we pass it
        pass          #pass represents null value
    def sleep(self):
        print("Zzz grrr!")
class Lion(Animal):
    def make_sound(self):
        print("Roar!!!")
class Cat(Animal):
    def make_sound(self):
        print("Meow!!!")
lion = Lion()
lion.make_sound()
cat = Cat()
cat.make_sound()
lion.sleep()

