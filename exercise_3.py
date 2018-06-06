import random

n = random.randint(1,10)

while True:
	guess= int(raw_input("guess a number 1 to 10"))
	if guess > n:
		print "guess is to high"
	elif guess < n:	
		print "guess is to low"
	else:
		print "you guess it", 
		break
