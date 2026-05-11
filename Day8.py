# for loops

#range:
for i in range(0, 11, 2):
    print(i)

print()

# reverse: ( start > end )
for i in range(5, 0, -1):
    print(i)    

print()

# sequence
a = [1,2,3,4,5]
for i in a:
    print(i)    


# nested-loops
'''
*
**
***
****
******
'''

for i in range(0, 5):
    for j in range(0, i+1):
        print("*", end=" ")
    print()    
