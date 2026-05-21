# There are 4 pillars of OOPS: Encapsulation, Abstraction, Inheritance, Polymorphism.
# Encapsulation is the wrapping of data and function into single unit. We can do data hiding.
# Data Hiding-Public(accessible everywhere inside and outside class),by default all attributes are public.
# Private(accessible only inside class),private attributes made by __publicAttribute(data mangling).
# Protected(accessible in class and subclass),protected attributes made by _publicAttribute. 
# Using getter and setter, we can access private attribute outside the class.

class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance
    def get_balance(self):
        return self.__balance
    def set_balance(self,balance):
        self.__balance=balance

acc1= BankAccount("Josh Bus",100_000)
#print(f"{acc1.name} has a balance of {acc1._balance}")By convention,will not show error with protected
#print(f"{acc1.name} has a balance of {acc1.__balance}")this will show AttributeError,use get set.
print(f"{acc1.name} has a balance of {acc1.get_balance()}") #we use getter function over here.
acc1.set_balance(50_000) #using setter function to change the balance outside class.
print(f"{acc1.name} has a balance of {acc1.get_balance()}")
#In python we can break encapsulation by accessing private attribute without getter and setter,see next line
print(f"{acc1.name} has a balance of {acc1._BankAccount__balance}") #we dont do it use get and set.
