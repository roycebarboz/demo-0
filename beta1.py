from cProfile import label
from cgitb import text
from email.mime import image, message
from tkinter import *
from tkinter import messagebox
from turtle import width, window_width
window =Tk()
window.title("Login Page")
window.geometry("1920x1080")

def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

Label1= Label(window, text = "Symptomate", width=100, height=5, bg=rgb_hack((10,172,185)), font=("Time New Roman", 25))
Label1.pack(padx=10 , pady=10)

nameL= Label(window, text = "Username: ", font=("Time New Roman", 20))
nameL.place(x=100, y=300)

nameE = Entry(window, font=("Times New Roman", 20),borderwidth=3, width=20, bg=rgb_hack((10,172,185)))
nameE.place(x= 250, y=300)

passL= Label(window, text = "Password: ", font=("Time New Roman", 20))
passL.place(x=100, y=450)

passE = Entry(window, font=("Times New Roman", 20), borderwidth=3, show=("*"), width=20, bg=rgb_hack((10,172,185)))
passE.place(x= 250, y=450)

def login():
  user = nameE.get()
  passw = passE.get()
  if user=="" and passw=="":
    messagebox.showerror("Fill all the details")
  elif user=="harshilsp" and passw=="1234":
    messagebox.showinfo("Logged In Successfully")
  else:
    messagebox.showerror("Invalid Credentials")


loginButton = Button(window, text ="Login", font=("Times New Roman", 20), command=login, borderwidth=8, width=8, bg=rgb_hack((10,172,185)))
loginButton.place(x= 150, y=550)

RegButton = Button(window, text ="Register", font=("Times New Roman", 20), borderwidth=8, width=8, bg=rgb_hack((10,172,185)))
RegButton.place(x= 400, y=550)

photo = PhotoImage(file="C:\Users\Royce Barboz\Downloads\ph.png")
PhotoL = Label(image=photo)
PhotoL.place(x=700, y=250)

window.mainloop()