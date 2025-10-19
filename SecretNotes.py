from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import os

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

def save_Encrypt():
    title = e1.get()
    note = text.get("1.0",END)

    if not title or not note.strip():
        messagebox.showerror("Error","Please fill in everything.")
        return
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_note = fernet.encrypt(note.encode())

    filename = f"{title}.txt"
    with open(filename, "wb") as file:
        file.write(encrypted_note)

    messagebox.showinfo("Saved",f"Your note is encrypted. \nSave this key:\n\n{key.decode()}")
    e1.delete(0,END)
    text.delete("1.0",END)
    e2.delete(0,END)
def note_decrypt():
    title = e1.get()
    key = e2.get()
    if not title or not key:
        messagebox.showerror("Error","Please enter title and key")
        return
    filename = f"{title}.txt"
    if not os.path.exists(filename):
        messagebox.showerror("Error","File not found.")
        return
    try:
        with open(filename , "rb") as file:
            encrypted_note = file.read()
        fernet = Fernet(key.encode())
        decrypted = fernet.decrypt(encrypted_note).decode()
        text.delete("1.0",END)
        text.insert("1.0",decrypted)
    except:
        messagebox.showerror("Error","Decrypted failed. Check your key.")
button1.config(command=save_Encrypt)
button2.config(command=note_decrypt)

window.mainloop()