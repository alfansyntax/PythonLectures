# Class is a blueprint where we can store two things-properties which are the variables known as the ATTRIBUTES.Another thing is the behavior
# like for student object there is a function used to calculate cgpa so this is known as the METHODS.
# In every class there exist _init_Method which is called also CONSTRUCTOR. It is used to initialise our object. If we do not make init method 
# Python itself creates the init method.
# In Java we can write multiple constructor but in python we can only write one per class.
# There are two types of attributes- class(belongs to class which means all object will have this in common) and instance(belong to object).
# Methods are three types instance,class and static.
class Student:
    uni = "North South University" # class attributes, all objects have this common
    PI = 3.142
    def __init__(self,name,cgpa):
        self.name=name
        self.cgpa=cgpa # instance attributes, different for objects
        self.PI=3.1
    def get_info(self):  #instance method(always has first parameter self and can access both class and instance attributes)
        print(f"{self.name} from {self.uni} has cgpa of {self.cgpa}")
    @classmethod  #this is decorator which makes instance class to class class. If decorator was not written u can access instance attributes
    def get_uni(cls): #but bcuz of decorator it will show error
        print(f"The university is {cls.uni} ")
    @staticmethod  #another decorator,static has no connection with attributes this is normal function but as we write in class so 
    def calc_fee(credit,price): #have to make it static
        fee=credit*price
        print(f"Semester fee is {fee}")
s1 = Student("Alfan",3.41)
print(s1.name)
print(Student.uni) # objects has higher priority so object can call both class&instance but classes can call only class attributes
print(s1.PI) # Both class and instance had PI so when PI is called from object it will give the value of instance 
print(Student.PI)   #when class called then give class value """
s1.get_info()     # Just object can call it not class
Student.get_uni() # Both class and object can call class method
s1.calc_fee(3,6500)
