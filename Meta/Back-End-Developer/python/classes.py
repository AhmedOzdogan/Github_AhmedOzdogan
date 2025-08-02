class Students():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class Teachers(Students):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display(self):
        super().display()
        print(f"Subject: {self.subject}")
        
class Courses():
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher

    def display(self):
        print(f"Course Name: {self.course_name}")
        print("Teacher Details:")
        self.teacher.display()
        

student1 = Students("Alice", 20)
student1.display()

print("********")

teacher1 = Teachers("Mr. Smith", 35, "Mathematics")
teacher1.display()

print("********")

course1 = Courses("Calculus 101", teacher1)
course1.display()

from abc import ABC, abstractmethod

class AbstractCourse(ABC):
    @abstractmethod
    def course_info(self):
        pass
    
class OnlineCourse(AbstractCourse):
    def __init__(self, course_name, duration):
        self.course_name = course_name
        self.duration = duration
    
    def course_info(self):
        return f"Online Course: {self.course_name}, Duration: {self.duration}"


math = OnlineCourse("Advanced Mathematics", "3 months")


print("********************************")

class A():
    def __init__(self):
        print("Class A initialized")
    
class B(A):
    def __init__(self):
        print("Class B initialized")
        super().__init__()

class C(B):
    def __init__(self):
        print("Class C initialized")
        super().__init__()
        
print(C.mro())
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
# List of classes in the method resolution order (MRO) for class C

print(C.__mro__)
print(type(C.__mro__))

# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
# tuple of classes in the method resolution order (MRO) for class C
print(help(C))
"""
Help on class C in module __main__:

class C(B)
 |  Method resolution order:
 |      C
 |      B
 |      A
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __init__(self)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors inherited from A:
 |  __doc__
 |      str
 |  __module__
 |      __main__
 |  ----------------------------------------------------------------------
"""