#IS - A relationship
#Alumni is a STudent
class Student:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""

#Alumni extends student class
class Alumni(Student):

    def __init__(self,firstname, lastname, alumninumber ):
        #Static caling __init__ method 
        #Student.__init__(self, firstname, lastname)
        #To create the parent object inside the child object
        #you can use keyword super()
        #which will return the object of parent class
        super().__init__(firstname, lastname)
        self.alumninumber = alumninumber 
        pass

    def __str__(self):
        return f"First Name: {self.firstname}\n \
        Last Name ; {self.lastname}\nIC Number:{self.icnumber} \
        Alumni Number: {self.alumninumber}"
    
     
#we have created an object of Alumni class
# alumni = Alumni("Asyful","Iman")
alumni = Alumni("Asyful","Iman", 97409)
print(alumni)


