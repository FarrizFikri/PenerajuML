#Methods are nothing but functions inside class
#Methods take at least 1 parameter which is self
#This parameter is used by python to pass the instance

class calculator:
    #since this method take self as parameter(istance argument)
    #it is called instance method
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    #since this method also take self as parameter(instance argument)
    # this method also called instance method
    def add(self):
        return self.num1+self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    
mycalculator = calculator(20,10)
print(mycalculator.add())
print(mycalculator.subtract())

#There is a class which has many methods but no properties
#why methods take self as a parameter? Because we want to access the properties
#which means the methods no need to take self as parameter anymore
#since no property, we no need to create objects
#these type of methods are attached to the class not the object
#these type of methods are called class methods

class utility:
    def addition(x,y):
        return x+y
    def subtraction(x,y):
        return x-y
    
print(utility.addition(10,20))

#however this can be easily done using module in python
#no need to create a class