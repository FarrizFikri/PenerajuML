# age= int(input("Umur: "))
# usually_working = age >= 18 and age <= 65

# print(f"At {age}, you are usually working: {usually_working}.")

# x = int(input("Please enter your withdrawal amount: "))

# withdrawal_amount = int(input("Please enter your withdrawal amount: "))

# if withdrawal_amount % 10 != 0:
#     print("Error: Withdrawal amount must be a multiple of 10.")
# else:
#     fifty_bills = withdrawal_amount // 50
#     withdrawal_amount %= 50
#     twenty_bills = withdrawal_amount // 20
#     withdrawal_amount %= 20
#     ten_bills = withdrawal_amount // 10
#     withdrawal_amount %= 10
#     one_bills = withdrawal_amount // 1

#     print( fifty_bills, "- 50 dollar bills,", twenty_bills, "- 20 dollar bills,", ten_bills, "- 10 dollar bills,", one_bills, "- 1 dollar bills.")

# An Adam number is a number for which the square of the number and the square of 
# its reverse are themselves reverses of each other. In other words, if you take a number, 
# reverse it, square both the original number and the reversed number, and the results are 
# still reverse of each other, then the original number is called an Adam number.

x = int(input("Please put the number:"))

y = x%10
a1 = x //10

y = (y*10) + (a1)
print (y)

x2 = x**2
y2 = y**2

# kat sini number dah square
print (x2, y2)

y3 = y2%10 
a2 = y2 //10 


y3 = (y3*10) + (a2%10) #14
print (y3)

a3 = a2 // 10
y3 = (y3*10) + (a3%10) #14
print (y3)



if y3 == x2:
    print("Yay, Adam Number!")

else:
    print ("Not Adam Number.")

# a3 = y4//10 

# y5 = (y4*10) + (a3%10)
# print(y5)







# An Armstrong number (also known as a Narcissistic number or a Pluperfect number) is a number that is equal to the sum of 
# its own digits each raised to the power of the number of digits. For example, 153 is an Armstrong number 
# because 1 ** 3 + 5 ** 3 + 3 ** 3 = 153

