from tkinter import *
from tkinter import messagebox as mbox
from os import startfile as start
from time import sleep as wait
antivirus = Tk()
antivirus.geometry("30x65")
antivirus.title('Niko Software antivirus (free version)')
def check():
    wait(3)
    mbox.showinfo('Report', 'We found no viruses in Emas APP')
def close():
    start('python.py')
checkforviruses = Button(antivirus, bg = "Red", text = "Check for viruses", command=check)
checkforviruses.place(x = 0, y = 0)
closemenu = Button(antivirus, bg = 'Yellow', text = "Close", command=close)
closemenu.place(x = 0, y = 20)
antivirus.mainloop()
