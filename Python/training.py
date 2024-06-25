# # Take the price per ticket as input
# X = int(input())

# # Take the number of tickets as input
# num_tickets = int(input())

# # Determine the discount rate based on the number of tickets
# if num_tickets < 50:
#     discount = 0
# elif 50 <= num_tickets <= 100:
#     discount = 0.10
# elif 101 <= num_tickets <= 200:
#     discount = 0.20
# elif 201 <= num_tickets <= 400:
#     discount = 0.30
# elif 401 <= num_tickets <= 500:
#     discount = 0.40
# else:
#     discount = 0.50

# # Calculate the total expenses after applying the discount
# total_expenses = (X * num_tickets) * discount

# # Print the total expenses formatted to 2 decimal places
# print("{:.2f}".format(total_expenses))

# card1 = input().split()
# card2 = input().split()
# card3 = input().split()

# if card1[0] == card2[0] == card3[0] and card1[1] == card2[1] == card3[1]:
#     print("Double Bonanza")
# elif card1[0] == card2[0] == card3[0] or card1[1] == card2[1] == card3[1]:
#     print("Bonanza")
# else:
#     print("No Bonanza")

# print("Enter a string of numbers separated by commas:")
# input_string = input()

# # Convert the string to a list of numbers
# numbers = [int(num) for num in input_string.split(",")]

# # Find 3 unique numbers whose sum is 100
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         for k in range(j + 1, len(numbers)):
#             if numbers[i] + numbers[j] + numbers[k] == 100:
#                 print("The 3 unique numbers whose sum is 100 are:", numbers[i], numbers[j], numbers[k])
#                 exit()

# print("No 3 unique numbers found whose sum is 100")

n = int(input())
for i in range (1,n+1):
    for j in range (1,i+1):
        print(j, end=" ")
    print()



