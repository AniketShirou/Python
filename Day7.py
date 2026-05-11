import random

computer = random.randint(0, 100)

user = int(input("Guess a number from 0 to 100: "))

count = 1

while user != computer:
      if(user > computer):
            print("Guess a lower number: ", end = " ")
      elif(user < computer):
            print("Guess a higher number: ", end = " ")
            
      count += 1
      user = int(input())

print("Bingo!!!")                
print("you took: ", count , "attempt to guess the number right")      
