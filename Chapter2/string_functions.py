name = "aniket Rana Rana"

#length of string
print("Length of String: ", len(name))

#endswith
print(name.endswith('na'))

#startswith
print(name.startswith(("An")))

#Captalize: Only first letter capital
print(name.capitalize())

#title : Every first letter capital(after space)
print(name.title())

#upper : convert all to uppercase
print(name.upper())

#lower: convert all to uppercase
print(name.lower())

#strip : delete any occurance of character from starting and ending ( default : whitespace )
username = "_!__JohnDoe!__!!"
print(username.strip('!_'))


#convert to string
a = 45
print(str(a));
print(type(str(a)))

#replace particular word
print(name.replace("Rana", "Singh"))

#split: spiling with respect to particular character anc converting to string
print(name.split('R'))

#Join: Joins elements of an iterable into a string using this string as separator.
print("-".join(["aniket", "rana", "from", "haryana"]))

#find: Finds the first occurrence of a substring; returns -1 if not found.
print(name.find("R"))

#isalpha/ isdigit -> these are common