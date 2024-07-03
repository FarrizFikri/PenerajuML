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
open ('fruits.txt','xt')
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
def createFile (filename):
    if not exists(filename):
        try:
            open (filename,'xt')
        except Exception as e: 
            print("Something gone wrong when creating the file", e)

filename = "fruits.txt"
createFile(filename)
