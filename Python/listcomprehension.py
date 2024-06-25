#deepcopy
fruits = ["apple","orange","mango","banana","grapes"]
prices = [1.60,1.20,2.20,4.80,6.20]

#for loop with some statement
for fruit in fruits:
    print(fruit)

#overseafruits = fruits) you shouldnt do this
#overseafruits = fruits.copy()
overseafruits = []
#for loop with list
for fruit in fruits:
    overseafruits.append(fruit)
print (overseafruits)

#using list comprehension
overseafruits = [fruit for fruit in fruits]
print (overseafruits)
print("="*100)

#using tuple comprehension
overseafruits = tuple(fruit for fruit in fruits)
print("Tuple of overseafruits:", overseafruits)


priceswithsst = []
for price in prices:
    priceswithsst.append(price + (price * 0.06))

print("Prices with SST:", priceswithsst)

#using list comprehension
priceswithsst= [price + (price*0.06) for price in prices]
print("Prices with SST:", priceswithsst)

#task we need to find price with sst
# you need price
# now using info above create a function

def calculateSST(price):
    priceswithsst = price + (price*0.06)
    return priceswithsst

#map function takes 2 parameters
# 1st parameter is fucntion and second parameter is list
# map function applies function to each item in list
priceswithsst = map(calculateSST, prices)
print("Prices with SST:", list(priceswithsst))

#what map does?
# inside map there is for loopwhich pulls out the price from prices 
# and pass the price to or function. Our function return the price with sst
# now map append return value inside a list
# finally once all the prices are iterated the map function return the list
def map(func,values):
    result = []
    for value in values:
        result.append(func(value))
    return result


fahrenheitvalues= [32,33,34,35,36,37,38,39,40]
celciusvalues = []
for fahrenheit in fahrenheitvalues:
    celcius = (fahrenheit - 32) * 5/9
    celciusvalues.append(celcius)
print (celciusvalues)

#using list comprehension
celciusvalues = [((fahrenheit - 32) * 5/9) for fahrenheit in fahrenheitvalues]
print (celciusvalues)

def fahrenheitToCelcius (fahrenheitvalue):
    return ((fahrenheitvalue - 32) * 5/9)

celciusvalues = map(fahrenheitToCelcius, fahrenheitvalues)
print ("List of celcius values:",list(celciusvalues))

#all the above are trying to create a new list
# number of items in both list the same
#instead of writing traditionally for loops
#we can use list comprehension

multiplesofthree = []
numbers = list(range(1,50)) #list of 50 items
for number in range (1,50):
    if (number %3 == 0):
        multiplesofthree.append(number)
print("Multiples of 3: ",multiplesofthree)

#listcomprehension
multiplesofthree = [number for number in range (1,50) if number %3 == 0]
print("Multiples of 3: ",multiplesofthree)

def findMultiplesofThree (number):
    return True if (number %3 == 0) else False

multiplesofthree= filter (findMultiplesofThree, range (1,50))
print("Multiples of 3: ",list(multiplesofthree))

numbers = [2,5,7,8,4,6,10,11,15,17,24,22]
oddnumbers =[]
for number in numbers:
    if (number %2 != 0):
        oddnumbers.append(number)

print("Odd numbers:",oddnumbers)

#listcomprehension
oddnumbers = [number for number in numbers if (number %2 != 0)]
print("Odd numbers:",oddnumbers)


def isOddNumber (number):
    return True if (number %2 != 0) else False

oddnumbers = filter (isOddNumber, numbers)
print("Odd numbers:",list(oddnumbers))
    
#all the above are trying to create a new list
# number of items in created list is less than or the same
   
sum = 0 
for number in range (1,10):
    sum = sum + number
print("Sum of numbers from 1 to 9:",sum)

mean = 0
for number in range (1,11):
    mean = mean + number
    mean = mean / 10
print("Mean of number:",mean)

#in the above examples, trying to reduce the list to a single value

#reduce is not a built in function
#it is part of functools
from functools import reduce

numbers = [1,2,3]

def findTotal(oldvalue, currentvalue):
    return oldvalue + currentvalue

print (reduce(findTotal,numbers))
#reduce applies the function to the first two elements of the list, then to the result and the
#next element, and so on, until it has processed the entire list.
#it reduces the list to a single value
#function as 1st parameter, reduce function takes list as second parameter

'''def reduce(func, numbers):
    sum = 0 #reduce is smart, initialize sum ==1 if use multiplication
    for number in numbers:
        sum = func(sum, number)
    return sum'''

def factorial(oldvalue,currentvalue):
    return oldvalue * currentvalue

print(reduce(factorial,numbers))

#initialize sum = 5
print(reduce(factorial,numbers,5))
