class Passport:
    def __init__(self, country, passportnumber):
        self.country = country
        self.passportnumber = passportnumber

class Customer:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = ""
        self.passport = ""