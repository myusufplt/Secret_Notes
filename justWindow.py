from tkinter import *

#Ekran
window = Tk()
window.title("Secret Notes")
window.minsize(width=450,height=750)

#Logo
image = PhotoImage(file="logo.png")
logo =  Label(window , image=image)
space = Label()
space.config(pady=5)
logo.pack()
space.pack()

#label1 - entry1
l1 = Label(text="Enter Your Title",font=('lucida',20,"bold"))
l1.pack()
e1 = Entry()
e1.pack()

#label2 - text
l2 = Label(text="Enter Your Secret Note",font=('lucida',20,"bold"))
l2.pack()
text = Text(width=45,height=25)
text.pack()

#label3 - entry2
l3 = Label(text="Enter Key",font=('lucida',20,"bold"))
e2 = Entry(width=30)
l3.pack()
e2.pack()

#button1,2
button1 = Button(text="Save And Encrypt")
button2 = Button(text="Decrypt")
button1.pack()
button2.pack()

window.mainloop()