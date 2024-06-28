# principle = 1000
# period = 1
# rate = 6
# simpleInterest = (principle*period*rate)/100
# print("Simple Interest:", simpleInterest)
'''
def calculateSimpleInterest(principle,period,rate):
    simpleInterest = (principle*period*rate)/100
    return simpleInterest

def calculateTotalAMountToBePrinted(principle, simpleInterest):
    return principle + simpleInterest

principle = 1000
period = 1
rate = 6
result = calculateSimpleInterest (principle, period, rate)
newresult = calculateTotalAMountToBePrinted (principle, result)

print("Simple Interest",result)
print("Total amount to be paid:", newresult) '''
 
#IN python we cannot declare properties (variable)
#without assigning a value
#special method (function) called constructor
#This method gets called/invoked/executed everytime 
# when create an object
#of this class (instance of this class)
#speical method must hae=ve double underscore 
#followed by init and again followed by underscore
#difference between method and function
#1) Method is nothing but a function  inside a class
#2) Methods will have at least 1 parameter
#3) You no need to pass argument for first parameter
#4) First parameter of method is very special
#5) First parameter of method is called self

class Student:
    def __init__(self):
        print("Object is created")

#lets create first object
#object is an instance of class
zul = Student()




