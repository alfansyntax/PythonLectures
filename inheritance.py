#Inheritance is where one class(child) acquires the properties and behaviors of another class(parent).
#Single Level Inheritance: A child inherits from one parent(parent>child)
#Multi Level Inheritance: A child inherits from a parent and another class inherits from the child(grandparent>parent>child)
#Multiple Inheritance: A child inherits from more than one parent class.(mom and dad>child).
#super() keyword -Used to call parent class’s method from child class.

class Employee:                # Parent/Base/Superclass
    start_time="10am"
    end_time="6pm"
    def __init__(self,name):
        self.name=name
class Teacher(Employee):       # Child/Derived/Subclass
    def __init__(self,name,subject):
        self.subject=subject
        super().__init__(name) #Using super() keyword we invokde/call the constructor of the parent class
class Assistant(Teacher):
    def __init__(self,salary,subject,name):
        self.salary=salary
        super().__init__(name,subject) #child does not need super for grandparent.  
class Student:
    def __init__(self,cg):
        self.cg=cg
class CR(Employee,Student):
    def __init__(self,mark,name,cg):
        self.mark=mark
        super().__init__(name) #child with multiple parents can have super for only parent that is in the
        Student.__init__(self,cg) #beginning of parameter, rest call with parent name
t1 = Teacher("Alfan","Math")
print(f"{t1.name} starts at {t1.start_time} teaches {t1.subject} and ends at {t1.end_time}.")
# If you want to have a private attribute and want to have it in your subclass so make it protected.
t2 = Assistant(25_000,"Physics","Rifat")
print(f"{t2.name} of salary {t2.salary} teaches {t2.subject}.")
t3 = CR(68,"John",3.41)
print(f"{t3.name} of marks {t3.mark} has cg of {t3.cg}.")

