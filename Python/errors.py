x = 10

#Syntax error
# if (x % 2 ==0):
# print("x is even")
#IndentationError: expected an indented block after 'if' statement on line 2

#Logical Error
# if (x % 2 ==0):
#       print(f"Given Number is {x}")
# print("x is even")

#Runtime Error
principle = int(input ("Principle: "))
period = int(input ("Period:"))
rate = int(input ("Rate:"))
interest = (principle * period * rate )/100
print ("Interest Amount:", interest)

