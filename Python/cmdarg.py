#when we call python to execute our program we can pass values 
#to our program in command line which is also caled command line arguments
#Remember the arguments for function is separated by comma
#sys.argv give us a list, 
#which contains all the command line arguments
#passed to Python
#in the list, item at position 0 is program name itself
import sys

cmdarguments = sys.argv #.(dot) operator to access
#the variable which is inside module sys
print (cmdarguments)

#find the total of all the arguments
#if we know the total number of arguments we can hardcode it
#total = int(cmdarguments[1]) + int(cmdarguments[2])

#In this case, loops needed since we do not know total arguments
total = 0
for number in cmdarguments[1:]:
    total = total +int(number)
print(total)