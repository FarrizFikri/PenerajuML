#set uses {}
#is modifiable (add,edit,delete)
#is unordered (items does not retain its position)
# is not indexed (0,1,2,3,4)
#set does not allow dupicates

#in python, this is first time {}
x = {10,20,30,10,40,50,20,60,70}
print(x)
#what do you observe
#it removes duplicates and unordered

#Selection and Indexing
#set does not support indexing and slicing
#x[0] #TypeError: 'set' object does not support indexing
#x[0:3] #TypeError: 'set' object does not support indexing  

#to retrieve items inside the set
#only way is to use for loop
for item in x:
    print(item)

#modifiable 
fruits = {"apple","orange","mango"}
print(fruits) 
fruits.add("durian") #add random place
print(fruits)

#to delete an item in the set
fruits.remove("orange") #if item not found, it will raise error
print(fruits)

#pop = randomly removes item in set
fruits.pop()
print(fruits)

fruits = {"apple","orange","apple", "mango","banana","apple"}
uniquefruits = set(fruits)
print(uniquefruits)

overseafruits = {"apple","orange","mango","banana","grapes"}
localfruits = {"durian","rambutan","cempedak", "banana","mangosteen"}
print(overseafruits.union(localfruits))
print(overseafruits.intersection(localfruits))
print(overseafruits.difference(localfruits)) #overseafruits - localfr
print(localfruits.difference(overseafruits))
print(overseafruits.symmetric_difference(localfruits)) #overseafruits ^ localfr

favoritefruits = {"durian","rambutan","mangosteen"}
print(favoritefruits.issubset(localfruits)) #favoritefruits is subset of
print(localfruits.issuperset(favoritefruits)) #localfruits is superset
print(favoritefruits.isdisjoint(overseafruits))

emailcontent = '''A shocking proportion of email traffic—about 49 percent according to 2022 data—is spam. 
Much of that spam is purposely crafted for fraudulent purposes, to compromise communication, 
and gain access to data, networks, or funds.Many spam filtering programs identify spam messages 
before they reach human readers. Many more seem obviously fishy and are easy to delete when they 
reach your inbox. But what about those outlier messages that are hard for both software and people to detect?
Based on the latest 2022 Gone Phishing Tournament results, in an organization of 10,000 or more employees,
690 are likely to click on a phishing email link. For small businesses, this translates to 3 or 4 individuals
falling for the “phish” and giving out confidential information. For businesses, those actions by a small
minority of employees can cause maximum damage.Being able to consistently detect and avoid phishing emails
that arrive in your inbox or appear on your smartphone is a key component of strong cyber security. 
To do that, it's important to be aware of different types of phishing emails and 
stay attentive to the warning signs in every possible scenario.'''

words = emailcontent.split()
print(len(words))

uniquewords = set(words)
print(len(uniquewords))

print(uniquewords)

cleanwords = []
for word in words:
    # word is instance of string class or word is a string object
    # remove is method inside the word object
    # remove takes 2 arguments, first arguments is used to find 
    # second argument is used to replace
    word = word.replace(",","")
    word = word.replace(".","")
    word = word.lower()
    cleanwords.append(word)

uniquewords = set (cleanwords)
print(len(uniquewords))
print(uniquewords)

commonwords = {"is","or","of","so","by","how","when","it","on","the","into","a","to","is","are", "what", "be","i","you","more","and","can","an"}

uniquewords = uniquewords.difference(commonwords)
print(len(uniquewords))
print(uniquewords)

spamwords = {"tricked","trick","phishing","security","criminals"}
print(uniquewords.intersection(spamwords))

