from tkinter import ttk
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from Speach2Text import STT
import sys
sys.path.append('../summary/')
from Base_Summary import Final_Summary

# Root Setup
root = tk.Tk()
text = tk.Text(root)


# setting the minimun size of the root window
root.minsize(400, 400)
# Background Color of the window
root.configure(background='#242F3E')

myFont = Font(family="Times New Roman", size=12,)
text.configure(font=myFont)

myFont.configure(size=30)


root.title('Recorder and Transcript')

img = PhotoImage(file='../image/microphone.png')
root.tk.call('wm', 'iconphoto', root._w, img)

style = ttk.Style()
style.theme_use('clam')

photo = PhotoImage(file='../image/microphone.png').subsample(40, 40)




label1 = ttk.Label(root, text='To record the audio click the recorder and to stop click once again.')
label1.grid(row=0, column=0)

btn2 = tk.StringVar()

# Play the original audio
PlayButton = ttk.Button(root, text='Play Original', width=20, command=STT.play_original)
PlayButton.grid(row=10, column=0 , padx=10,pady=10)

# Play the Summarized audio
PlayButton = ttk.Button(root, text='Play Summary', width=20, command=STT.play_summary)
PlayButton.grid(row=11, column=0 , padx=10,pady=10)

# Display the summarized result
MyButton1 = ttk.Button(root, text='Summary', width=20, command=STT.display_summary)
MyButton1.grid(row=15, column=0,padx=10,pady=10)





MyButton3 = ttk.Button(root, image=photo, command=STT.buttonClick)#, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton3.grid(row=5, column=0 , padx=10,pady=10)

root.wm_attributes('-topmost', 1)
btn2.set('google')
root.mainloop()