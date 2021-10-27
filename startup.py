with open('thisversion.txt') as f:
#    __version__ = f.read()
    __version__ = '0.0'
__versionindev__ = '.' + '1'
#__versionindev__ = ''
end_ofsupport = False
from time import sleep as wait
from os import startfile as start
import webbrowser
import requests
from tkinter import *
from tkinter import messagebox
def createtestscreen():
    logs = Tk()
    logs.title('Test screen')
    logs.resizable(0,0)
    wait(4)
    logs.destroy()

def check_updates():
    try:
        # -- Online Version File
        # -- Replace the url for your file online with the one below.
        response = requests.get(
            'https://raw.githubusercontent.com/Emila-Software/Emas-app/main/thisversion.txt?token=APFUAN5DSDJSE7LZZXGM5ETBL4K7O')
        data = response.text

        if float(data) == float("404"):
            messagebox.showinfo('End of support :(', 'Emīla Software software has stopped support for this Os we recommend to use the New Os')
        else:
            if float(data) > float(__version__):
                messagebox.showinfo('Software Update', 'Update Available!')
                mb1 = messagebox.askyesno('Update!', f'{__AppName__} {__version__}{__versionindev__} needs to update to version {data}')
                if mb1 is True:
                    # -- Replace the url for your file online with the one below.
                    webbrowser.open_new_tab('https://codeload.github.com/catko6583/Niko-XP/zip/refs/heads/main')
                    exit()
                else:
                    pass
            else:
                print('No new Updates')
    except Exception as e:
        print('Unable to Check for Update, Error: ' + str(e))
__AppName__ = 'Emas™ app'

print(f'{__AppName__} version {__version__}{__versionindev__}')
print("Please wait as we start the Opreating system")
print("In login the username is user and the password is 1234")
wait(1)
if not __version__ == '0.0':
    print("Checking for updates...")
    wait(4)
    check_updates()
    wait(0.10)
else:
    pass
print("testing screen...")
createtestscreen()
wait(4)
print("Working")
wait(0.10)
print("Checking if Emīla Software apps are working")
wait(4)
print("Working")
wait(0.10)
start('startupintro.pyw')