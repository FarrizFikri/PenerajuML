#Fx are not for solving problems like operators if,for,while
#Fx are used to organize our code
#When to create our own FX?
#Whenevr you copy & paste a block of code
#then already know it has to be a function

def sayHelloWorld():
    print("Hello World !!!")

# FX created using keyword def
# followed by function name
# which is again followed by parentheses ()
# followed by colon :
# place your block of code inside function with indentation

#Calling a FX
#what will happen if never call/invoke the FX
#nothing happens
#how to call Fx
#function name followed by parentheses ()

sayHelloWorld()

#when we create a FX if that fx takes some value
#create a variable (placeholder) in between brackets
#if the FX takes more than 1 value, we must create
#more than 1 variables (placeholders) seperated bycomma
#these variables is called "parameter"
def greeting(name):
    print("Good morning", name)

#when we call fx since fx is taking parameter
#we must pass value to parameter(s)
#the value we are passing is called argument
#the number of argument(s) must match with parameter(s)
greeting ("Jegan")

def total(x,y,z):
    result = x + y +z 
    print ("Result", result)

total (10,20,30)
#arguments are positional

#we ask him to buy, after buy he give back to us
# to identify price for food and return prices
def buyLunch (makan, minum):
    prices = [] #empty list
    for food in makan:
        if (food == "nasi"):
            prices.append (2.80)
        elif (food == "sayur"):
            prices.append (2.20)
        
    for drink in minum:
        if (drink == "nescafe"):
            prices.append (2.50)
        elif (drink == "air kosong"):
            prices.append (0.80)

    #print (prices)
    return prices

#now calculate the amount to be paid
#unless the function return / give youback the receipt
#there is no way for us to find the amount to be paid
#since buyLunch function is returning some value
#it becomes compulsory for us to hold the value
#we must declare the placeholder

itemprices = buyLunch (["nasi", "sayur"],["nescafe", "air kosong"])
total = 0
for prices in itemprices:
    total = total + prices
print("Amount to be paid:", total)

def simpleInterest(principle, period,rate):
    interest = (principle * rate * period) / 100
    return interest

print("Interest amount:",simpleInterest(1000,1,6))

#however when return value more than one seperated by comma,
#it will be a tuple (tuple is nothing but readonly list)
def participantList (nameone, nametwo, namethree):
    nameone = nameone + "Data Science"
    nametwo = nametwo + "Data Science"
    namethree = namethree + "Data Science"
    return [nameone, nametwo, namethree]

result = participantList("John","Peter","Parker")
print(type(result))

#can also make the rate parameter optional by having a default value
def calculateSimpleInterest(principle, period =1,rate = 6):
    interest = (principle * rate * period) / 100
    return interest

#since we are not passing the value of rate parameter
#rate automatically 6

print(calculateSimpleInterest(1000))
#now 2nd argument is passed meaning period = 2 and rate is 6
#which means arguments still positional 
print(calculateSimpleInterest(1000, 2))

#is there way to pass values for only principle and rate only
#we use named arguments/keyword arguments
#here te name is referring to parameter
print(calculateSimpleInterest(principle=1000, rate = 5))

def findTotal (givenNumbers):
    total = 0
    for numbers in givenNumbers:
        total = total + numbers
    return total 

#Variable length arguments
#the number of arguments which we pass vary
#the caller can pass the values as a list
print(findTotal([10,20,30]))
print(findTotal([10,20,30,40,50,60]))

#but there are use cases where caller is not able to place the values
#inside the list and pass the list
# can declare parameter to be able to accept any number
# introducing * infront of parameter
# python will take all arguments place them inside a list
# and pass the list to FX

def findTotal (*givenNumbers):
    total = 0
    for numbers in givenNumbers:
        total = total + numbers
    return total 

print(findTotal(10,20,30))
print(findTotal(10,20,30,40,50,60))

def listSixLetterFruits(*fruits):
    for fruit in fruits:
        if len(fruit) == 6:
            print(fruit)

#we are sending the item individually not as a list
#however python will convert them to list of fruits and pass it
listSixLetterFruits("apple", "orange", "mango", "banana", "durian", "grapes")

def listFruitDetails(*fruits):
    for fruit in fruits:
        print(fruit)

listFruitDetails("apple", 20, 1.40, "orange",40,1.20)

def sum (a,b):
    return a+b

def minus (a,b):
    return a-b

'''def arithmetic (keyword,a,b):
    if keyword == "s":
        return sum(a,b)
    elif keyword == "m":
        return minus(a,b) '''
    
def arithmetic (func,a,b):
    return func(a,b)

print(arithmetic(sum,10,20))
print(arithmetic(minus,10,20))

def mul (a,b):
    return a*b

print(arithmetic(mul,10,20))

    
# print(arithmetic("s",10,20))
# print(arithmetic("m",10,20))


    