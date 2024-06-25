name = "Javid"
batch = 101
fee = 1245.6578
inputstring = "Hello " + name +", welcome to Python Class " + str (batch)
print (inputstring)

#special string called f string
inputstring = f"Hello {name}, welcome to Python Class {batch}"
print(inputstring)

#how much of space is required
inputstring = f"Hello {name:40}, welcome to Python Class {batch}"
print(inputstring)

#align David to center
inputstring = f"Hello {name:^40}, welcome to Python Class {batch}"
print(inputstring)

#align David to right
inputstring = f"Hello {name:>40}, welcome to Python Class {batch}"
print(inputstring)

#can also provide padding characters
inputstring = f"Hello {name:#>40}, welcome to Python Class {batch}"
print(inputstring)

#Truncate to 3 characters
inputstring = f"Hello {name:.3}, welcome to Python Class {batch}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to Python Class {batch:10d}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to Python Class {batch:10d} in KL for RM {fee:10.2f}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to Python Class {batch:10d} in KL for RM {fee:3.2f}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to Python Class {batch:b} in KL for RM {fee:.2f}"
print(inputstring)

#Let us focus on decimal let us take 10 space
inputstring = f"Hello {name:.3}, welcome to Python Class {batch:b} in KL for RM {fee:,.2f}"
print(inputstring)







