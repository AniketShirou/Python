# string creation

s = 'hello'
s = "hello"

#multi-line strings 
s = '''hello'''
s = """hello"""

print(s)


# accessing character from strings
s = "aniket"

#positive indexing
print(s[4])

#negative indexing
print(s[-3])

#slicing
print(s[0:len(s)])

#reverse a string
print(s[::-1])


# editing and deleting in string is not possible
# but whole string can be deleted using ( del ) keyword

# del s
# print(s)

# operators in strings
print("aniket" + "rana")
print("aniket " * 10)
print("aniket" >= "rana")
print("aniket" != 'rana')
print("hello" or "world")
print("hello" and "world")
print(not "aniket")
print('a' is 'aniket')


# string functions
s = "aniketz rana"
print(len(s))
print(max(s)) # prints largest char from string
print(min(s)) # prints smallest char from string
print(sorted(s)) # sorts the string, and convert it into list
print(sorted(s, reverse=True))


# format function in string
name = "aniket"
gender = "male"

print(f"Hi, my name is {name} and my gender is {gender}")
print("Hi, my name is {} and my gender is {}".format(name, gender))


#split , join and replace
s = "my name is nitish"
print(s.split("is"))
print(" ".join(s.split("is")))
print(s.replace("nitish", "iiit"))