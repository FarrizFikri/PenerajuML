#function can have inner function
def sum(a,b):
    return a+b

x = 10

# #Anonymous function assigned to a variable
# sum = def (a,b):
#     return a+b

#OUTER FUNCTION
def authenticate (username,password):
    #INNER FUNCTION
    def calculateSI(principle,period,rate):
        result = (principle*period*rate) /100
        return result
    if (username=="admin" and password == "pwd123"):
        #since CalculateSI function is inside authenticate function 
        #we can call this function here
        print("Login Successfull")
        #print ("Simple Interest:", calculateSI(1000,1,6))
        #instead of calling calculateSI
        #LET US RETURN The inner function calculateSI
        return calculateSI #address where the function is located

func = authenticate("admin","pwd123")
#now func is pointing to calculateSI function
print(func(1000,1,6)) #calling calculateSI function using func variable
#output: 60.0
# print(calculateSI(10000,5,5)) #Error because calculateSI is not
# accessible outside authenticate function 

print(authenticate("admin","pwd123")(1000,1,6))
#output: 60.0