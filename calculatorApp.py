import tkinter as tk

root = tk.Tk()
root.title("Calculator")
# root.geometry("1000x500")
buttonframe = tk.Frame(root)
buttonframe.grid(row = 3, column = 0, columnspan = 2)
label1 = tk.Label(root, text = "This is a Calculator app.", font = ("ComicSansMS", 24, "bold"))
label1.grid(row = 0, column = 0, columnspan = 2)
label2 = tk.Label(root, text = "Choose your first number:")
label2.grid(row = 1, column = 0, padx = 10)
entry1 = tk.Entry(root)
entry1.grid(row = 1, column = 1, padx = 10)
label3 = tk.Label(root, text = "Choose your second number:")
label3.grid(row = 2, column = 0, padx = 10)
entry2 = tk.Entry(root)
entry2.grid(row = 2, column = 1, padx = 10)
label4 = tk.Label(root, text = f"")
label4.grid(row = 4, column = 0, pady = 10)
def add():
    a = float(entry1.get())
    b = float(entry2.get())
    answer = a + b
    label4.config(text = f"This is your answer: {answer}")
addbutton = tk.Button(buttonframe, text = "+", command = add)
addbutton.grid(row = 0, column = 0)
def minus():
    a = float(entry1.get())
    b = float(entry2.get())
    answer = a - b
    label4.config(text = f"This is your answer: {answer}")
minusbutton = tk.Button(buttonframe, text = "-", command = minus)
minusbutton.grid(row = 0, column = 1)
def times():
    a = float(entry1.get())
    b = float(entry2.get())
    answer = a * b
    label4.config(text = f"This is your answer: {answer}")
timesbutton = tk.Button(buttonframe, text = "*", command = times)
timesbutton.grid(row = 0, column = 2)
def divide():
    a = float(entry1.get())
    b = float(entry2.get())
    answer = a / b
    label4.config(text = f"This is your answer: {answer}")
dividebutton = tk.Button(buttonframe, text = "/", command = divide)
dividebutton.grid(row = 0, column = 3)
root.mainloop()
