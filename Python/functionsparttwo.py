#function can have inner function
def sum(a,b):
    return a+b

x = 10

# #Anonymous function assigned to a variable
# sum = def (a,b):
#     return a+b

#OUTER FUNCTION
def authenticate (username,password):
    #INNER FUNCTION
    def calculateSI(principle,period,rate):
        result = (principle*period*rate) /100
        return result
    if (username=="admin" and password == "pwd123"):
        #since CalculateSI function is inside authenticate function 
        #we can call this function here
        print("Login Successfull")
        #print ("Simple Interest:", calculateSI(1000,1,6))
        #instead of calling calculateSI
        #LET US RETURN The inner function calculateSI
        return calculateSI #address where the function is located

func = authenticate("admin","pwd123")
#now func is pointing to calculateSI function
print(func(1000,1,6)) #calling calculateSI function using func variable
#output: 60.0
# print(calculateSI(10000,5,5)) #Error because calculateSI is not
# accessible outside authenticate function 

print(authenticate("admin","pwd123")(1000,1,6))
#output: 60.0

#Anonymous function means function without name
#lambda function is an example of anonymous function
#however is ypu create a function without a name how to call them?
#we can assign anonymous function to a variable
#sum = def(a,b)
#     return a+b
# the above is not valid syntax in python, however this is every functions are 
# handled by python itself
#That means in python every function is an anonymous function
#but we assign a name to it so that we can call it later

#lambda function is a shorthand for creating a function
#def add(a,b): return a,b
#instead of def use lmambda and not require () and return keyword
#lambda arguments: expression
sum = lambda a,b,c: a+b+c
print(sum(10,20,30)) #output: 60
#lambda function is used when we need a function for a short period of time

fahrenheitvalues= [32,33,34,35,36,37,38,39,40]
def fahrenheitToCelcius (fahrenheitvalue):
    return ((fahrenheitvalue - 32) * 5/9)

celciusvalues = map(fahrenheitToCelcius, fahrenheitvalues)
print ("List of celcius values:",list(celciusvalues))

# #using lambda function
# #STep 1 = create anonymous function
# def (fahrenheitvalue): return ((fahrenheitvalue - 32) * 5/9)
# #step 2 = assign to a variable
# fahrenheitToCelcius = def (fahrenheitvalue): return ((fahrenheitvalue - 32) * 5/9)
# #step 3 = rename def to lambda
# fahrenheitToCelcius = lambda (fahrenheitvalue): return ((fahrenheitvalue - 32)*5/9)
# #step 4 : remove () at parameter and return keyword
# fahrenheitToCelcius = lambda fahrenheitvalue: ((fahrenheitvalue - 32)*5/9)

fahrenheitvalues= [32,33,34,35,36,37,38,39,40]


