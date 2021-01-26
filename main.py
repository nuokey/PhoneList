import shelve
from tkinter import *

def contacts():
	global last_i, name, number, delete_contact, contact_was
	with shelve.open("data.db") as data:
		tele_list = list(data.items())
	
	label_list = []

	if contact_was:
		for q in range(len(label_list)):
			label_list[q][0].destroy()
			label_list[q][1].destroy()
			label_list.pop(q)

	for i in range(len(tele_list)):
		name = Label(text = tele_list[i][0], bg = 'black', fg = 'white')
		number = Label(text = tele_list[i][1], bg = 'black', fg = 'white')
		delete_contact = Button(text = 'x', command = lambda: contact_delete(name))

		name.place(x = 10, y = 30 + i * 30, width = 100 ,height = 20)
		number.place(x = 120, y = 30 + i * 30, width = 100, height = 20)
		delete_contact.place(x = 225, y = 30 + i * 30, width = 20, height = 20)

		label_list.append((name, number))

		last_i = i
	
	contact_was = True

def contact_add():
	global last_i, plus_contact, enter_name, enter_number
	enter_name = Entry()
	enter_number = Entry()

	enter_name.place(x = 10, y = 30 + (last_i + 1) * 30, width = 100 ,height = 20)
	enter_number.place(x = 120, y = 30 + (last_i + 1) * 30, width = 100, height = 20)

	plus_contact['text'] = 'S'
	plus_contact['command'] = contact_safe

def contact_delete(name):
	with shelve.open('data.db') as data:
		data.pop(name['text'])

	contacts()

def contact_safe():
	global last_i, plus_contact, enter_name, enter_number
	with shelve.open('data.db') as data:
		data[enter_name.get()] = enter_number.get()

	enter_name.destroy()
	enter_number.destroy()

	plus_contact['text'] = '+'
	plus_contact['command'] = contact_add

	contacts()

root = Tk()
root.geometry("250x500")
root['bg'] = 'grey'

last_i = 0
contact_was = False

contacts()

root_name = Label(text = 'NuoPhone', bg = 'grey', fg = 'white')
root_name.place(x = 0, y = 0, width = 250, height = 30)

plus_contact = Button(text='+', bg = 'black', command = contact_add)
plus_contact.place(x = 225, y = 5, width = 20, height = 20)

root.mainloop()