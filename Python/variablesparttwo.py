#Now we are going to learn how to assign multiple values
# to a single variable
# We want to go shopping
# We already have list of items to buy in mind
#We want to buy 10 items, doesnt mean we are going to create 
# 10 variables and assign each item to each variable
# new data structure called 'list'
# other language called array
#fruit = "apple"
#fruit1,fruit2 = "apple", "orange"

fruits = ["apple", "orange", "banana", "grape", "mango"]
print (fruits)

#indexing and selection
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
print(fruits[4])

#how many items are there in the list
#built in function len
print("Number of items in the list:", len(fruits))

#max index that we can have
print("Maximum index:", len(fruits)-1)

#does the index has to be positive number?
#Not necessary it can even be negative number
print(fruits[-1]) #last item in the list
print(fruits[-2])
print(fruits[-3])
print(fruits[-4])
print(fruits[-5])
#retrieve values in reverse order

#Range start_index:end_index
#In python when we refer to Range, end_index is not included
print (fruits[1:3])
print (fruits[1:4])
print (fruits [:4]) 
# dont mention the start index, it will take start index 0
print(fruits[0:])
# never mention end index, it will retrieve until last
fruits = ["apple", "orange", "banana","cempedak", "grape", "mango", "rambutan", "durian", "manggis"]
#since want to include all, we can use 9 as end index eventhough maximum index is 8
print(fruits[0:9])
#Only want items in even position
print(fruits[0:9:2])
print(fruits[0:9:3]) #feature is important for us to take samples
#range also can have negative numbers
print(fruits[-5:-1])
print(fruits[-1:-5]) #-1 >-5 start index is greater than end index result is empty list
#due to default step up is 1-1 +1
print(fruits[-1:-5:-1])
#which means reverse the entire list
print(fruits[::-1])

