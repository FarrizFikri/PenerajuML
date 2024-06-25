firstName= "Khairi"
lastName = "Abu Bakar"
fullName = firstName + " "+ lastName
print (fullName)

carPlate = "JCG"
number= 6969
carPlateNumber = carPlate + str(number)          # concantenation
print(carPlateNumber)

product = "book"
print(product*5)  #times effect
print("=" *50)

#so far we know strings are enclosed
#with single quote or double quote

#Traditonally how we handle multiline strings
#using string concantenation
#we have to introduce character \n
# the slash \ character is also called escape character
# the slash followed by t means tab key
#slash followed by r means carriage return
message =  "As I am not feeling well\n"
message = message + "I won't be able to attend the meeting.\n"
message = message + "Please proc\reed...\n"
print (message)

myfile = "c:\newfolder\table\read.txt"
print (myfile)
#we suppose to tell python to ignore the escape sequence
myfile = "c:\\newfolder\\table\\read.txt"
print (myfile)
#in python also have special string called raw string 
myfile = r"c:\newfolder\table\read.txt"
print(myfile)

#we can also use triple double quote or triple 
#single quote. used to create multiline strings
message =  """As I am not feeling well
I won't be able to attend the meeting.
Please proceed..."""
print (message)

#relationship between strings and list
#strings are nothing but list of characters
mygreeting = "Hello World"
print(mygreeting[0])
print(mygreeting[0:6])
print(mygreeting[::2])
print(mygreeting[::-1])
#how many characters in mygreeting
print(len(mygreeting))

#reverse the given number
givenNumber = 97409
print(givenNumber)
print(int(str(givenNumber)[::-1]))

#When I started this python class I said all these literals
#are objects
#"television" is a string literal/string value
#"television is also called string object"
#Objects have functions inside
product = "Television Cloths Vegetables Fruits"
print(product.split())#split takes the literal 
#assigned to variable 'product'and split them(tokenize them)
#into multiple words (separated by space)
#"Television".
#Functions inside the object is also called "Method"
#From now you must say "print is function"
#while "split is a method"


