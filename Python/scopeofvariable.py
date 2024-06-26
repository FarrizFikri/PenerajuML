def add(a,b):
    #result is a local variable
    #variable created inside function
    # this variable cannot be accessed from outside the function
    result = a + b
    return result

#print (result)

#The above discussion is called scope of a variable
#Now we are at the main context is also called global context
x = 10
#variable x is created at the main context/ global context
def printX():
    #can i access the variable x created at the main context
    #inside the function context (printX)
    print("Inside the function printX:",x)

printX()

def modifyX():
    #we are trying to modify value of variable x
    #whenever you try to modify a variable the variable is
    #immediately created at the local context
    #it does not refer to the global context
    x = 15
    print("Inside the function (modifyX):",x)

modifyX()
print(x)

#If you really want a function to modify the variable in the 
#global context then the function must return the value
#which again must be assigned to global variable

def traditionalModifyX():
    x = 15
    return x

x = traditionalModifyX()
print(x)
#proper programming recommendation

#however in python we also have a short cut
#because if follow traditional method, function always return single value
#but what if we want to modify multiple variables?

def pythonModifyX():
    global x #telling python dont create x locally
    x = 25
    print("Inside the function (pythonModifyX):",x)

pythonModifyX()
print(x)

#Lets us discuss about scope of variables in function context
def simpleInterest (principle, period, rate): #outer function
    result = 0
    def printSimpleInterest(): #inner function
        temp = 0 #variable created in the inner function
        print ("Simple Interest", result) # however inner function can access the variable in outer function
        print ("Principle:", principle)
        print ("Period:", period)
        print ("Rate:", rate)
    # print(temp)
    result = (principle*period*rate)/100
    printSimpleInterest()
    return result

simpleInterest(1000,1,6)

