from tkinter import *


aboutScreen = Tk()
aboutScreen.geometry("640x480")
aboutScreen.title("About pIDE")

t = Label(master=aboutScreen, text="This section isn't complete.", font=("Segoe UI", 16))
t.pack()

aboutScreen.mainloop()