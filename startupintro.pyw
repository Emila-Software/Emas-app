import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
from time import sleep as wait
from os import startfile as start
from sys import exit as sexit

video_name = "intro.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image
    start('login.pyw')
    root.destroy()


if __name__ == "__main__":

    root = tk.Tk()
    root.title('')
    root.iconbitmap("white.ico")
    root.resizable(0,0)
    my_label = tk.Label(root)
    my_label.pack()
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop()