from os import path
from tkinter import *
from tkinter import ttk

from audio import Audio

# temp file
FILE_NAME = path.abspath(".") + path.sep + "test.mp3"
print(FILE_NAME)

audio = Audio()
audio.load(FILE_NAME)
audio.slice()

# UI part
root = Tk()
root.title("Once More")
root.resizable(width=False, height=False)
mainFrame = ttk.Frame(root)

previous = ttk.Button(mainFrame, text="pre", command=audio.previewSlice).pack(side=LEFT)
next = ttk.Button(mainFrame, text="replay", command=audio.playSlice).pack(side=LEFT)
replay = ttk.Button(mainFrame, text="next", command=audio.nextSlice).pack(side=LEFT)

mainFrame.pack()
root.mainloop()
