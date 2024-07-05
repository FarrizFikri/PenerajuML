#any/all
#builtin functions
#take boolean list as parameter
#return true if any element is true
#[True,True,False,True, False, False]
#any([True,True,False,True, False, False]) -> True
#any([False,False,False,False,False,False]) -> False
#Any True becomes True (any == or)
#Any False becomes False (any == and)
#All requires everything to be True (all == and)
#All requires everything to be False (all == or)

#check whether given number is Prime Number
givenNumber = 11
divisors = range (2,givenNumber)
# A list is given and we are going to create another list
if (len([mynumber for mynumber in divisors if (givenNumber % mynumber == 0)])==0):
    print ("Prime Number")
else:
    print ("Not a Prime Number")

if any ([givenNumber % mynumber == 0 for mynumber in divisors]):
    print ("Not a Prime Number")
else:
    print ("Prime Number")

# Prime Number
# Check whether given number is prime or not 
# check whether input is prime or not
#Generate first 10 prime numbers
# Generate prime numbers between 10 and 100
    
