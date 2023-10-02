from random import randint
num = randint(1,100)
guess = 0
print("I have chosen a random number...\n")
answer  = int(input("Enter a number: "))


while True:
        if num > answer:
        	print("That's too low")
        	guess += 1
        	answer  = int(input("Enter a number: "))
        elif num < answer:
        	print("That's too high")
        	guess += 1
        	answer  = int(input("Enter a number: "))
        elif num == answer:
        	guess += 1
        	print(f"Thats correct, it took you {guess} guesses.")
        	guess = 0
        	answer2 = input("Do you want to play again? (Y/N)\n")
        	if answer2 == ("Y"):
                	print("I have chosen a random number")
                	answer  = int(input("Enter a number: "))
        	else:
                	print("Thanks")
                	break	
