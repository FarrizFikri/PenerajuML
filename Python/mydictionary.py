#Python dictionary is called JSON in other programming language
# Javascript Object Notation (JSON)
# Dictionary also using {}
#The data is ordered
#The data is indexed by key(not by number)
#Every data is associated with key
#For example, firstname is key and Peter is the data
#Key cannot be duplicated, Data can be duplicated
#It is modifiable

foreigner={
    "firstname":"Peter",
    "lastname":"Parker",
    "passportnumber":"E4837589",
    "incometaxnumber":"SG834934",
    "pcbamount":892,
    "lastmonth":5,
    "lastyear":2024,
    "previousmonth":[(4,2024,891),(3,2024,895),(2,2024,893),(1,2024,892)],
    "addresses":{
        "office": {
            "street": "123 Main St",
            "city": "Singapore",
            },
        "home":{
            "street": "456 Home St",
            "city": "Singapore",

        }
    },
    "phone":"01111111111"
}

print("First Name:", foreigner["firstname"])
print("Last Name:", foreigner["lastname"])
print("Passport Number:", foreigner["passportnumber"])
print("Income Tax Number:", foreigner["incometaxnumber"])
print("PCB Amount:", foreigner["pcbamount"])
print("Last Month:", foreigner["lastmonth"])
print("Last Year:", foreigner["lastyear"])

# for item in foreigner["previousmonth"]:
# item will hold tuple (4,2024,891)
#tuple is auto explodable
#as long as have 3 variables, we can explode and hold 3 values
for month, year, amount in foreigner["previousmonth"]:
    print(f"Transaction: {month}-{year}, Amount:RM{amount}")

officeaddress=foreigner["addresses"]["office"]
print("Office Address:")
print("Street:", officeaddress["street"])
print("City:", officeaddress["city"])

officeaddress=foreigner["addresses"]["home"]
print("Home Address:")
print("Street:", officeaddress["street"])
print("City:", officeaddress["city"])

#you can access the street directly as follows
print("Office Address Street:", foreigner["addresses"]["office"]["street"])

#you can access the city directly as follows
print("Home Address City:", foreigner["addresses"]["home"]["city"])

#sometimes we may not know the keys
#we can use .keys() to get all keys
for key in foreigner.keys():
    #isinstance is built in function to determine type of variable 
    if isinstance(foreigner[key], list):
        for item in foreigner[key]:
            print(f"{key}: {item}")
        else:
            print(foreigner[key])

#when you use method items, you will get key, value
for key, value in foreigner.items():
    print(key,value)

print("")
#how can i modify the dictionary
#since the key car does not exists in the dict, it gets added automatically
foreigner ["car"] = {
    "brand": "Toyota",
    "model": "Camry",
    "year": 2015
}
foreigner["salary"] = 4890
print(foreigner)

#If I want to modify salary
#Since salary is already there, it modifies/updates the existing salary
foreigner["salary"] = 5000
print(foreigner)

foreigner.pop("car")
print(foreigner)
