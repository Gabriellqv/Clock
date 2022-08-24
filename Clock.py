from tkinter import *
import tkinter
from datetime import datetime
import pyglet
pyglet.font.add_file("digital-7.ttf")

color1 = "#3d3d3d"
color2 = "#dedcdc"

window = Tk()
window.title("")
window.geometry("300x170")
window.resizable(width = FALSE, height = FALSE)
window.configure(bg = color1)


def clock():
    time = datetime.now()
    hour = time.strftime("%H:%M:%S")
    weekday = time.strftime("%A")
    day = time.day
    month = time.strftime("%b")
    year = time.strftime("%Y")

    l1.config(text = hour)
    l1.after(200, clock)
    l2.config(text = weekday + "   " + str(day) +
            "/" + str(month) + "/" + str(year))

    print(hour)
    print(day)
    print(month)
    print(year)


l1 = Label(window, text = "", font = ("digital-7 70"), bg = color1, fg = color2)
l1.grid(row = 0, column = 0, sticky = NW, padx = 5)

l2 = Label(window, text = "", font=("digital-7 20"), bg = color1, fg = color2)
l2.grid(row = 1, column = 0, sticky = NW, padx = 5)

clock()

window.mainloop()