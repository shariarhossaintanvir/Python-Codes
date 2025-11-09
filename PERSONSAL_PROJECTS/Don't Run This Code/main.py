import tkinter
root = tkinter.Tk()
root.attributes('-fullscreen', True)
root.attributes('-topmost', True)
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.mainloop()