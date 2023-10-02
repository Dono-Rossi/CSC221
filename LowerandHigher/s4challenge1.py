from random import randint

num = randint(1, 1000)
print("I chose a random number")

question = "ask a number"
ans = int(input(question))

if ans == num:
	print("thats correct!")

else:
	print("incorrect")
