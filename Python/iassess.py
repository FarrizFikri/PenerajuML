# name = input ("Enter your name")
# inputstring = f"Hello {name}! Welcome to Amphi Event Management System"
# print(inputstring)

# w = int(input("Enter branding expenses"))
# x = int(input("Enter travel expenses"))
# y = float(input("Enter food expenses"))
# z = float(input("Enter logistics expenses"))

# Addition = (w + x + y + z)
# wpercent = (w/Addition)*100
# xpercent = (x/Addition)*100
# ypercent = (y/Addition)*100
# zpercent = (z/Addition)*100

# print(f"Total expenses: Rs.{Addition:.2f}")
# print(f"Branding expenses percentage:{wpercent:.2f}")
# print(f"Travel expenses percentage: {xpercent:.2f}")
# print(f"Food expenses percentage: {ypercent:.2f}")
# print(f"Logistics expenses percentage: {zpercent:.2f}")

# Get input for the total volume, desired concentration, and concentrations of the available solutions
# total_volume = float(input("Enter the total volume of the solution: "))
# desired_concentration = float(input("Enter the desired concentration (%): ")) / 100
# concentration1 = float(input("Enter the concentration of the first solution (%): ")) / 100
# concentration2 = float(input("Enter the concentration of the second solution (%): ")) / 100

# # Calculate the amount of the first solution required
# amount1 = (total_volume * desired_concentration - total_volume * concentration2) / (concentration1 - concentration2)

# # Calculate the amount of the second solution required
# amount2 = total_volume - amount1

# # Check if the required amounts are within the maximum stock
# if amount1 <= 3:
#     print("Solution (A) is available, can proceed")
# else:
#     print("Solution (A) is not available, please order", amount1 - 3, "liters now")

# if amount2 <= 3:
#     print("Solution (B) is available, can proceed")
# else:
#     print("Solution (B) is not available, please order", amount2 - 3, "liters now")

# print("Amount of the first solution required: ", amount1, "liters")
# print("Amount of the second solution required: ", amount2, "liters")

# x = float(input("Enter the total investment: "))
# y = float(input("Enter the interest rate for the first account (%): ")) / 100
# z = float(input("Enter the interest rate for the second account (%): ")) / 100
# a = float(input("Enter the total annual interest: "))

# AmountA = (a - x*z)/(y-z)

# AmountB = x - AmountA

# print("Amount invested in the first account: RM", AmountA)
# print("Amount invested in the second account: RM", AmountB)

# Totalsalary = float(input("Enter the total salary paid "))
# x= (Totalsalary - 800)/130

# weekends = x
# weekdays = x+10

# print(f"Number of weekday hours is {weekdays:.0f}")
# print(f"Number of weekend hours is {weekends:.0f}")

# show1_people = int(input("Enter the number of people who watched show 1\n"))
# show1_rating = float(input("Enter the average rating for show 1\n"))
# show2_people = int(input("Enter the number of people who watched show 2\n"))
# show2_rating = float(input("Enter the average rating for show 2\n"))
# show3_people = int(input("Enter the number of people who watched show 3\n"))
# show3_rating = float(input("Enter the average rating for show 3\n"))

# total_people = show1_people + show2_people + show3_people

# total_rating = (show1_people * show1_rating) + (show2_people * show2_rating) + (show3_people * show3_rating)

# overall_average = total_rating / total_people

# # Print the overall average rating for the show
# print(f"The overall average rating for the show is {overall_average:.2f}")

# # Get the input string from the user
# user_input = input("Enter a string: ")

# # Initialize a counter for vowels
# vowel_count = 0

# # Loop through each character in the string
# for char in user_input:
#     # Check if the character is a vowel (both lowercase and uppercase)
#     if char.lower() in 'aeiou':
#         # If it's a vowel, increment the counter
#         vowel_count += 1

# # Print the result
# print("Number of vowels in the string:", vowel_count)

# givenNumbers = range(2, 51)
# print("First 10 prime numbers are:")
# print("1")
# count = 0

# for givenNumber in givenNumbers:
#     is_prime = True
#     divisors = range(2, givenNumber)
    
#     for divisor in divisors:
#         if givenNumber % divisor == 0:
#             is_prime = False
#             break
    
#     if is_prime:
#         print(givenNumber)
#         count += 1
#         if count == 9:
#             break

# count = 0
# num = 2
# print ("First 10 prime numbers are:")
# print ("1")
# while count < 9:
#     is_prime = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)
#         count += 1
#     num += 1

# import random

# while True:
#     user_choice = int(input("Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))

#     while user_choice not in [1, 2, 3]:
#         user_choice = int(input("Invalid choice. Enter your choice (1 for Rock, 2 for Paper, 3 for Scissors): "))

#     computer_choice = random.randint(1, 3)
#     print(f"Computer chose: {'Rock' if computer_choice == 1 else 'Paper' if computer_choice == 2 else 'Scissors'}")

#     if user_choice == computer_choice:
#         print("It's a tie!")
#     elif (user_choice == 1 and computer_choice == 3) or \
#          (user_choice == 2 and computer_choice == 1) or \
#          (user_choice == 3 and computer_choice == 2):
#         print("You win!")
#     else:
#         print("Computer wins!")

#     play_again = input("Do you want to play again? (yes/no): ")
#     if play_again.lower() != "yes":
#         print("Thanks for playing!")
#         break

# Problem 7 Harmonic Series:

# Write a program that calculates the sum of the first n terms of the harmonic series. Take the n as Input.

# Hn = 1 + 1/2 + 1/3 + 1/4 .... + 1/n

n = int(input("Enter number la mat:"))
hn = 0
for i in range(1, n + 1):
    hn += 1 / i
    print("Sum of harmonic series is: ", hn)
    