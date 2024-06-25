#How to represent binary numbers in python
# use 0b followed by the binary number
# how ever it is still an integer
ownerpermission = 0b111
print(ownerpermission)

filepermision = 0b111101001 
#owner read,write, execute
#group read, execute
#others can execute only

#in data science/ machine learning when you were given
# categorical data, must convert them to numbers
# which machine can understand,
# this itself called 'feature engineering'
# gender representation 01 for female and 10 for male 
# race representation 1000 for malay, 0100 for chinese

#this bit extraction can be done using bitwise and operator 
mask = 0b000111000
print ("{0:b}".format((filepermision & mask)>>3))
print (bin((filepermision & mask)>>3))

# in order to perform bit extraction we use bitwise & operator
#we are interested in 4,5,6 bits only 
#Mask are the data that you create to extract data you want
# Original data = 0b111101001 &
# Mask data = 0b000111000
# 4,5,6 bits extracted = 0b000101000
# shift it to right 3 times 000000101 >>3

# Original Data             111101001 |
# Mask data =               000111000
# 4,5,6 bits extracted =    111111001
# The OR operator is used to set a specific bit to 1
# Please remember there is no way to set a specific it t0 0 using OR operator
#Or operator is also used in extracting region of interest in an image

print (bin(filepermision | mask))

# Original Data             01001010 ^
# Mask data =               00101100
# 4,5,6 bits extracted =    01000110
#xor is used for encryption 
message = 0b01001010 #mycontent 'J'
key = 0b00101100 #encryption key ","
encrypted_message = message ^ key 
print(bin(encrypted_message))

decrypted_message = encrypted_message ^ key
print(bin(decrypted_message))

#1s complement 
givennumber = 5
# 5             0101
# 1s complement 1010
# 2s complement = 1s complement + 1
print (~givennumber) # ~ 1s complement
print (-givennumber) # - unary negative
print (+givennumber) # + unary positive
print (~givennumber + 1) #2s complement

hexadecimalnumber = 0xF
print(hexadecimalnumber)
print (hex(hexadecimalnumber))
octalnumber = 0o10
print(octalnumber)
print(oct(octalnumber))
