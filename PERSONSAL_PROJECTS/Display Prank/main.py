import tkinter
import random
from PIL import Image , ImageTk
root = tkinter.Tk()
root.attributes('-fullscreen',True)
root.attributes('-topmost',True)
root.attributes('-transparentcolor')
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
canvas = tkinter.Canvas(root , width=width , height=height,highlightthickness=0)
canvas.pack
img = Image.open('shit.png')
shit_img = ImageTk.PhotoImage(img)

def add_shit():
   x = random.randint(0,width)
   y = random.randint(0,height)
   canvas.create_image(x,y,image=shit_img)
   root.after(500,add_shit)
add_shit()   
root.mainloop()
