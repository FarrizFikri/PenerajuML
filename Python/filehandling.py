#should not hardcode data in program as follows
#fruits = ["apple","orange","mango"]
#must keep apple, orange, mango in txt file or csv file or excel
# must write a program to read the data 
# from file and do necessary things
# other words, data must be seperated

#must create a file using python code
#use keyword open
# open ('fruits.txt')
#open built in fucntion take 2 parameters 
#have to give instruction to python if file do not exist create it
#we call extra instruction as mode
#Mode 
#1. x create the file if it does not exist
#2. t - this will be going to be a text file 
#3. b - binary file
#4. 
# open ('fruits.txt','xt')
#when run again, gets error
# import os 
# os.path.exists('filename')
# from os import path
# path.exists('filename')

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

def doMenu(filename):
    choice = -1
    while choice != 0:
        print("-----------------")
        print("|  0 - Exit     |")
        print("|  1 - List     |")
        print("|  2 - Add Menu |")
        print("|  3 - Edit Product |")
        print("-----------------")
        choice = keyboardInput(int, "Enter your choice: ", "Invalid choice")
        if choice==0:
            print("Zai Jian")
        elif choice == 1:
            printProduct(filename)
        elif choice == 2:
            addProduct(filename)
        elif choice == 3:
            editProduct(filename)

def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename,'xt')
        except Exception as e:
            print("Something went wrong when we create the file",e)
        else:
            createTitle(filename)
        finally:
            # filehandler is object
            # has may method like read, write and close
            filehandler.close()

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

def printProduct(filename):
    lines = None
    try:
        with open(filename, 'rt') as filehandler:
            lines = filehandler.readlines()
        for index,line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            
            if(index == 0):
                print(f"{"No:":5}{product:40}{quantity:>20}{price:>20}")
                print("=" * 85)
            else:
                print(f"{index:<5}{product:40}{int(quantity):>20}{float(price):>20.2f}")
    except Exception as e:
        print("Something went wrong when we read from the file", e)

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

filename = 'fruits.txt'
createFile(filename)
doMenu(filename)
# addProduct(filename)
# printProduct(filename)

# content = input ("Fruit Name: ")
# filehandler = open(filename, '')
