
# ----------------------54---------------------

class Student():
    pass

harry = Student() 

marry = Student() 

# This are the instance variables 
# It can be kept anything that you want 
# By anything we mean to say that we can keep list , integer , floating point 
harry.name = "Harry"
harry.section = 23 

marry.subjects = ["hindi" , "mathematics"]

print(harry.section) 

# ----------------------55----------------------
# good practice to have the capital name of Employee

class Employee : 
    num_leaves = 10 
    pass 

harry = Employee() 
marry = Employee() 

harry.name =  "Harry" 
harry.age = 30 
harry.smile = "good" 
marry.name = "Marry" 

print(Employee.num_leaves) 
#using dict attribute 

print(harry.__dict__)
print(harry.num_leaves) 

# Instance se classs ke variable change nhi honge 

# kehne ka matlab yeh hai ki value inside the object is same for every object 

# We can change this value only by the name of class not by the name of instance 

# -------------------56-----------------------

# Self and __init__ (Constructors)
# Objects bannane mein asssani 


class Worker :   
    num_leavves = 20 
    def __init__(self , aname , asalary , arole ) : 
        self.name = aname 
        self.salary = asalary
        self.role = arole 
    
    def printdetails(self):
        return f"The name is {self.name} and the salary is {self.salary} and the role is {self.role}"

# __init__ : It takes care of all the arguments that is taken by the class defined earlier  
# This is basically a convention of PYTHON programming 

larry = Worker("Harry" , 639 , "Jadugar")   # with the help of __init__ function 



print(larry.printdetails())

print(larry.salary)

print(harry)

# Toh jo hai directly the instance variable is created by making use of __init__ function 
# OTherwise seperately kr rhe the apn 


# ---------------------------57----------------------
# class methods in python 



@classmethod
def change_numleaves(cls , newleaves) :
    cls.numleaves = newleaves 


# Employee.num_leaves(56)   _

# classmethods can be used for alternative constructors 

# Text file me data ho then we want to make the objects in a flash 

@classmethod
def from_dash(cls,string):
    params = string.split("-")
    print(params)
    return cls( params[0] , params[1] , params[2])
    # return cls(*string.split("-")) 

# split("-") : This splits the things from - 
# input is like : ROHAN-4332-INSTRUCTOR 

# then the destination is to create the object that was created earlier 

# --------------------------59----------------
# Static - methods in python 

@staticmethod 
def printgood(string) :
    print("This is good" + string )


# We can also use from instance and class , the static method 


# -----------------------60---------------------

# Abstraction and encapsulation 

# Theoritical concepts were there 




