#First Method
import mymodule
print("Interest:", mymodule.simpleInterest(1000,1,6))

#Second method
#better because dont need to type module name everytime
from mymodule import simpleInterest
print("Interest:", simpleInterest(1000,1,6))



