x = 7
y = 2
print("Addition:", x+y)
print("Substraction:", x-y)
print("Multiplication:",x*y)
print("Division:", x/y)
print("Quotient:", x//y)
print("Remainder:", x%y)

print("Exponent: ", 10**3)
print("What is the maximum number in a 64 bit env: ", (2**64) -1)

#Assignment Operators
x = 100
x += 1 #x = x+1
#y=mx+c
# y = x**2 + 2 + 2 * x +3

x += 2 # x = x+2
x += 5 

# x = 108
x += x+1
print (x)

x -= 1 #x =x-1
print (x)

x *= 1 # x=x*1
x /= 1 # x = x/1
x %= 1 # x = x%1
x //= 1 # x = x //1

#COMPARISON OPERATORS
myHeight = 5.2
yourHeight = 5.3
mysisterHeight = 5.2

#Let us create TRUE statement
print (yourHeight > myHeight)
print (myHeight == mysisterHeight)
print (mysisterHeight < yourHeight)
print (myHeight != yourHeight)

print (yourHeight >= myHeight) #greater than or equals
print (myHeight >= mysisterHeight) #greater than or equals

print (myHeight <= yourHeight)
print (mysisterHeight <= myHeight)

a = 21
b = 14
c = 7

print(a>b and a >c) #a is the greatest
print (c <a and c<b) # c is the smallest
print ((b >c and b <a) or (b>a and b < c))

print((a>c) ^ (a>b))       


