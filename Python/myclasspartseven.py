class Card:
    def __init__(self):
        pass
    def doSomething(self):
        print("Card doSomething()")

class ATMCard(Card):
    def __init__(self):
        super().__init__()
    # def doSomething(self):
    #     print("ATM Card doSomething()")

class CreditCard(Card):
    def __init__(self):
        super().__init__()
    # def doSomething(self):
    #     print("Credit Card doSomething()")
        
class DebitCard(Card):
    def __init__(self):
        super().__init__()
    # def doSomething(self):
    #     print("Debit Card doSomething()")

class BankCard(ATMCard, CreditCard, DebitCard):
    def __init__(self):
        super().__init__()
    def doSomething(self):
        #print("Bank Card doSomething()")
        super().doSomething()

bankCard = BankCard()
bankCard.doSomething()

# Method Resolution Order
print(BankCard.mro())
# <class '_main_.BankCard'>, 
# <class '_main_.ATMCard'>, 
# <class '_main_.CreditCard'>, 
# <class '_main_.DebitCard'>, 
# <class '_main_.Card'>, 
# <class 'object'>

# BIGGEST CONCLUSION:
# Every class in python is inherited from a class called object
# class object:
#   def _init_():
#       pass
#   def _str_():
#       print(memory address)

class Student:
    # def _str_(self):
    #     return "Student"
        pass
class Alumni(Student):
    # def _str_(self):
    #     return "Alumni"
    pass
    
alumni = Alumni()
print(alumni)

# Iterator object like enumeratoe, range, map, filter do not override
# _str_ method. They override _repr_ method.

#what if i dont want my class to inherit from base class called object
#definitely dont want to do because will lose all default feature of class

class myclass:
    pass

#myclass(). will list more methods
#now we understand those methods are coming the base class called object
#NO! I insist I dont want my class to inherit from object

class noObjectClass():
    pass

test = noObjectClass()
print(test)