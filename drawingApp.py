import tkinter as tk
from tkinter import ttk, filedialog
from PIL import ImageGrab

root = tk.Tk()
root.title("Drawing app")
colors = ["RED", "ORANGE", "YELLOW", "GREEN", "LIGHTBLUE", "PURPLE", "PINK", "BLACK", "GREY", "WHITE"]
colorlist = ttk.Combobox(root, values = colors, state = "readonly")
colorlist.grid(row = 5, column = 0)
index = colorlist.current()
colorlist.set("WHITE")
canvas = tk.Canvas(root, bg = "white", width = 700, height = 600)
canvas.grid(row = 0, column = 0)
def changebg(event):
    selected_color = colorlist.get()
    print(selected_color)
    canvas.config(bg = selected_color.lower())
colorlist.bind("<<ComboboxSelected>>", changebg)
lastx, lasty = None, None
color = "red"
buttonframe = tk.Frame(root)
buttonframe.grid(row = 1, column = 0)
buttonframe2 = tk.Frame(root)
buttonframe2.grid(row = 2, column = 0)
def startdraw(event):
    global lastx, lasty
    lastx, lasty = event.x, event.y
def draw(event):
    global lastx, lasty, color
    scale = scalebar.get()
    canvas.create_line(lastx, lasty, event.x, event.y, fill = color, width = scale)
    lastx, lasty = event.x, event.y
canvas.bind("<Button-1>", startdraw)
canvas.bind("<B1-Motion>", draw)
def clearcanvas():
    canvas.delete("all")
button = tk.Button(buttonframe2, text = "CLEAR", command = clearcanvas)
button.grid(row = 0, column = 1, pady = 10)
def blue():
    global color
    color = 'RoyalBlue2'
bluebutton =  tk.Button(buttonframe, text = "BLUE", command = blue, fg =  "RoyalBlue2")
bluebutton.grid(row = 0, column = 4, pady = 10)
def green():
    global color
    color = 'green4'
greenbutton =  tk.Button(buttonframe, text = "GREEN", command = green, fg = "green4")
greenbutton.grid(row = 0, column = 3, pady = 10)
def red():
    global color
    color = 'red'
redbutton =  tk.Button(buttonframe, text = "RED", command = red, fg = "red")
redbutton.grid(row = 0, column = 0, pady = 10)
def yellow():
    global color
    color = 'gold'
yellowbutton =  tk.Button(buttonframe, text = "YELLOW", command = yellow, fg = "gold")
yellowbutton.grid(row = 0, column = 2, pady = 10)
def purple():
    global color
    color = 'dark violet'
purplebutton =  tk.Button(buttonframe, text = "PURPLE", command = purple, fg = "dark violet")
purplebutton.grid(row = 0, column = 5, pady = 10)
def orange():
    global color
    color = 'dark orange'
orangebutton =  tk.Button(buttonframe, text = "ORANGE", command = orange, fg = "dark orange")
orangebutton.grid(row = 0, column = 1, pady = 10)
def black():
    global color
    color = 'black'
blackbutton =  tk.Button(buttonframe, text = "BLACK", command = black, fg = "black")
blackbutton.grid(row = 0, column = 7, pady = 10)
def pink():
    global color
    color = 'PaleVioletRed1'
pinkbutton =  tk.Button(buttonframe, text = "PINK", command = pink, fg = "PaleVioletRed1")
pinkbutton.grid(row = 0, column = 6, pady = 10)
def grey():
    global color
    color = 'gray49'
greybutton =  tk.Button(buttonframe, text = "GREY", command = grey, fg = "gray49")
greybutton.grid(row = 0, column = 8, pady = 10)
def erase():
    global color
    color = "white"
erasebutton =  tk.Button(buttonframe2, text = "ERASE", command = erase, fg = "black")
erasebutton.grid(row = 0, column = 2, pady = 10)
def save():
    filepath = filedialog.asksaveasfilename(defaultextension = ".png", filetypes = [("PNG files", "*.png")])
    root.update()
    if filepath:
        x = root.winfo_rootx()+canvas.winfo_rootx()
        y = root.winfo_rooty()+canvas.winfo_rooty()
        xend = x + canvas.winfo_width() + canvas.winfo_width()
        yend = y + canvas.winfo_height() + canvas.winfo_height()
        print(x, y, xend, yend)
        ImageGrab.grab().crop((x, y, xend, yend)).save(filepath)
savebutton = tk.Button(buttonframe2, text = "SAVE", command = save, fg = 'black')
savebutton.grid(row = 0, column = 0)
scalebar = tk.Scale(root, from_ = 1, to = 10, orient = tk.HORIZONTAL)
scalebar.grid(row = 3, column = 0, pady = 10)
root.mainloop()