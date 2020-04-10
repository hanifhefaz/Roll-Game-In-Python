from tkinter import *
import random
import time
import random

top = Tk()
top.geometry("800x600")
top.title("Luck Roll")
#-------------------------------------------------------------------




#-------------------------------------------------------------------

#-------------------------------------------------------------------
def genrandom():
	rr = random.randrange(0,99)
	randomresult = Label(top, text = rr).place(x = 280,y = 150)
	if (rr == 1):
		multiplier = rr * 1.01
	elif (rr == 2):
		multiplier = rr * 1.02
	elif (rr == 3):
		multiplier = rr * 1.03
	elif (rr == 4):
		multiplier = rr * 1.04
	elif (rr == 5):
		multiplier = rr * 1.05
	elif (rr == 6):
		multiplier = rr * 1.06
	elif (rr == 7):
		multiplier = rr * 1.07
	elif (rr == 8):
		multiplier = rr * 1.08
	elif (rr == 9):
		multiplier = rr * 1.09
	else:
		multiplier = rr * 2
	multiplier_result = Label(top, text = multiplier).place(x = 280,y = 250)
	newac = multiplier_result + initial_amount
grand = Button(top, text = "Roll",activebackground = "pink", activeforeground = "blue",command = genrandom).place(x = 220, y = 150) 
 #------------------------------------------------------------------



top.mainloop()