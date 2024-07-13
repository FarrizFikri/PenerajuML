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

def addProduct(connection):
    try:
        product = keyboardInput(str, "Product: ", "Product must be string")
        description = keyboardInput(str, "Description: ", "Description must be string")
        quantity = keyboardInput(int, "Quantity: ", "Quantity must be integer")
        price = keyboardInput(float, "Price: ", "Price must be float")
        sql = f"INSERT INTO products (name,description, quantity, price) VALUES ('{product}', '{description}', {quantity}, {price})"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()

    except Exception as e:
        print("Something went wrong when we write to the file", e)

def printProduct(connection):
    SQL = f"SELECT id, name, description, quantity, price FROM products"
    cursor = connection.cursor()
    cursor.execute(SQL)
    print(f"{'Id':6s}|{'Name':20s}|{'Description':40s}|{'Quantity':20s}|{'Price':20s}")
    for id, name, description, quantity, price in cursor:
        print(f"{id:6d}|{name:20s}|{description:40s}|{quantity:20d}|{price:20.2f}")

def editProduct(connection):
    try:
        id = keyboardInput(int,"Plesase insert Product ID:", "Id must be integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()

    except:
        print("Product for this ID does not exist")
    else:
        print(f"Product : {name}\nDescription:{description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str, "Are you sure?  (y/n): ", "Please insert y or n")
        if confirm == "y":
            newproduct = keyboardInput(str, f"Product[{name}]: ", f"Product must be string")
            newdescription = keyboardInput(str, f"Description[{description}]: ", f"Description must be string")
            newquantity = keyboardInput(int, f"Quantity[{quantity}]: ", f"Quantity must integer")
            newprice = keyboardInput(float, f"Price[{price}]: ", f"Price must float")
            SQL = f"""UPDATE products SET name = '{newproduct}', description = '{newdescription}',
            quantity = {newquantity}, price = {newprice} WHERE id = {id}"""
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

def deleteProduct(connection):
    try:
        id = keyboardInput(int,"Plesase insert Product ID:", "Id must be integer")
        SQL = f"SELECT id, name, description, quantity, price FROM products WHERE id = {id}"
        cursor = connection.cursor()
        cursor.execute(SQL)
        id, name, description, quantity, price = cursor.fetchone()

    except:
        print("Product for this ID does not exist")
    else:
        print(f"Product : {name}\nDescription:{description}\nQuantity: {quantity}\nPrice: {price}")
        confirm = keyboardInput(str, "Are you sure?  (y/n): ", "Please insert y or n")
        if confirm == "y":
            SQL = f"DELETE FROM products WHERE id = {id}"
            cursor = connection.cursor()
            cursor.execute(SQL)
            connection.commit()

connection = dbConnect()
doMenu(connection)