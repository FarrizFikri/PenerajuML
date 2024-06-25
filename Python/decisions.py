#Write a program whether our business is making profit, loss or breakeven

expenses = 1200
sales = 1100

#Objective 1: Just say profit or not 
if (sales > expenses ):
    #block of code
    print("Yay, profit!")

# OBJECTIVE 2: Figure out profit or LOSS

if (sales>expenses):
    print ("Yay, Profit!")
else:
    print("Boo, LOSS!")

#Objective 3: Figure out Profit or LOss, or breakeven

if (sales>expenses):
    print ("Yay, Profit!")
else:
    if (sales==expenses):
        print("Okay La, Breakeven meh.")
    else:
        print("Boo, Loss!")

if (sales>expenses):
    print ("Yay, Profit!")
elif (sales==expenses):
    print("Okay La, Breakeven meh.")
else:
    print("Boo, Loss!")


print("Thank you!")

#find whether the given number is even 
givennumber = int(input("Enter Number la anjir"))
#if the statement to be executed is not a block of code
#if single statement, then we can write it the same line 
if (givennumber%2 ==0): print("Even Number")

#find whether the given number is even or odd
print ("Even Number") if (givennumber% 2 ==0) else print("Odd Number")

#find whether the given number is positive, negative or zero 
print ("+ve") if (givennumber>0) else print ("-ve")if (givennumber<0) else print ("zero")