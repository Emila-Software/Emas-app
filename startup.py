with open('thisversion.txt') as f:
    __version__ = f.read()
__versionindev__ = '0.1'
end_ofsupport = False
from time import sleep as wait
from os import startfile as start
import webbrowser
import requests
from tkinter import *
from tkinter import messagebox

from win32api import MessageBox
logs = Tk()
logs.title('Test screen')
logs.resizable(0,0)


def check_updates():
    try:
        # -- Online Version File
        # -- Replace the url for your file online with the one below.
        response = requests.get(
            'https://raw.githubusercontent.com/Emila-Software/Emas-app/main/thisversion.txt?token=APFUANZAVEORYHWUF47SPFLBLBEDM')
        data = response.text

        if float(data) == float("404"):
            messagebox.showinfo('End of support :(', 'Niko software has stopped support for this Os we recommend to use the New Os')
        else:
            if float(data) > float(__version__):
                messagebox.showinfo('Software Update', 'Update Available!')
                mb1 = messagebox.askyesno('Update!', f'{_AppName_} {__version__} needs to update to version {data}')
                if mb1 is True:
                    # -- Replace the url for your file online with the one below.
                    webbrowser.open_new_tab('https://codeload.github.com/catko6583/Niko-XP/zip/refs/heads/main')
                    exit()
                else:
                    pass
            else:
                print('No new Updates')
    except Exception as e:
        print('Unable to Check for Update, Error:' + str(e))
_AppName_ = 'Niko XP'
with open('nikosoftware', 'w') as f:
    f.write('no')

print("Niko XP version " + __version__ + __versionindev__)
print("Please wait as we start the Opreating system")
print("In login the username is user and the password is 1234")
wait(1)
print("Checking for updates...")
wait(4)
check_updates()
wait(0.10)
print("testing screen...")
wait(4)
logs.destroy()
print("Working")
wait(0.10)
print("Checking if Niko apps are working")
wait(4)
print("Working")
wait(0.10)
start('login.pyw')
