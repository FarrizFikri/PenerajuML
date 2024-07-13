import mysql.connector as mysql
from os.path import exists

def keyboardInput(datatype,caption, errorMessage):
    value = None
    isInvalid = True
    while (isInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False   
    return value
filename = "fruits.txt"

def doMenu(connection):
    choice = -1
    while choice != 0:
        print("-----------------")
        print("|  0 - Exit     |")
        print("|  1 - List     |")
        print("|  2 - Add Menu |")
        print("|  3 - Edit Product |")
        print("|  4 - Delete Product |")
        print("-----------------")
        choice = keyboardInput(int, "Enter your choice [0,1,2,3,4]:", "Invalid choice")
        if choice==0:
            print("Zai Jian")
        elif choice == 1:
            printProduct(connection)
        elif choice == 2:
            addProduct(connection)
        elif choice == 3:
            editProduct(connection)
        elif choice == 4:
            deleteProduct(connection)

def dbConnect():
    connection = mysql.connect(host="localhost", user="root", password = "", database = "peneraju")
    return connection 
    

# content = input("Fruit Name: ")
# filehandler = open(filename,'')

# open file using different syntax
#whenever we come out from this block,
# the resource will closed automatically
def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            # here | (pipe) is used as delimiter
            # we can use delimiter to split the line into
            # different columns
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
        print("Something went wrong when we write to the file", e)

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be integer")
        price = keyboardInput(float, "Price: ", "Price must be float")

        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we write to the file", e)

def printProduct(connection):
    SQL = f"SELECT id, name, description, quantity, price FROM products"
    cursor = connection.cursor()
    cursor.execute(SQL)
    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':20s}|{'Price':20s})")
    for id, name, description, quantity, price in cursor:
       if(index == 0):
            print(f"{id:6s}|{name:20s}|{description:40s}|{quantity:20d}|{price:20.2f}")

def editProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        print(data)

        index = keyboardInput(int,"Plesase insert line number", "Number must be integer")
        if index >= 4:
            print("You can't edit this line")
        else:
            product, quantity, price = data[index]
            print(f"{product}, {quantity}, {price}")
            confirm = keyboardInput(str, "Are you sure?  (y/n): ", "Please insert y or n")
            if confirm == "y":
                newproduct = keyboardInput(str, f"Product[{product}]: ", f"Product must be string")
                newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", f"Quantity must integer")
                newprice = keyboardInput(float, f"Price[{price}]: ", f"Price must float")
                data[index] = [newproduct, newquantity, newprice]

                newlines = []
                for prod in data:
                    line = "|".join(map(str,prod)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)

    except Exception as e:
        print("Error edit product:", e)

def deleteProduct(filename):
    try:
        lines = None
        with open(filename, "rt") as filehandler:
            lines = filehandler.readlines()
        data = []
        for line in lines:
            data.append(line.strip().split("|"))
        print(data)

        index = keyboardInput(int,"Plesase insert line number", "Number must be integer")
        if index >= 4:
            print("You can't edit this line")
        else:
            product, quantity, price = data[index]
            print(f"{product}, {quantity}, {price}")
            confirm = keyboardInput(str, "Are you sure you want to delete?  (y/n): ", "Please insert y or n")
            if confirm == "y":
                
                del data[index] 
                newlines = []

                for prod in data:
                    line = "|".join(map(str,prod)) + "\n"
                    newlines.append(line)
                newlines[-1] = newlines[-1].strip()
                with open(filename, "wt") as filehandler:
                    filehandler.writelines(newlines)

    except Exception as e:
        print("Error edit product:", e)

connection = dbConnect()
doMenu(connection)