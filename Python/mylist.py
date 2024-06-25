#4 different builtin data structure 
#list, tuple, set and dictionary

#list uses []
#is modifiable (append,edit,delete)
#is ordered (items retain its position)
#can have duplicate values

fruits = ["apple", "orange","mango","banana", "grapes"]
#fruits is a variable assigned with multiple values
#fruits is also called object
#if anything called object, which means it is instance of class
#Jegan, John, Peter, Khairi are objects, instance of Human Class
#Jegan has eyes (2), nose(1), legs(2) => properties
#Jegan can walk can run can eat can teach => methods
print(fruits)

# Indexing and Selection
# Refer to variables part two

#Modifiable 
fruits.append("durian")
#items get added as last item
print(fruits)

#insert items inside the list
fruits.insert(1, "rambutan")
print(fruits)
fruits.insert(3,"cempedak")
print(fruits)
fruits.insert(5, "dummy")
print(fruits)

#update items in the list
fruits [5] = "mangosteen"
print(fruits)

#how to remove item from the list
fruits.remove("durian")
print(fruits)

#to remove the last item you can use method "pop"
fruits.pop()
print(fruits)

#delete an item by index 
#we can delete anything from memory permanently using keyword del
del fruits[3]
print(fruits)

greeting = "Good Morning"
print(greeting)
del greeting
# print(greeting) #this will throw error #NameError
#print ([1,2,3,4,5] + 5) #TypeError

#clear the list
fruits.clear()
print(fruits)

del fruits
#print(fruits) #NameError

fruits = ["apple", "mango","orange","mango", "apple", "banana", "grapes", "apple"]
print(fruits.index("mango"))

newfruits = fruits[2:] #0,1
print (fruits.index("mango") + 1)

#Enumerate is an iterable object
# but print do not know how to iterate the enumerate
# we can typecast the enumerate object to a list using list function
print(list(enumerate(fruits)))
#Enumerate returns list of tuple
#Each tuple has 2 items, first item is index, second item is the fruit

for item in enumerate(fruits):
    print(item[0])
    print(item[1])
    if item[1] == "mango": 
        print("mango found at index", item[0])

#you want to know how many apples in the list
print("Total number of apples:",fruits.count("apple"))

#other functions which can help us to sort the items in the list
#sort() - sort the list in ascending order
fruits.sort()
print(fruits)

#reverse() - reverse the list
fruits.reverse()
print(fruits)

#sort() - sort the list in descending order
fruits.sort(reverse=True)

for fruit in fruits:
    print(fruit)

#shallow copy
x = [10,20,30,40,50]
y = x
#y is not a copy of x, it is a reference to x
print(x)
print(y)
#both x and y are pointing to the same list
x[2]=35
print(x)
print(y)

#perform deep copy
x = [10,20,30,40,50]
y =[]
for i in x:
    y.append(i)
print("#" *40)
print(x)
print(y) 
x[2]=35
print(x)
print(y)
#now x and y are two different lists
x = [10,20,30,40,50]
y =x.copy()
print("=" *40)
print(x)
print(y) 
x[2]=35
print(x)
print(y)

#fruits is an instance of a list class
#Technically objects are created by calling the class
x = list ([15,25,35,45,55])
print(x)
# however in python to create list instead using class, we use []
x = [12,22,32,42,52]
print(x)

#to invoke or call operator we use ()
#() is used in expressions
#to invoke or call method we use . (dot operator)
#to invoke built in function print() sum() 
#to create object we call class type() int() float() list()
#to call function inside module sys.pat()
#to call method in object 'Television'.split

x = tuple(x)
print(x)
#tuple is immutable

#one last feature in list, can auto explode
#explode means 1 variable for every item in the list
fruits = ["apple","orange","mango"]
fruit01 = fruits[0]
fruit02 = fruits[1]
fruit03 = fruits[2]
#however in python, you dont need to explode manually
#python can do it for you
fruit01,fruit02,fruit03 = fruits
print(fruit01)
print(fruit02)
print(fruit03)
#python can explode list into multiple variables
#this is called unpacking