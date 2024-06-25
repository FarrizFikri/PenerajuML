#Whenever you want to iterate a list of items then you must use for loop
fruits = ["apple", "orange", "banana","cempedak", "grape", "mango", "rambutan", "durian", "manggis"]
#print all items in the list
for fruit in fruits:
    print (fruit)

print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

#print all items in the even position
for fruit in fruits[::2]:
    print (fruit)

print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
#print fruits with 6 letters
for fruit in fruits:
    if (len(fruit)==6):
        print(fruit)

#print each fruit with its index
position = 0
for fruit in fruits:
    print(position, fruit)
    position +=1

#I want to create the multiplication table of 5 
#I want to go until 12
multipliers = [1,2,3,4,5,6,7,8,9,10,11,12]
multiplicant = 5
for multiplier in multipliers:
    print(multiplier, "x", multiplicant, "=", multiplier*multiplicant)

#this is not practical when until 200, we have to for 
#range option start_index:end_index
#but the : operator can work only on array
#we use built in function called range to generate list of numbers
#range fx takes start index and end index
#start index included - but end index is not included
print(range(1,12))
#range is an iterable object, which means we can use it 
#in for loop together with "int" operator
#however, print fx do not understand how to iterate them
#so it prints as range (1,12)
#any iterable object can be typecast to list using list function
#print fx knows how to iterate the list
print(list(range(1,12)))
#range function does not include 12

multiplicant = 6
for multiplier in range (1,20):
    print(multiplier, "x", multiplicant, "=", multiplier*multiplicant)

#split the digit from input and print them
#EX user input 97409
#take input, print 9,7,4,0,9
#since do not have it as a list and also dont know number of digits
#we have to use while loop

givenNumber = 97409
while (givenNumber >0):
    print(givenNumber%10)
    #givenNumber //=10
    givenNumber = givenNumber //10

givenNumber = 97409
numberofdigit = len(str(givenNumber)) - 1
while (givenNumber >0):
    print(givenNumber//10**numberofdigit)
    givenNumber %=10**numberofdigit
    numberofdigit -=1

givenNumber = 67891
strGivenNumber = str(givenNumber)
for digit in strGivenNumber:
    print(digit)

#for loop and while loop can have else block
fruits = ["apple","orange","mango","banana","grapes"]
for fruit in fruits:
    print (fruit)
    #since we add condition not it sees mango
    #jumps out of loop (iteration not exhausted)
    #code in ekse block not executed
    if (fruit == 'mango'): break
else:
    print("Setel bai print Fruits")

#code in else block gets executed only when condition fails
multiplicant = 6
multiplier = 1
while (multiplier <=12):
    print(multiplier, "x", multiplicant, "=", multiplier*multiplicant)
    multiplier +=1 
    if multiplier == 11: break
else:
    print("Multiplication table",multiplicant,"done")

#19June2024
#please do not print when the multipliers are multiples of 5

multiplicant = 7
multipliers = range (1,13)
for multiplier in multipliers:
    if multiplier % 5 == 0: continue 
    #continue keyword will do is without executing the following line
    #it will jump back to the loop
    print(multiplier, "x", multiplicant, "=", multiplier*multiplicant)






