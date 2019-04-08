print ("this is a game which you should find the number")
while True:
    yes_list = ["yes", "y", "yeah"]
    No = 1381
    guess = input("guess what the number is: ")
    guess = int(guess)
    if guess == No :
        print ("YOU DID iT :)")
        break
    elif guess > No :
        print ("your number is bigger than my number")
    elif guess < No :
        print ("your number is smaller than my number")