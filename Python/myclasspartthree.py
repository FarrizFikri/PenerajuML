#Encapsulation
#Encapsulate the properties inside the class
#in other language have keyword public, private, protected
#to protect the properties

class circle:

    def __init__(self, radius):
        #change the property with single underscore
        #this makes property private
        self.__radius = 0
        if (isinstance(radius,int)):
            self.__radius = radius
        else:
            print ("radius must be integer")

    #getter method and setter method
    def getRadius(self):
        return self.__radius
    
    def setRadius(self, radius):
        if (isinstance(radius,int)):
            self.__radius = radius
        else:
            print("radius must be integer")

    radius = property(getRadius, setRadius)

    #property is a class
    #we are calling/invoking class by passing method as argument
    #please notice after getRadius no ()
    #the property class returns the property object which is assigned to a variable radius
    # other words, radius is an instance of property class
        
    
    def area(self):
        return 3.14 * self.__radius ** 2
    
    def circumference(self):
        return 2 * 3.14 * self.__radius
    
    def __str__ (self):
        return f"Radius of this circle is {self.__radius}"

mycircle = circle (20)
# print(mycircle)
# mycircle.radius = "abc"

#mycircle.radius = 30
#you are indirectly passing the value 30 to the setter method
mycircle.radius = 30
print(mycircle)
print(mycircle.area())
#indirectly passing value "abc" to the setter method
mycircle.radius = "abc"
print(mycircle)


# print(f"Area of the circle: {mycircle.area():.2f}")
# print(f"Circumference of the circle: {mycircle.circumference():.2f}")
