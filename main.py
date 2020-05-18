import tkinter as tk
import random
import time
import random


def roll():
	rolled = random.randint(0, 99)
	lbl_result["text"] = str(rolled)
	global balance
	if((balance>0) and (bet <= balance)):
		
		if((rolled > lucky_number) and (l["text"] == 'Greater')):
			if((lucky_number>=0) and (lucky_number<=10)):
				won = bet*1.1
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>10) and (lucky_number<=20)):
				won = bet*1.2
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>20) and (lucky_number<=30)):
				won = bet*1.3
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>30) and (lucky_number<=40)):
				won = bet*1.4
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>40) and (lucky_number<=50)):
				won = bet*1.5
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>50) and (lucky_number<=60)):
				won = bet*1.6
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>60) and (lucky_number<=70)):
				won = bet*1.7
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>70) and (lucky_number<=80)):
				won = bet*1.8
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>80) and (lucky_number<=90)):
				won = bet*1.9
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>90) and (lucky_number<=99)):
				won = bet* 2
				balance += won
				lbl_result_balance["text"] = balance
		elif((rolled > lucky_number) and (l["text"] == 'Smaller')):
			if((lucky_number>=0) and (lucky_number<=10)):
				lose = bet*2
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>10) and (lucky_number<=20)):
				lose = bet*1.9
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>20) and (lucky_number<=30)):
				lose = bet*1.8
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>30) and (lucky_number<=40)):
				lose = bet*1.7
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>40) and (lucky_number<=50)):
				lose = bet*1.6
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>50) and (lucky_number<=60)):
				lose = bet*1.5
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>60) and (lucky_number<=70)):
				lose = bet*1.4
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>70) and (lucky_number<=80)):
				lose = bet*1.3
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>80) and (lucky_number<=90)):
				lose = bet*1.2
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>90) and (lucky_number<=99)):
				lose = bet* 1.1
				balance -= lose
				lbl_result_balance["text"] = balance
		elif((rolled < lucky_number) and (l["text"] == 'Smaller')):
			if((lucky_number>=0) and (lucky_number<=10)):
				won = bet*2
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>10) and (lucky_number<=20)):
				won = bet*1.9
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>20) and (lucky_number<=30)):
				won = bet*1.8
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>30) and (lucky_number<=40)):
				won = bet*1.7
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>40) and (lucky_number<=50)):
				won = bet*1.6
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>50) and (lucky_number<=60)):
				won = bet*1.5
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>60) and (lucky_number<=70)):
				won = bet*1.4
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>70) and (lucky_number<=80)):
				won = bet*1.3
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>80) and (lucky_number<=90)):
				won = bet*1.2
				balance += won
				lbl_result_balance["text"] = balance
			elif((lucky_number>90) and (lucky_number<=99)):
				won = bet* 1.1
				balance += won
				lbl_result_balance["text"] = balance
		elif((rolled < lucky_number) and (l["text"] == 'Greater')):
			if((lucky_number>=0) and (lucky_number<=10)):
				lose = bet*2
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>10) and (lucky_number<=20)):
				lose = bet*1.9
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>20) and (lucky_number<=30)):
				lose = bet*1.8
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>30) and (lucky_number<=40)):
				lose = bet*1.7
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>40) and (lucky_number<=50)):
				lose = bet*1.6
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>50) and (lucky_number<=60)):
				lose = bet*1.5
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>60) and (lucky_number<=70)):
				lose = bet*1.4
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>70) and (lucky_number<=80)):
				lose = bet*1.3
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>80) and (lucky_number<=90)):
				lose = bet*1.2
				balance -= lose
				lbl_result_balance["text"] = balance
			elif((lucky_number>90) and (lucky_number<=99)):
				lose = bet* 1.1
				balance -= lose
				lbl_result_balance["text"] = balance
		else:
			balance = balance + (bet * 3)
		
	else:
		lbl_result["text"] = "Balance is not enough!"


def set_balance():
	global balance
	balance = int(ent_value_balance.get())
	lbl_result_balance["text"] = balance
	if(balance>0):
		btn_convert["state"] = "disabled"
	elif(balance<=0):
		btn_convert["state"] = "disabled"
		btn_convert_bet["state"] = "disabled"
		btn_convert_lucky["state"] = "disabled"
		lbl_result["text"] = "Please recharge your account!"



def set_lucky_number():
	global lucky_number
	lucky_number = int(ent_value_lucky.get())
	lbl_result_lucky["text"] = lucky_number

def set_bet():
	global bet
	global balance
	bet = int(ent_value_bet.get())
	lbl_result_bet["text"] = bet

def print_selection():
	global l
	l.config(text= var.get())


window = tk.Tk()

#--------------------------------------------------------------------------

frm_entry_bet = tk.Frame(master=window)
ent_value_bet = tk.Entry(master=frm_entry_bet, width=10)
ent_value_bet.grid(row=0, column=0, sticky="e")
btn_convert_bet = tk.Button(
    master=window,
    text="SET",
    command = set_bet
)
lbl_result_bet = tk.Label(master=window, text="Bet = 0")
frm_entry_bet.grid(row=10, column=0, padx=10)
btn_convert_bet.grid(row=10, column=1, pady=10)
lbl_result_bet.grid(row=10, column=2, padx=10)

#--------------------------------------------------------------------------

var = tk.StringVar()
l = tk.Label(window, bg='white', width=20, text='empty')
l.grid(row=30, column=2, padx=10)
r1 = tk.Radiobutton(window, text='Greater', variable=var, value='Greater', command=print_selection)
r1.grid(row=30, column=0, padx=10)
r2 = tk.Radiobutton(window, text='Smaller', variable=var, value='Smaller', command=print_selection)
r2.grid(row=30, column=1, padx=10)


#--------------------------------------------------------------------------

frm_entry_balance = tk.Frame(master=window)
ent_value_balance = tk.Entry(master=frm_entry_balance, width=10)
ent_value_balance.grid(row=0, column=0, sticky="e")
btn_convert = tk.Button(
    master=window,
    text="SET",
    command = set_balance
)
lbl_result_balance = tk.Label(master=window, text="Balance = 0")
frm_entry_balance.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result_balance.grid(row=0, column=2, padx=10)

#---------------------------------------------------------------------------

frm_entry_lucky = tk.Frame(master=window)
ent_value_lucky = tk.Entry(master=frm_entry_lucky, width=10)
ent_value_lucky.grid(row=0, column=0, sticky="e")
btn_convert_lucky = tk.Button(
    master=window,
    text="SET",
    command = set_lucky_number
)
lbl_result_lucky = tk.Label(master=window, text="Lucky Number")
frm_entry_lucky.grid(row=20, column=0, padx=10)
btn_convert_lucky.grid(row=20, column=1, pady=10)
lbl_result_lucky.grid(row=20, column=2, padx=10)

#--------------------------------------------------------------------------

btn_roll = tk.Button(text="Roll", command=roll)
lbl_result = tk.Label()
btn_roll.grid(row=40, column=1, sticky="nsew")
lbl_result.grid(row=40, column=2)

#--------------------------------------------------------------------------




window.mainloop()