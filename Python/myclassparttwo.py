class Student:
    #usually init method is used to declare preperties
    #difference between variables and properties
    #1) properties are nothing but variables but inside the class
    #2) properties are always prefix by the first parameter
    #3) if do not declare with prefix, it will become just a 
    #   LOCAL variable and can be accessed from anywhere

    #Some of the properties are compulsory
    #you cannot become a student without telling firstname, lastname and icnumber
    #in other words, should not allow object to be created
    #without these properties or value for compulsory
    #however program and address can be provided later (not compulsory)

    def __init__(self, firstname, lastname, icnumber):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.program = ""
        self.address = ""

    def attendClass(self):
        print(f"{self.firstname} {self.lastname} started attending class")

    def doProject(self, projectname):
        print(f"{self.firstname} {self.lastname} started doing project: {projectname}")

    def attendExam(self, exam):
        grade = "A"
        return f"{self.firstname} {self.lastname} has attended the exam: {exam} and obtained score {grade}"

    def info (self):
        print("First Name:",self.firstname)
        print("Last Name:",self.lastname)
        print("IC Number:",self.icnumber)
        #here program is local varible created inside method
        for program in self.program:
            print("Program:",program)
        print("Address:",self.address)
        print(self.address["Street"])
        print(self.address["Area"])
        print(self.address["Postcode"])
        print(self.address["State"])
        print(self.address["Country"])

    #there is also another specialmethod
    # def _str_(self)
    #which returns string value
    #this mehod will be called when you try to print the object

    def __str__ (self):
        return f"""First Name:{self.firstname}
        Last Name: {self.lastname}
        IC Number: {self.icnumber} """
     
# Creating a Student object with compulsory properties
# how to set value for properties
# 1) using constructor (__init__method)
zul = Student("Ahmad", "Zul", "980102121234")
zul.attendClass()
zul.doProject("Pokemon")
print(zul.attendExam("Python 102"))

#2) can set values to property directly using dot operator
zul.program = ["Computer Science","Data Science", "Machine Learning"]
zul.address = {
    "Street":"Jalan 1/1",
    "Area" : "SUbang Jaya 2",
    "Postcode" :  43100,
    "State" : "Selangor",
    "Country" : "Malaysia"
}
zul.info()
#default behaviour is to print the address location where the object is
#however we want to override behaviour we can do that by __str__
print(zul)
#when we try to print object
#if that class has __str__ method it will be executed automatically