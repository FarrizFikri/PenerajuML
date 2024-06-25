#python has a built in function called input
# the input function will display the caption and wait the user input
# user will provide input and press enter
#input is always in string data

firstNumber = input("Please key in the first number:")
print(firstNumber)
print(type(firstNumber))

secondNumber = input ("Please key in the second number:")
print(int(firstNumber)+int(secondNumber))  #concantenation because both still in string

numbers = input("Enter the numbers to do Total:")
numberlist = numbers.split(",")
print(numberlist)
total =0
for number in numberlist:
    #int function trim the string value, remove spaces in string
    #then convert string to integer
    total = total + int(number)
print(total)