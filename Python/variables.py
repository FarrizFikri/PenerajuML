product = "Television" #string
# "Television" is the string value/literal. 
# Data types = number (can do arithmetic)
#string (categorical), boolean (true or false)
quantity = 2  #integer
price = 1455.25 #float
available = True #boolean value/literal
print("Product =", product)
print("Quantity =", quantity)
print("Price =", price)
print("Available =", available)

#type is another built in function that tells the type of data
#dynamically assigned
print(type(product))
print(type(quantity))
print(type(price))
print(type(available))

total = quantity * price
print ("Total:", total)

quantity = "10"
print(type(quantity))
price = "1455.5"

total = int(quantity) * float(price)
print(total)

a = "Hello"
b = "Hello"
print (id(a))
print (id(b))

#how to assign more than one value to more than one variables
#in one line of statement

x,y = 101,102
print (x)
print (y)

#also can do this
x,y = 101 + 1, 102 +1
x,y = x +1, y +1
print (x,y)

print ("50 dollar bills -",x, ",20 dollar bills - ",y)

# print =10
# print(print)
# if =10