from tkinter import *
import string
import random
import pyperclip

def generator():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special = string.punctuation

    all = small_alphabets + capital_alphabets + numbers + special
    password_length = int(length_Box.get())

    if choice.get() == 1:
        passwordfield.insert(0, random.sample(small_alphabets,password_length))
    
    if choice.get() == 2:
        passwordfield.insert(0, random.sample(small_alphabets+capital_alphabets+numbers, password_length))
    
    if choice.get() == 3:
        passwordfield.insert(0, random.sample(all,password_length))


def copy():
    password = passwordfield.get()
    pyperclip.copy(password)

root = Tk()
root.config(bg="antiquewhite1")
root.geometry("500x400")
choice = IntVar()
Font=('arial',13,'bold')

passwordLabel = Label(root, text='Password Generator', font=('times new roman', 18, 'bold'),bg='antiquewhite1')
passwordLabel.grid(pady=10, padx=140)

weakbutton = Radiobutton(root,text='Weak Password',value=1,variable=choice, font=Font, bg='aquamarine1')
weakbutton.grid(pady=7)

mediumbutton = Radiobutton(root, text='Medium Password', value=2, variable=choice, font=Font, bg='aquamarine1')
mediumbutton.grid(pady=7)

strongbutton = Radiobutton(root, text='Strong Password', value=3, variable=choice, font=Font, bg='aquamarine1')
strongbutton.grid(pady=7)

lengthlabel = Label(root, text='Choose your Password Length',font=Font, bg='antiquewhite1')
lengthlabel.grid(pady=7)

length_Box = Spinbox(root, from_=5, to_=18, font=Font, width=5)
length_Box.grid(pady=7)



passwordfield = Entry(root, width=25, bd=2, font=Font)
passwordfield.grid(pady=7)

generateButton = Button(root, text='Generate Password', font=Font, command=generator)
generateButton.grid(pady=7)

copyButton = Button(root, text='Copy Password', font=Font, command=copy)
copyButton.grid(pady=7)
root.mainloop()