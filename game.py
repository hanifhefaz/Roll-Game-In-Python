from tkinter import *
import random
import time
import random

print("Welcome")
startamount = int(input("Please enter your start amount:"))
print("Your balance is: ", startamount)

betamount = int(input("Please enter your bet amount:"))
if (betamount>startamount):
	print("You dont have enough balance")
balance = startamount - betamount
print("Your balance is: ", balance)
while True:
	selectnumber = int(input("Please select your lucky number:"))
	print("Your lucky number is: ", selectnumber)

	print("Select if generated number will be greater or smaller then your lucky number")
	selectchoice = input("Type G for greater and S for smaller: ")
	print("Your choice is: ",selectchoice)

	rolldraw = input("Type !r to roll: ")

	if (rolldraw == '!r'):
		rand = random.randint(0,99)
		print("The random number generated is: ", rand)
		if((rand > selectnumber) and (selectchoice == 'G')):
			won = betamount * 2
			balance = balance + won
			print("Congrats! you won",won)
			print("Your curret balance is: ",balance)
		elif ((rand > selectnumber) and (selectchoice == 'S')):
			lost = betamount
			balance = balance - betamount
			print("Sorry you lost ",lost)
			print("Your curret balance is: ",balance)
		elif ((rand < selectnumber) and (selectchoice == 'S')):
			won = betamount * 2
			balance = balance + won
			print("Congrats! you won",won)
			print("Your curret balance is: ",balance)
		elif ((rand < selectnumber) and (selectchoice == 'G')):
			lost = betamount
			balance = balance - betamount
			print("Sorry you lost ",lost)
			print("Your curret balance is: ",balance)
		else:
			print("Though Luck")

	else:
		print("Please type '!r' ")
