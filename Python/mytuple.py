#tuple is nothing but readonly list
#tuple uses []
#is not modifiable (cannot append,edit,delete)
#is ordered (items retain its position)
#can have duplicate values
# is indexed (0,1,2,3,4)

x = (10,20,30,40,50,60,70)
print(x)
print(type(x))

#indexing and selection
print(x[0]) #10

#is not modifiable
# can delete the entir tuple using del keyword
fruits = ("apple",'orange',"apple","mango","apple")
print(fruits.count("apple"))

#tuple doesnot have many features as list
#but it is faster than list
#tuple is used when we dont want to modify the data
#tuple is used when we want to ensure data integrity
#tuple is used when we want to ensure data consistency
# takes less space

def returnFruits():
    return "apple","banana","orange"
fruits = returnFruits()
print(fruits)
print(type(fruits)) #tuple

def total(*numbers):
    print(type(numbers))
    result=0
    for num in numbers:
        result += num
    return result

print(total(10,20,30,40,50)) #150

#one last feature in tuple, can auto explode
#explode means 1 variable for every item in the tuple
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
#this is called tuple unpacking

#problem to highlight in tuple
x = (10)
print(type(x)) #int
x = (10,)
print(type(x)) #tuple
#python is confused is it tuple or expression
#so we use comma to indicate it is tuple
#python give priority for expression than tuple
#automatically 10(integer)assigned to x

