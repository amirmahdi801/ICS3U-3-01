from random import *
print ("this is a game which you should find the number")
No = randint(1,10000)
while True:  
    guess = input("guess what the number is: ")
    guess = int(guess)
    if guess == No :
        print ("YOU DID iT :)")
        break
    elif guess > No :
        print ("your number is bigger than my number")
    elif guess < No :
        print ("your number is smaller than my number")