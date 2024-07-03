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

# if exists ('filename'):
#     pass
# else:
#     open ('fruits.txt','xt')
def keyboardInput(datatype, caption,errorMessage):
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

def createFile (filename):
    if not exists(filename):
        try:
            #open built in function open file and return the handler
        #which we can use to read/write inside file
        # file handler is an object/ instance of File Class
            filehandler = open (filename,'xt')
        except Exception as e: 
            print("Something gone wrong when creating the file", e)
        else:
            createTitle (filename)
        finally:
            #filehandler has many methods like read,write and close
            filehandler.close()

#whenever come out with block the resource will close automatic
def createTitle (filename): 
    try:
        with open(filename,'wt') as filehandler:
            #here | pipe is used as delimiter
            #we can use delimiter to split the line into 
            #multiple data
            #Television201455.55"
            #Television2|20|1455.55
            filehandler.write("Product|Quantity|Price")

    except Exception as e: 
        print("Something gone wrong when creating the header", e)

def addProduct(filename):
    try:
        product = keyboardInput (str, "Product:", "Product must be string")
        quantity = keyboardInput (int, "Quantity:", "Quantity must be int")
        price = keyboardInput (float,"Price:", "Price must be float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
 
    except Exception as e: 
        print("Something gone wrong when appending the product", e)

def printProduct(filename):
    try:
        lines = None
        with open(filename, 'rt') as filehandler:
            lines = filehandler.readlines()
        for index, line in enumerate(lines):
            product, quantity, price = line.strip().split("|")
            if (index ==0):
                print(f"{product:40}{quantity:>20}{price:>20}")
                print("=" * 80)
            else:
                print(f"{product:40}{int(quantity):>20}{float(price):>20.2f}")


    except Exception as e: 
        print("Something gone wrong when we print the products", e)


filename = "fruits.txt"
createFile(filename)
addProduct(filename)
printProduct(filename)



# content = input ("Fruit Name: ")
# filehandler = open(filename, '')
