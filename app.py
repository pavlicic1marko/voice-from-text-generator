from gtts import gTTS
import os
from tkinter import *


def pronounce():
    text = entry.get()
    language = 'en'
    audio_output = gTTS(text=text, lang=language, slow=False)
    audio_output.save('app_audio.mp3')
    os.system("start app_audio.mp3")


root = Tk()
canvas = Canvas(root, width=400, height=300)
canvas.pack()

entry = Entry(root)
canvas.create_window(200, 180, window=entry)

button = Button(text="Start", command=pronounce)
canvas.create_window(200, 230, window=button)

root.mainloop()