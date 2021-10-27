def Warning():
    mbox.showwarning('Uh Oh', 'you are not supposed to go there!')
def Error():
    mbox.showerror('Uh Oh', 'there was a error while doing this!')
def restartos():
    os.startfile('startup.py')
    sys.exit('Restarted os')
def shutdown():
    sys.exit('Shutdowned os')
def logout():
    os.startfile('login.pyw')
    sys.exit('Logout')
def opennoviruses():
    start('antivirus.pyw')
def browser():
    start('browse.pyw')
def openfiles():
    start('file.pyw')
def editfiles():
    start('edit.pyw')

from tkinter import *
from tkinter import messagebox as mbox
import sys
import os
from os import startfile as start

logs = Tk()
logs.geometry("500x500")
logs.title('Emas APP')
logs.resizable(0,0)
logs.iconbitmap("white.ico")
def Smenu():
    S = Tk()
    S.geometry("30x65")
    S.title('Shutdown Menu')
    restart = Button(S, bg = "yellow", text = "Restart", fg = "orange", command=restartos)
    restart.place(x = 0, y = 0)
    Shutdown = Button(S, bg = "yellow", text = "Shutdown", fg = "orange", command=shutdown)
    Shutdown.place(x = 0, y = 20)
    Logoff = Button(S, bg = "yellow", text = "Log Out", fg = "orange", command=logout)
    Logoff.place(x = 0, y = 40)
    S.mainloop()
Sbutton = Button(logs, bg = "yellow", text = "Shutdown Menu", fg = "orange", command=Smenu)
Sbutton.place(x = 0, y = 475)
Browse = Button(logs, bg = "yellow", text = "Browser", fg = "orange", command=browser)
Browse.place(x = 50, y = 0)
Open = Button(logs, bg = "blue", text = "This PC", fg = "black", command=openfiles)
Open.place(x = 0, y = 0)
notepad = Button(logs, bg = "yellow", text = "text editor", fg = "orange", command=editfiles)
notepad.place(x = 125, y = 0)
Opene = Button(logs, bg = "yellow", text = "Niko antivirus", fg = "orange", command=opennoviruses)
Opene.place(x = 0, y = 20)
logs.mainloop()
